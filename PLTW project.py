#Imports and a time stopper
from tkinter import  *
import requests
import webbrowser

#Class test

class BoatBuilderGUI:
    
    def __init__(self):
        #Main root variable
        self.root = Tk()
        self.material = IntVar()
        self.type = IntVar()
        self.canvas = Canvas(self.root, height=600, width=600, bg='#FFFFFF')
        self.API_Handler = APIHandler()

        #Creates buttons
        self.wood_radio = Radiobutton(self.root, text='Wood', variable=self.material, value=1, command = self.wood)
        self.iron_radio = Radiobutton(self.root, text='Iron', variable=self.material, value=2, command = self.iron)
        self.steel_radio = Radiobutton(self.root, text= 'Steel', variable=self.material, value=3, command = self.steel)
        self.sailboat_radio = Radiobutton(self.root, text='Sailboat, "Caution may break upon use"', variable=self.type, value=1, command=self.sailboat)
        self.ironclad_radio = Radiobutton(self.root, text='Ironclad, meh', variable=self.type, value=2, command = self.ironclad)
        self.warship_radio = Radiobutton(self.root, text='Warship, "Boat Builder Destroyer"', variable=self.type, value=3, command=self.warship)


        #NEW ADDED FEATURE WITH LEADERBOARD DROP DOWN MENU
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        #Define both of the variables that hold the drop downs for each submenu in the top bar
        self.leaderboardmenu = Menu(self.menu_bar)
        self.sharemenu = Menu(self.menu_bar)

        #Cascade for the leaderboard menu
        self.menu_bar.add_cascade(label="Leaderboard", menu=self.leaderboardmenu)
        self.leaderboardmenu.add_command(label="View Leaderboard", command=self.leaderboard_view_command)
        #Cascade for the Share menu
        self.menu_bar.add_cascade(label="Share Boatbuilder!", menu=self.sharemenu)
        self.sharemenu.add_command(label="View on github")


        #Sets up positions for buttons
        self.wood_radio.grid(row=0, column = 0, sticky=W)
        self.iron_radio.grid(row=0, column = 4, sticky=W)
        self.steel_radio.grid(row=0, column=8, sticky=W)
        self.sailboat_radio.grid(row=1, column=0, sticky=W)
        self.ironclad_radio.grid(row=1, column=4, sticky=W)
        self.warship_radio.grid(row=1, column=8, sticky=W)
        
        self.canvas.grid(row=10,rowspan=999, column = 0, columnspan = 12)
        #creates colors
        self.red_intvar = IntVar()
        self.green_intvar = IntVar()
        self.blue_intvar = IntVar()

        #Don't know why this is here
        self.material.set(1) 
        self.type.set(1)
        #self.root mainloop
        self.root.mainloop()

    def hexstring(self, slider_intvar):
        '''A function to prepare data from controller's widget for view's consumption
        
        slider_intvar is an IntVar between 0 and 255, inclusive
        hexstring() returns a string representing two hexadecimal digits
        '''
        pass

    def sailboat(self):
        self.canvas.delete("all")
        rectangle1 = self.canvas.create_rectangle(100, 100, 200, 200, fill="#850000", outline = "#850000") 
        circle1 = self.canvas.create_oval(100, 140, 500, 500, fill='#850000', outline = "#850000")


    def ironclad(self):
        self.canvas.delete("all")
        rectangle = self.canvas.create_rectangle(200, 50, 100, 150, fill="#ece9ec", outline='#ece9ec')
        circle = self.canvas.create_oval(100, 140, 500, 500, fill="#ece9ec", outline = "#ece9ec")

        
    def warship(self):    
        self.canvas.delete("all")
        rectangle2 = self.canvas.create_rectangle(100, 100, 200, 200, fill='#c3cbad', outline='#c3cbad')
        rectangle3 = self.canvas.create_rectangle(150, 150, 250, 200, fill='#c3cbad', outline='#c3cbad')
        circle2 = self.canvas.create_oval(100, 140, 500, 500, fill='#c3cbad', outline='#c3cbad')

    def wood(self):
        pass

    def steel(self):
        pass
    def iron(self):
        pass

    #Drop down menu functions
    def leaderboard_view_command(self):
        '''Displays the leaderboard from the menu'''
        l = Leaderboard(self.API_Handler.get_leaderboard())

    def share_boat_builder(self):
        webbrowser.open_new_tab("https://github.com/rshowalter/BoatBuilder3.0")
        
        
class APIHandler:
    
    def __init__(self):
        pass
    
    def get_leaderboard(self):
        '''Gets the leaderboard data from the API'''
        try:
            r = requests.get('https://boatbuilder-api-sc1341.c9users.io/leaderboard.json')
            return r.json()
        except:
            return {"status":"api error"}
    
    def post_data_to_leaderboard(self, playername, boattype):
        '''Puts the user data into the leaderboard on the API side, leaderboard data should be a dictionary
        this does use a get request FYI, it is ok that values are put through url in this case'''
        r = requests.get('https://boatbuilder-api-sc1341.c9users.io/leaderboard.php?playername=' + playername + '&boattype=' + boattype)
    
    

class Leaderboard:

    def __init__(self, leaderboarddata):
        self.root = Tk()
        data = leaderboarddata
        height = 3
        width = 2
        for key, value in data.items():
            for i in range(height):
                for j in range(width): #Columns
                    b = Label(self.root, text=key + " " + value)
                    b.grid(row=i, column=j)

        self.root.mainloop()

if __name__ == '__main__':
    gui = BoatBuilderGUI()
