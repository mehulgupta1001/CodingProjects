import tkinter as tk
import requests
import datetime

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    total_recovered = str(json_data['recovered'])
    total_active = str(json_data['active'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text = "Total cases: "+total_cases+
        "\n"+"Total deaths: "+total_deaths+
        "\n"+"Total recovered: "+total_recovered+
        "\n"+"Total active: "+total_active+
        "\n"+"Today cases: "+today_cases+
        "\n"+"Today deaths: "+today_deaths+
        "\n"+"Today recovered: "+today_recovered)

    label2.config(text = date)
canvas = tk.Tk()
canvas.geometry('400x400')
canvas.title('Coronavirus Checker')

f = ("poppins", 15, "bold")

button = tk.Button(canvas, font = f, text = "Load", command = getCovidData)
button.pack(pady = 20)

label = tk.Label(canvas, font = f)
label.pack(pady = 20)

label2 = tk.Label(canvas, font = 8)
label2.pack()
getCovidData()
canvas.mainloop()