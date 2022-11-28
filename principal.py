from tkinter import *
import os
import shutil
from tkinter import messagebox as mb #Mostra as mensagens
from tkinter import filedialog as fd

#Função que abre o arquivo
def openAFile():
    # selecionando um arquivo usando askopenfilename de filedialog como fd
    files = fd.askopenfilename(
        title="Selecione o arquivo",filetypes=[("All files", "*.*")]
    )
    os.startfile(os.path.abspath(files))


# função para copiar um arquivo
def copyAFile():
    # usando o método askopenfilename() do filedialog para selecionar o arquivo
    copythefile = fd.askopenfilename(
        title="Selecione um arquivo para copiar",filetypes=[("All files", "*.*")]
    )
    # use o método askdirectory() do filedialog para selecionar o diretório
    dirToPaste = fd.askdirectory(title="Selecione a pasta para colar o arquivo")
    try:
        shutil.copy(copythefile, dirToPaste)
        mb.showinfo(title="Arquivo copiado!",message="O arquivo foi copiado para o destino."
        )
    except:
        mb.showerror(title="Erro!",message="O arquivo não pode ser copiado. Por favor, tente novamente!"
        )
    submitButton.pack(pady=2)
# definindo uma função que será chamada quando o botão enviar for clicado
def NameSubmit():
        # using the move() method of the shutil module to move the folder to the requested location
        shutil.move(folderToMove, des)
        mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')
#list all files in a folder
def listFilesInFolder():
    i = 0
    # using the askdirectory() method to select the folder
    folder1= fd.askdirectory(title="Select the Folder")
    files = os.listdir(os.path.abspath(folder1))
    listFilesWindow = Toplevel(win_root)
    # specifying the title of the pop-up window
    listFilesWindow.title(f'Files in {folder1}')
    listFilesWindow.geometry("300x500+300+200")
    listFilesWindow.resizable(0, 0)
    listFilesWindow.configure(bg="white")

    # creating a list box
    the_listbox = Listbox(
        listFilesWindow,selectbackground="#F24FBF",font=("Calibri", "10"),background="white"
    )
    the_listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    # creating a scroll bar
    the_scrollbar = Scrollbar(
        the_listbox,orient=VERTICAL,command=the_listbox.yview
    )
    the_scrollbar.pack(side=RIGHT, fill=Y)
    # setting the yscrollcommand parameter of the listbox's config() method
    the_listbox.config(yscrollcommand=the_scrollbar.set)

    # iterating through the files in the folder
    while i < len(files):
        # using the insert() method to insert the file details in the list box
        the_listbox.insert(END, "[" + str(i + 1) + "] " + files[i])
        i += 1
    the_listbox.insert(END, "")
    the_listbox.insert(END, "Total Files: " + str(len(files)))


if __name__ == "__main__":
    # creating an object of the Tk() class
    win_root = Tk()
    win_root.title("Ancoradouro")
    win_root.geometry("280x300+650+250")
    win_root.resizable(0, 0)
    win_root.configure(bg="white")

    # creating the frames using the Frame()
    header_frame = Frame(win_root, bg="#D8E9E6")
    buttons_frame = Frame(win_root, bg="skyblue")

    # using the pack() method to place the frames in the window
    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE, fill="both")

    # creating a label using the Label() widget
    header_label = Label(
        header_frame,text="Explorador de Arquivos",font=("Calibri", "16"),bg="white",fg="blue"
    )

    # using the pack() method to place the label in the window
    header_label.pack(expand=TRUE, fill="both", pady=12)

    # creating open button
    open_button = Button(
        buttons_frame,text="Abrir arquivo",font=("Calibri", "15"),width=20,bg="white",fg="blue",relief=GROOVE,
        activebackground="blue",command=openAFile
    )
    # copy button
    copy_button = Button(
        buttons_frame,text="Copiar arquivo",font=("Calibri", "15"),width=20,bg="white",fg="blue",
        relief=GROOVE,activebackground="blue",command=copyAFile
    )

    # list all files button
    list_button = Button(
        buttons_frame,text="Listar arquivos da pasta",font=("Calibri", "15"),width=20,bg="white",fg="Blue",relief=GROOVE,
        activebackground="Blue",command=listFilesInFolder
    )
    # create an object of Stringvar class
    fileNameEntered = StringVar()

    # use the pack method to place the buttons
    open_button.pack(pady=9)
    copy_button.pack(pady=9)
    list_button.pack(pady=10)
    win_root.mainloop()