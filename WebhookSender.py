import tkinter as tk
import requests
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 60,  relief = 'raised')
canvas1.place(relheight=.5)
canvas1.pack()

label1 = tk.Label(root, text='Send discord Webhooks')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)




label2 = tk.Label(root, text='Enter your Webhook address')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry2)

label3 = tk.Label(root, text='Enter your Webhook content')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label3)


entry3 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry3)

label4 = tk.Label(root, text='Enter your Webhook name')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label4)

entry4 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry4)

label5 = tk.Label(root, text='Enter your Webhook Avatar URL (optional: will be the default new account icon if left blank)')
label5.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label5)


def sendWebhook ():
    
    url = entry1.get()
    content=entry2.get()
    name=entry3.get()
    avatar_url=entry4.get()
    data = {
    "content" : content,
    "username" : name,
    "avatar_url": avatar_url
    }
    
    result = requests.post(url, json = data)

    
button1 = tk.Button(text='Send Webhook', command=sendWebhook, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

label1.pack()
label2.pack()
entry1.pack()
label3.pack()
entry2.pack()
label4.pack()
entry3.pack()
label5.pack()
entry4.pack()

button1.pack()
root.mainloop()