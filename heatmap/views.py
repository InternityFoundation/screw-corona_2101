from django.shortcuts import render

#dataset
p = [210847,
     140633,
     202922,
     382841,
     440335
     ]

n1 = [5,
      12,
      9,
      18,
      5
    ]

n2 = [0,
      0,
      0,
      3,
      3
    ]

n3 = [1,
      3,
      3,
      3,
      2
    ]

def givecolor(n1,n2,n3,p):
    val = ((n1*1.5+n2*2.6+n3*3.6)/p)*100
    if val >=0.02:
        return "#ff0000"
    elif val>=0.01 and val<0.02:
        return "#ffa500"
    elif val>0 and val<0.01:
        return "#0000ff"

def index(request):
    context = {"color_"+str(chr(x+65)):givecolor(n1[x], n2[x], n3[x], p[x]) for x in range(len(p))}
    return render(request, 'heatmap/index.html', context)
