from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
root=Tk()
root.title("Notepad")
root.geometry("1200x680")
global open_status_name
open_status_name=False

# function for new file
def new_file():                                  
    my_text.delete("1.0",END)
    root.title("New file- TextPad")
# function for open file
def open_file():
    my_text.delete("1.0",END)
    text_file=filedialog.askopenfilename(initialdir="C:/Users/RAJASHEKAR" ,title="Open File",filetypes=(("Text Files",".txt"),("HTML Files",".html"),("Python Files",".py"),("All Files",".*")))
    if text_file:
        global open_status_name
        open_status_name=text_file
    text_file=open(text_file,"r")
    x=text_file.read()
    my_text.insert(END,x)
    text_file.close()
    
# function to saveas file
def save_file_as():
    text_file=filedialog.asksaveasfilename(defaultextension=".",initialdir="C:/Users/RAJASHEKAR" ,title="Save File",filetypes=(("Text Files",".txt"),("HTML Files",".html"),("Python Files",".py"),("All Files",".")) )
    if(text_file):
        text_file=open(text_file,"w")
        text_file.write(my_text.get(1.0,END))
        text_file.close()
def save_file():
    global open_status_name
    if open_status_name:
        text_file=open(open_status_name,"w")
        text_file.write(my_text.get(1.0,END))
        text_file.close()
    else:
        save_file_as()
#cut text
def cut_text(e):
    global selected
    if my_text.selection_get():
        selected=my_text.selection_get()
        my_text.delete("sel.first","sel.last")
        
        
def paste_text(e):

    if selected:
        position=my_text.index(INSERT)
        my_text.insert(position,selected)
    
def copy_text(e):
    if my_text_selection_get():
        selected=my_text.selection_get()
        
#Bold Text
def bold_it():
    bold_font=font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")
    #Configure a tag
    my_text.tag_configure("bold",font=bold_font)
    current_tags=my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")

        
        
def Italic_it():
    italics_font=font.Font(my_text,my_text.cget("font"))
    italics_font.configure(slant="italic")
    #Configure a tag
    my_text.tag_configure("italic",font=italics_font)
    current_tags=my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic","sel.first","sel.last")
    else:
        my_text.tag_add("italic","sel.first","sel.last")


        
 #change text color
def text_color():
    #pick a color
    my_color=colorchooser.askcolor()[1]
    color_font=font.Font(my_text,my_text.cget("font"))
    #color_font.configure(slant="italic")
    #Configure a tag
    my_text.tag_configure("colored",font=color_font,foreground=my_color)
    current_tags=my_text.tag_names("sel.first")
    if "colored" in current_tags:
        my_text.tag_remove("colored","sel.first","sel.last")
    else:
        my_text.tag_add("colored","sel.first","sel.last")
    

#change background color
def bg_color():
    my_color=colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)
        
#change All text Color
def all_text_color():
    my_color=colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)
    
#add image to notepad
def add_image():
    try:
        # Ask the user to select an image file
        filename = askopenfilename()
        
        # Open the image file and create a Tkinter PhotoImage object
        image = Image.open(filename)
        resized_image=image.resize((300,210),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized_image)
        
        # Insert the PhotoImage object into the text editor
        my_text.image_create(INSERT, image=photo)
        
        # Keep a reference to the PhotoImage object
        my_text.image = photo
    except Exception as e:
        print(f"Error adding image: {e}")







#create toolbar frame        
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)

#create main frame
my_frame=Frame(root)
my_frame.pack(pady=10)
# create scroll bar for text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)


text1_scroll=Scrollbar(my_frame,orient="horizontal")
text1_scroll.pack(side=BOTTOM,fill=X)
#create text box
my_text=Text(my_frame,width=130,height=40,font=("Times New Roman",18),undo=True,selectbackground="blue",wrap="none",xscrollcommand=text1_scroll.set)
my_text.pack()
#configure scroll bar with text
text_scroll.config(command=my_text.yview)
#create menu
my_menu=Menu(root)
root.config(menu=my_menu)
#add file to menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save as",command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="exit",command=root.quit)

#add edit menu
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=lambda :cut_text(False),accelerator="(Ctrl+X)")
edit_menu.add_command(label="copy",command=lambda :copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="paste",command=lambda :paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")



#Color menu
color_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="change selected text",command=text_color)
color_menu.add_command(label="All Text",command=all_text_color)
color_menu.add_command(label="Background",command=bg_color)


#add edit menu
image_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Add Image",menu=image_menu)
image_menu.add_command(label="Add Image from Device",command=add_image)
#image_menu.add_command(label="Add Image from from browser",command=add_image)









# Add a button to the window to allow the user to add an image
#add_image_button = Button(toolbar_frame, text="Add Image", command=add_image)
#add_image_button.grid(row=0,column=3,padx=5)

root.mainloop()