import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import math
import sys
import random
from point import Point
from space import Space

unit = "m"

systemlocation = Point(0,0,0)
loitersafearea = Space(Point(0,6,5), 4)

def plotspace(plot, point, r):
    xnought = point[0]
    ynought = point[1]
    xvals = [x/10 for x in range( (xnought - r) * 10, (xnought + r) * 10 + 1 )]
    yvalspos = [ynought + math.sqrt(r**2 - (x/10 - xnought)**2) for x in range( (xnought - r) * 10, (xnought + r) * 10 + 1 )]
    yvalsneg = [ynought - math.sqrt(r**2 - (x/10 - xnought)**2) for x in range( (xnought - r) * 10, (xnought + r) * 10 + 1 )]
    plot.plot(xvals, yvalspos, "b-")
    plot.plot(xvals, yvalsneg, "b-")

def parameterize(pointa, pointb, length):
    coordsa = [pointa.x, pointa.y, pointa.z]
    coordsb = [pointb.x, pointb.y, pointb.z]
    xcoords = []
    ycoords = []
    zcoords = []
    parameterization = [xcoords, ycoords, zcoords]
    for i in range(int(length * 100) + 1):
        t = i/100
        for w in range(len(parameterization)):
            parameterization[w].append(t*coordsb[w] + (1-t)*coordsa[w])
    return parameterization

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Position Visualization Application")
        self.root.geometry("1200x700")
        self.root.configure(bg="white")

        self.fig, (ax1, ax2) = plt.subplots(1, 2)
        self.subplots = [ax1, ax2]
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.sideimg = plt.imread("images/side.png")
        self.backimg = plt.imread("images/back.png")
        self.subplots[0].imshow(self.sideimg, extent=[-10, 10, -10, 10], aspect="auto", zorder=-1)
        self.subplots[1].imshow(self.backimg, extent=[-10, 10, -10, 10], aspect="auto", zorder=-1)

        for subplot in self.subplots:
            subplot.set_xlim(-10, 10)
            subplot.set_ylim(-10, 10)
            subplot.xaxis.set_major_locator(ticker.MultipleLocator(base=5))
            subplot.xaxis.set_major_formatter(FormatStrFormatter("%d {}".format(unit)))
            subplot.yaxis.set_major_locator(ticker.MultipleLocator(base=5))
            subplot.yaxis.set_major_formatter(FormatStrFormatter("%d {}".format(unit)))
            subplot.grid()
        plotspace(self.subplots[0], [loitersafearea.y, loitersafearea.z], loitersafearea.r)
        plotspace(self.subplots[1], [loitersafearea.x, loitersafearea.z], loitersafearea.r)
        
        self.sideviewpoint, = self.subplots[0].plot(systemlocation.y, systemlocation.z, "ko", markersize=10)
        self.backviewpoint, = self.subplots[1].plot(systemlocation.y, systemlocation.z, "ko", markersize=10)

        directionalvector = parameterize(systemlocation, loitersafearea.p, 0.5)
        if not loitersafearea.contains(systemlocation):
            self.sidedirectionalvector, = self.subplots[0].plot(directionalvector[1], directionalvector[2], color="black", linestyle="dashed")
            self.backdirectionalvector, = self.subplots[1].plot(directionalvector[0], directionalvector[2], color="black", linestyle="dashed")
        else:
            self.sidedirectionalvector, = self.subplots[0].plot([0]*len(directionalvector[0]), [0]*len(directionalvector[0]), color="black", linestyle="dashed")
            self.backdirectionalvector, = self.subplots[1].plot([0]*len(directionalvector[0]), [0]*len(directionalvector[0]), color="black", linestyle="dashed")

        self.animation = animation.FuncAnimation(self.fig, self.update, interval=200, blit=False, save_count=100)
        self.loadimage()
        self.root.protocol("WM_DELETE_WINDOW", self.terminate)

    def update(self, frame):
        if loitersafearea.contains(systemlocation):
            self.fig.suptitle("Loiter OK", fontsize=16)
        else:
            dist = round(systemlocation.distancefrom(loitersafearea.p) - loitersafearea.r, 2)
            self.fig.suptitle("System {}{} from Safe Area".format(dist, unit), fontsize=16)

        systemlocation.adjustpoint(random.randint(-2,2)/10, random.randint(-2,2)/10, random.randint(-2,2)/10)
        self.sideviewpoint.set_data([systemlocation.y], [systemlocation.z])
        self.backviewpoint.set_data([systemlocation.x], [systemlocation.z])

        tempdirectionalvector = parameterize(systemlocation, loitersafearea.p, 0.5)
        if not loitersafearea.contains(systemlocation):
            self.sidedirectionalvector.set_data(tempdirectionalvector[1], tempdirectionalvector[2])
            self.backdirectionalvector.set_data(tempdirectionalvector[0], tempdirectionalvector[2])
        else:
            self.sidedirectionalvector.set_data([0]*len(tempdirectionalvector[0]), [0]*len(tempdirectionalvector[0]))
            self.backdirectionalvector.set_data([0]*len(tempdirectionalvector[0]), [0]*len(tempdirectionalvector[0]))

        self.canvas.draw()
        return self.sideviewpoint, self.backviewpoint
    
    def loadimage(self):
        image = Image.open("images/usas.png")
        image = image.resize((400, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.root, image=photo)
        self.label.image = photo
        self.label = tk.Label(self.root, image=photo, bg="white")
        self.label.pack(side=tk.BOTTOM, fill=tk.X)

    def terminate(self):
        if self.animation.event_source is not None:
            self.animation.event_source.stop()
        self.root.quit()
        self.root.destroy()
        sys.exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()