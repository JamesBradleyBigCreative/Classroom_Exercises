import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,250]) ## x and y axis plotting

plt.plot(x,y) ## To plot without a line put a o string at the end of the function parameters plt.plot(x,y,'o')
plt.show()

#Multiple points

x1 = np.array([1,2,6,8])
y1 = np.array([3,8,1,10]) # draw a line from (1,3) to (2,8) to (6,1) and finally (8,10)

plt.plot(x1,y1)
plt.show()

#if we do not have x values they will get default values depending on the length of the y axis.

#Marker

yp = np.array([3,8,1,10])

plt.plot(yp,marker = 'o') # Each point has a circle on it, you can do different symbols like a star with * instead of o
plt.show()

#Format strings

plt.plot(yp, 'o:r') #Formats the line, Marker/Line/Color
plt.show()

# Marker size

plt.plot(yp,marker = 'o',ms =20) #Marker size is ms, so in this case its 20.
plt.show()

# Marker color edge

plt.plot(yp,marker = '*',ms = 20,mec = 'r') #Changes the edge color with mec to red.
plt.show()

#Marker color Face

plt.plot(yp,marker = '*',ms = 20,mfc = 'r') # Changes colour of the marker face, mfc and mec togehter colour the whole marker
plt.show()

#Line style

plt.plot(yp,linestyle = 'dotted') #you can do dotted,dashed others aswell dashdot,solid
plt.show()

#you can shorten it by doing this

plt.plot(yp,ls = ':') 
plt.show()

#line color

plt.plot(yp,color ='r') #you can also use hexadecimal values for colour
plt.show()

#line width

plt.plot(yp,linewidth = '20.5') #Changes the width to 25.5
plt.show()

#multiple lines

y1 = np.array([3,8,1,10]) #you can also use specified y and x axis to plot multiple lines.
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()

#Labels and title

x2 = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y2 = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x2,y2)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15} #Sets a dictionary with font data

plt.title('Sports Watch Data',fontdict = font1,loc = 'left') #you can use the loc parameter to position the title 
plt.xlabel('Average Pulse',fontdict = font2) #sets the font information for each label and title
plt.ylabel('Calorie Burnt',fontdict = font2)

#grid lines

plt.grid(color = 'green',linestyle = '--',linewidth = 0.5) #this function adds grids and you can specify by adding a parameter called axis and asigning it to a axis. x or y

plt.show()

#Subplot Draw multiple plots together

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1) # Takes 3 argumets, Row and column then order.
plt.plot(x,y)
plt.title('Sales')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Income")

plt.suptitle('MY SHOP') #This is the heading title above everything else and other titles.
plt.show()

#Scatter

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]) #Comparison Scatter
plt.scatter(x, y, color = 'yellow')

plt.show()

#scatter sizes for markers

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x,y,s=sizes)
plt.show()

#scatter Alpha / Transparency

sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x,y,s = sizes,alpha = 0.5)

plt.show()

#color bar

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

# barchart

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y) #if you want horizontal us barh() , you can add color,change width and height
plt.show()

#Histogram

x = np.random.normal(170, 10, 250) ##this generates random values 

plt.hist(x) ## takes in random values into the histogram
plt.show() 

#pie chart

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

#adding labels

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y,labels = mylabels)
plt.show()

#start angle

plt.pie(y, labels = mylabels, startangle = 90) #starts the pie chart from 90 degrees
plt.show

#wedge pie chart and shadow

myexplode = [0.2, 0, 0, 0]
plt.pie(y,labels = mylabels,explode = myexplode,shadow = True) #wedges one of the pies and creates a shador around it all
plt.show()
#color

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y,labels = mylabels,colors = mycolors)
plt.show()

#you can have a legend

plt.pie(y,labels = mylabels)
plt.legend(title = 'Four Fruits') #you can add a header
plt.show()