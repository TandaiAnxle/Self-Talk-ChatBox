import tkinter

def Submit():
    # Get the message from the entry box
    message = EntryChat.get()

    # Create a label to display the message
    # Align the message to the left for this user (change to right for another user)
    user_message = tkinter.Label(Window, text=message, bg="lightblue", anchor="w", padx=10)
    user_message.pack(fill="x", padx=5, pady=2)

    # Clear the Entry field after submitting the message
    EntryChat.delete(0, tkinter.END)

Window = tkinter.Tk()
# Head
Window.title("ChatBox")
Window.geometry("500x500")
Window.iconbitmap("C:/Users/Bertu/Downloads/favicon.ico")

# Body
EntryChat = tkinter.Entry(Window)
EntryChat.pack(padx=10, pady=10, fill="x")

SubmitButton = tkinter.Button(Window, text="Submit", command=Submit)
SubmitButton.pack(pady=5)

Window.mainloop()
