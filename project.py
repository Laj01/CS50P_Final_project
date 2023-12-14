import tkinter
import tkintermapview


def main():

    #create window
    window = tkinter.Tk()
    window.geometry(f'{1000}x{700}')
    window.resizable(False, False)
    window.title('CS50 Final Project')

    #create map widget
    map_widget = tkintermapview.TkinterMapView(window, width=1000, height=700, corner_radius=0)
    map_widget.grid(column=0, row=0)
    
    #set tile server
    #map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    #set position
    map_widget.set_position(47.162494, 19.503304)
    map_widget.set_zoom(7)

    #set address
    #country_name = 'Budapest Hungary'
    #map_widget.set_address(country_name)
    #map_widget.set_zoom(7)

    custom_function_1()
    custom_function_2()
    custom_function_3()

    window.mainloop()

def custom_function_1():
    ...

def custom_function_2():
    ...

def custom_function_3():
    ...

if __name__ == '__main__':
    main()