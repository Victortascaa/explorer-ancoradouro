from tkinter import *
import os
import shutil
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def openAFile():

    files = fd.askopenfilename(
        title="Selecione um arquivo",filetypes=[("All files", "*.*")]
    )
    os.startfile(os.path.abspath(files))



def copyAFile():
    copythefile = fd.askopenfilename(
        title="Selecione um arquivo para copiar",filetypes=[("All files", "*.*")]
    )
    dirToPaste = fd.askdirectory(title="Selecione a pasta para colar o arquivo")
    try:
        shutil.copy(copythefile, dirToPaste)
        mb.showinfo(title="Arquivo copiado!",message="O arquivo foi copiado para o destino."
        )
    except:
        mb.showerror(title="Erro!",message="O arquivo não pode ser copiado. Por favor, tente novamente!"
        )


    try:
        shutil.move(folderToMove, des)
        mb.showinfo("Pasta movida!", 'A pasta selecionada foi movida para o local desejado')
    except:
        mb.showerror('Erro!', 'A Pasta não pode ser movida. Certifique-se de que o destino existe')

def listFilesInFolder():
    i = 0

    folder1= fd.askdirectory(title="Selecione a pasta")
    files = os.listdir(os.path.abspath(folder1))
    listFilesWindow = Toplevel(win_root)

    listFilesWindow.title(f'Files in {folder1}')
    listFilesWindow.geometry("300x500+300+200")
    listFilesWindow.resizable(0, 0)
    listFilesWindow.configure(bg="white")

    the_listbox = Listbox(
        listFilesWindow,selectbackground="#F24FBF",font=("Calibri", "10"),background="white"
    )
    the_listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    the_scrollbar = Scrollbar(
        the_listbox,orient=VERTICAL,command=the_listbox.yview
    )
    the_scrollbar.pack(side=RIGHT, fill=Y)

    the_listbox.config(yscrollcommand=the_scrollbar.set)


    while i < len(files):

        the_listbox.insert(END, "[" + str(i + 1) + "] " + files[i])
        i += 1
    the_listbox.insert(END, "")
    the_listbox.insert(END, "Total Files: " + str(len(files)))


if __name__ == "__main__":

    win_root = Tk()
    win_root.title("Ancoradouro")
    win_root.geometry("300x270+650+250")
    win_root.resizable(0, 0)
    win_root.configure(bg="white")

    # cores do app
    header_frame = Frame(win_root, bg="skyblue") #fundo do título
    buttons_frame = Frame(win_root, bg="skyblue") #fundo do app

    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE, fill="both")

    header_label = Label(
        header_frame,text="Explorador de Arquivos",font=("Calibri", "16"),bg="white",fg="black"
    )

    header_label.pack(expand=TRUE, fill="both", pady=12)

    open_button = Button(
        buttons_frame,text="Abrir arquivo",font=("Calibri", "15"),width=20,bg="white",fg="black",relief=GROOVE,
        activebackground="blue",command=openAFile
    )

    copy_button = Button(
        buttons_frame,text="Copiar arquivo",font=("Calibri", "15"),width=20,bg="white",fg="black",
        relief=GROOVE,activebackground="blue",command=copyAFile
    )

    list_button = Button(
        buttons_frame,text="Listar arquivos da pasta",font=("Calibri", "15"),width=20,bg="white",fg="black",relief=GROOVE,
        activebackground="black",command=listFilesInFolder
    )
    fileNameEntered = StringVar()

    open_button.pack(pady=10)
    copy_button.pack(pady=9)
    list_button.pack(pady=10)
    win_root.mainloop()