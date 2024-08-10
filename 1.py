from tkinter import *
from tkinter import ttk
import requests, json
import randomcolor

# Generate random colors
random_color_generator = randomcolor.RandomColor()
color1 = random_color_generator.generate()[0]
color2 = random_color_generator.generate()[0]

def create_diagonal_gradient(canvas, width, height, color1, color2):
    gradient = PhotoImage(width=width, height=height)
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    for i in range(width):
        nr = int(r1 + (r2 - r1) * (i / width))
        ng = int(g1 + (g2 - g1) * (i / width))
        nb = int(b1 + (b2 - b1) * (i / width))
        color = "#%04x%04x%04x" % (nr, ng, nb)
        gradient.put(color, to=(i, 0, i+1, height))
    
    return gradient

def get_data():
    city = city_name.get()
    if not city:
        weather1.config(text="Empty input")
        wd1.config(text="")
        temp1.config(text="")
        pres1.config(text="")
    else:
        try:
            data = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4cec456a12e78e190dc12413b1d46585'
            ).json()
            weather1.config(text=data['weather'][0]['main'])
            wd1.config(text=data['weather'][0]['description'])
            temp1.config(text=int(data['main']['temp'] - 273.15))
            pres1.config(text=data['main']['pressure'])
        except KeyError:
            weather1.config(text="City not found.")
            wd1.config(text="")
            temp1.config(text="")
            pres1.config(text="")

window = Tk()
window.title('Weather App')
window.geometry("700x500")
window.resizable(False, False)

# Create a canvas for the gradient background
canvas = Canvas(window, width=700, height=500)
canvas.pack(fill="both", expand=True)

# Create and set the diagonal gradient background
gradient = create_diagonal_gradient(canvas, 700, 500, color1, color2)
canvas.create_image(0, 0, anchor=NW, image=gradient)

# Add widgets
label_name = Label(window, bg='skyblue', text='Welcome to the Weather App', font=('Time New Roman', 30, 'bold'))
label_name.place(x=25, y=40, height=40, width=625)

city_name = StringVar()
lst_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
            "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
            "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
            "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
            "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
            "National Capital Territory of Delhi", "Puducherry"]
lst = ttk.Combobox(window, textvariable=city_name, values=lst_name, font=('Time New Roman', 25, 'bold'))
lst.place(x=25, y=100, height=40, width=450)

left_tab = Label(window, bg='yellow', text='Select', font=('Time New Roman', 30, 'bold'))
left_tab.place(x=500, y=100, height=36, width=148)

weather = Label(window, text='Weather Report', font=('Time New Roman', 20))
weather.place(x=30, y=210, height=30, width=200)

weather1 = Label(window, text='', font=('Time New Roman', 20))
weather1.place(x=250, y=210, height=30, width=200)

wd = Label(window, text='Weather Description', font=('Time New Roman', 16))
wd.place(x=30, y=255, height=30, width=200)

wd1 = Label(window, text='', font=('Time New Roman', 16))
wd1.place(x=250, y=255, height=30, width=200)

temp = Label(window, text='Temperature(°C)', font=('Time New Roman', 20))
temp.place(x=30, y=300, height=30, width=200)

temp1 = Label(window, text='', font=('Time New Roman', 20))
temp1.place(x=250, y=300, height=30, width=200)

pres = Label(window, text='Pressure(mb)', font=('Time New Roman', 20))
pres.place(x=30, y=350, height=30, width=200)

pres1 = Label(window, text='', font=('Time New Roman', 20))
pres1.place(x=250, y=350, height=30, width=200)

hap = Label(window, text='🌤️'+'🌦️'+'⛅'+' Enjoy the weather '+'🌤️'+'🌦️'+'⛅', font=('Time New Roman', 20))
hap.place(x=30, y=400, height=30, width=420)

button = Button(window, text='Click', font=('Time New Roman', 20, 'bold'), command=get_data)
button.place(y=150, height=50, width=100, x=200)

window.mainloop()
