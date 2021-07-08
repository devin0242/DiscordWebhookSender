import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from tkinter import filedialog
import time
import discord
root=tk.Tk()
root.title("Discord Webhook Sender")
root.config(width=1000, height=500)

root.resizable(False,False)




def error_popup_window(error=None):
    window = tk.Toplevel()

    label = tk.Label(window, text=f"There was an error!: {error}")
    label.grid(row=0, column=0)

def previewImage():
    global img
    try:
        
        img_url = pfpEntry.get()
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        window=tk.Toplevel()
        panel = tk.Label(window, image=img)
        
        panel.grid(row=1, column=0)
        label=tk.Label(window,text="------Webhook Avatar Image Preview------").grid(row=0, column=0)
    except Exception as E:
        error_popup_window(E)


#title
title=tk.Label(text="Send Discord Webhooks")
title.config(font=("helvetica",15))
title.grid(row=0, column=0)


#webhook name stuff
#webhook name LABEL
name_column_default=0
input_name_label=tk.Label(text="Input the name of the webhook you want to send.")
input_name_label.grid(row=1, column=name_column_default,padx=25)
#webhook name input
hookNAME_entry=tk.Entry(root)
hookNAME_entry.grid(row=2,column=name_column_default)

#webhook content stuff
#webhook content LABEL
content_column_default=name_column_default+1
input_hookcontent_label=tk.Label(text="Input the message content of the webhook you want to send.")
input_hookcontent_label.grid(row=1, column=content_column_default,padx=25)
#content input box
content_entry=tk.Text(root, height=5, width=50)
content_entry.grid(row=2,column=content_column_default,rowspan=2)

#webhook link stuff
#webhook link LABEL
link_column_default=content_column_default+1
input_hookURL_label=tk.Label(text="Input the WebHook URL")
input_hookURL_label.grid(row=1, column=link_column_default)

#webhook input box
hookUrl_entry=tk.Entry(root,width=60)
hookUrl_entry.grid(row=2,column=link_column_default,padx=25)

#profile picture stuff

#image url input box LABEL
img_column_default=link_column_default+1
input_img_url_label=tk.Label(text="Input the Image you would like to use as the webhook's profile picture.")
input_img_url_label.grid(row=1, column=img_column_default,padx=25)
#image url input box
pfpEntry=tk.Entry(root)
pfpEntry.grid(row=2,column=img_column_default)
#preview image button
img_url_confirm_button=tk.Button(text="Preview your image",command=previewImage)
img_url_confirm_button.grid(row=3, column=img_column_default,pady=9)

#sending the webhook
def sendWebhook ():
    try:
        url = hookUrl_entry.get()
        content=content_entry.get('1.0', 'end-1c')
        name=hookNAME_entry.get()
        avatar_url=pfpEntry.get()
        data = {
        "content" : content,
        "username" : name,
        "avatar_url": avatar_url
        }

        result = requests.post(url, json = data)
        
        window = tk.Toplevel()

        label = tk.Label(window, text=f"WebHook Sent Successfully!!")
        label.grid(row=0, column=0)
    except Exception as E:
        error_popup_window(E)
#send webhook 
send_webhook_column_default=img_column_default-1

#send webhook button
sendWebhook_button=tk.Button(text="Send the Webhook",command=sendWebhook,bg='pale green',height=4,width=40, activebackground="forest green")
sendWebhook_button.grid(row=4, column=send_webhook_column_default,pady=10,rowspan=2,columnspan=3)


import json




s2jLABEL=tk.Label(text="Save the settings in the boxes above to a json file.").grid(row=4, column=0)
def sendWebhookFromJSONdata(content,name, avatar_url,url):
    try:
        data={"content" : content,
        "username" : name,
        "avatar_url": avatar_url
        }
        
        result = requests.post(url, json = data)
        #print(data,url)
        #print(result)


    except Exception as E:
        error_popup_window(E)
def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

def showSettingsFromJSON():
    try:
        clear_frame()
        filename = filedialog.askopenfilename(title="Select A JSON file", filetypes=(("json files", "*.json"),("All Files","*.*")))
        with open(filename, "r") as f:
            settings=json.load(f)
        name=settings["username"]
        url=settings["webhook_url"]
        avatar_url=settings["avatar_url"]
        label=tk.Label(root, text=f"Username: {name}\nWebhook URL: {url}\nAvatar URL: {avatar_url}").grid(row=0, column=0)
        divider=tk.Label(root,text="----------------------------------------").grid(row=1, column=0)
    
        msg_content_box_label=tk.Label(root,text="Input the message content you want to send in the webhook.").grid(row=2, column=0)
        msg_content_box=tk.Text(root,height=5, width=100)
        msg_content_box.grid(row=3, column=0)
        webhookSendBTN=tk.Button(root,text=f"Send Webhook with data from {filename}",bg='pale green',height=4,padx=10, activebackground="forest green", command=lambda: sendWebhookFromJSONdata(msg_content_box.get('1.0', 'end-1c'),name,avatar_url,url))
        webhookSendBTN.grid(row=4, column=0,pady=9)
    except Exception as E:
        error_popup_window(E)
def file_save():
    file=filedialog.asksaveasfile(defaultextension=".json")
    file=file.name
    print(file)
    url = hookUrl_entry.get()
    name=hookNAME_entry.get()
    avatar_url=pfpEntry.get()
    data = {
    "username" : name,
    "avatar_url": avatar_url,
    "webhook_url": url
    }
    with open(file, "w") as f:    
        json.dump(data,f)
save2json=tk.Button(text="Save Settings as JSON",command=file_save).grid(row=5, column=0)
lfJSONlabel=tk.Label(text="Load data from JSON file.").grid(row=4, column=1)
loadfromjson=tk.Button(text="load from json",command=showSettingsFromJSON)
loadfromjson.grid(row=5, column=1)


root.mainloop()
