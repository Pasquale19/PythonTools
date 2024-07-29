
def hideOnClick(fig,ax):
    legend=ax.get_legend()
    lines=ax.lines[:]
    leglines=legend.get_lines()
    graphs={}
    for count,l in enumerate(leglines):
        l.set_picker(True)
        l.set_pickradius(5)
        line=next((x for x in lines if x._label == l._label),None)
        graphs[l]=line
    
    patches=ax.patches[:]
    legPatches=legend.get_patches()
    artists={}
    for count,l in enumerate(legPatches):
        l.set_picker(True)
        print(f"patchname={l._label}")
        artist=next((x for x in patches if x._label == l._label),None)
        artists[l]=artist    
        
    graphs=artists|graphs    
    def on_pick(event):
        legline = event.artist
        graph=graphs[legline]
        if graph=='none':
            graph=artists[legline]
        vis = not graph.get_visible()
        graph.set_visible(vis)
        legline.set_alpha(1.0 if vis else 0.2)
        fig.canvas.draw()
        
    fig.canvas.mpl_connect('pick_event', on_pick)