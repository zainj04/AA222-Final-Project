import pandas as pd
import seaborn as sns
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

#Create the pitch
pitch = Pitch(pitch_color='grass', axis=True, label=True, line_color='white', stripe=True, tick=True)
fig, ax = pitch.draw()

x = [5,20,20,20,20,65,65,65,65,90,90]
y = [40,10,30,50,70,10,30,50,70,30,50]

ax.scatter(x,y, c = 'red')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.invert_yaxis()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()