from tkinter import *
from tkinter import ttk
import requests,json
def get_data():
    city=city_name.get()
    if not city:
        # Handle the case when the city name is empty
        weather1.config(text="Empty input")
        wd1.config(text="")
        temp1.config(text="")
        pres1.config(text="")
    else:
        try:
            data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4cec456a12e78e190dc12413b1d46585').json()
            weather1.config(text=data['weather'][0]['main'])
            wd1.config(text=data['weather'][0]['description'])
            temp1.config(text=int(data['main']['temp'] - 273.15))
            pres1.config(text=data['main']['pressure'])
        except KeyError:
            # Handle the case when the city is not found or data format is unexpected
            weather1.config(text="City not found.")
            wd1.config(text="")
            temp1.config(text="")
            pres1.config(text="")
window=Tk()
window.title('Prepleaf by Masai')
window.config(bg='Light Green') 
window.geometry("700x500")
label_name=Label(window,bg='Sky blue',text='Welcome in Weather App',font=('Time New Roman',30,'bold'))
label_name.place(x=25,y=40,height=40,width=625)
city_name=StringVar()
lst_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
lst = ttk.Combobox(window, textvariable=city_name, 
values=lst_name, font=('Time New Roman', 25, 'bold'))
lst.place(x=25,y=100,height=40,width=450)
left_tab=Label(window,bg='Yellow',text='Select',font=('Time New Roman',
                                          30,'bold'))
left_tab.place(x=500,y=100,height=36,width=148)
weather=Label(window,text='Weather Report',
                   font=('Time New Roman',20))
weather.place(x=30,y=210,height=30,width=200)
weather1=Label(window,text='',
                   font=('Time New Roman',20))
weather1.place(x=250,y=210,height=30,width=200)
wd=Label(window,text='Weather Description',
                   font=('Time New Roman',16))
wd.place(x=30,y=255,height=30,width=200)
wd1=Label(window,text='',
                   font=('Time New Roman',16))
wd1.place(x=250,y=255,height=30,width=200)
temp=Label(window,text='Temperature °C',
                   font=('Time New Roman',20))
temp.place(x=30,y=300,height=30,width=200)
temp1=Label(window,text='',
                   font=('Time New Roman',20))
temp1.place(x=250,y=300,height=30,width=200)
pres=Label(window,text='Pressure',
                   font=('Time New Roman',20))
pres.place(x=30,y=350,height=30,width=200)
pres1=Label(window,text='',
                   font=('Time New Roman',20))
pres1.place(x=250,y=350,height=30,width=200)
hap=Label(window,text='🌤️'+'🌦️'+'⛅'+'Enjoy the weather'+'🌤️'+'🌦️'+'⛅',font=('Time New Roman',20))
hap.place(x=30,y=400,height=30,width=420)
button=Button(window,text='Click',font=('TimeNew Roman',20,'bold'),command=get_data)
button.place(y=150,height=50,width=100,x=200)
window.mainloop()