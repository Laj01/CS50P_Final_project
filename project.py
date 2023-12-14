import tkinter
import tkintermapview


def main():

    #create window
    window = tkinter.Tk()
    window.geometry(f'{1000}x{700}')
    window.title('CS50 Final Project')

    #create map widget
    map_widget = tkintermapview.TkinterMapView(window, width=1000, height=700, corner_radius=0)
    map_widget.grid(column=0, row=0)
    

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