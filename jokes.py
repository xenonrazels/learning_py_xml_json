from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json

class ProgramGUI:
    def __init__(self,master):
        master.title("Jokes Catalogue")
        # master.resizeable(False, False)
        
        try:
            f=open('data.txt','r')
            self.data = json.load(f)#json command to load json from data.txt
            
        except:
            messagebox.showerror(title="Error", message="Missing/invalid file")
            master.destroy()
            return
        
        self.frame_jokes = ttk.Frame(master,width=900,height=500)
        
        self.frame_jokes.pack()
        
        self.current_jokes=0
        # ttk.Label(self.frame_jokes, text=self.data[self.current_jokes].__getitem__("setup"), justify="center",font=('times-new-roman',10,'normal')).grid(row=0,column=0)
        # ttk.Label(self.frame_jokes,text=self.data[self.current_jokes].__getitem__("punchline"),justify="center",font=('times-new-roman',10,'italic')).grid(row=1,column=0)     
        self.show_jokes()


        self.button_frame = ttk.Frame(master,width=800,height=900)
        self.button_frame.pack()
        ttk.Button(self.button_frame, text="Laugh", command=lambda: self.rate_jokes('laugh')).grid(row=0, column=0)
        ttk.Button(self.button_frame, text="Groans",command=lambda: self.rate_jokes('groans')).grid(row=0, column=1)
        

        
    def show_jokes(self):
        self.punchline = ttk.Label(self.frame_jokes, text="", justify="center", font=('times-new-roman', 10, 'normal'))
        self.punchline.grid(row=0,column=0)
        self.punchline.config(text=self.data[self.current_jokes].__getitem__("setup"))
        

        ttk.Label(self.frame_jokes, text=self.data[self.current_jokes].__getitem__("punchline"), justify="center", font=('times-new-roman', 10, 'italic')).grid(row=2,column=0)
        
        
    def rate_jokes(self, ratings):
        if ratings == 'laugh':
           self.data[self.current_jokes].__setitem__("laugh", self.data[self.current_jokes].__getitem__("laugh") + 1)
        elif ratings == 'groans':
            self.data[self.current_jokes].__setitem__("groans", self.data[self.current_jokes].__getitem__("groans") + 1)
        f = open("data.txt", 'w')
        jsonstr = json.dumps(self.data)
        f.write(jsonstr)
        f.close()
        

        if self.current_jokes<len(self.data)-1:
            messagebox.showinfo(title="Ratings Recorded", message="Thank you for rating.\nThe next joke wil now appear")
            self.current_jokes+=1
            self.show_jokes()
            
        elif self.current_jokes == len(self.data) - 1:
            print(self.data)
            messagebox.showinfo(title="Ratings Recorded", message="Thank you for recording.\nThat was last joke.\n The program will now end.  ")
        
        
def main():
    root = Tk()
    gui = ProgramGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
    
