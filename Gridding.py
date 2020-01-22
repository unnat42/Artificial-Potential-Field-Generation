'''
Created by: Unnat Antani
Date: 20 Jan, 2020

Gridding the map that is captured and getting nodes and obstacles from it.

'''
import matplotlib.pyplot as plt
import cv2
try:
    from PIL import Image
except ImportError:
    import Image


    
def get_obstacle(image, nodes):#Gets the obstacles which are black in colour and stored their position
    image  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    obstacle = []
    for i in nodes:
        if image[i[0]][i[1]] < 10:
            obstacle.append(i)
    return obstacle 
     
def grid(fig,ax,no_blocks,width,height):#Discretizes the map and hece grids it for faster processing
    nodes = []
    for i in range(no_blocks):
        new_x = round(i*width/no_blocks)
        new_y = round(i*height/no_blocks)
        for j in range(no_blocks):
            nodes.append([new_x,round(j*height/no_blocks)])
        nodes.append([new_x,new_y])
        plt.axvline(x = new_x, color = 'r')
        plt.axhline(y = new_y, color = 'r')
    return nodes
    


if __name__ == "__main__":

    #Put the main code here
    
    
    image_shape = cv2.imread("test_map.png") #Read the map you want function to be applied on 
    image_shape = cv2.resize(image_shape,(1120,1120))

    width = image_shape.shape[1]
    height = image_shape.shape[0]
    
    image = Image.open('test_map.png')
    my_dpi=250
    
    
    fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
    ax=fig.add_subplot(111)
    
    # Remove whitespace from around the image
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    no_blocks = 20  #Can change this for accuracy. Higher the number, more accurate but costlier the computation
    nodes = grid(fig,ax,no_blocks,width,height)
    # print(nodes)
    ax.imshow(image)
    print("\nSaving the grid file...")
    fig.savefig('test_grid.jpg')
    print("SAVED !")
    print("Getting obstacle positions please wait.....")
    obstacle = get_obstacle(image_shape, nodes)
    print("Obstacles detected")
    print("Obstacles are at: {}".format(obstacle))
    
    
  
    plt.show()
    
    