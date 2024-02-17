station_names = [
    "Helsinki Harmaja",
    "Helsinki Kaisaniemi",
    "Helsinki Kaivopuisto",
    "Helsinki Kumpula",
    1
]
station_id = [
    1,
    3,
    5,
    3,
    1
]
i=1 
 
for i in range(0, len(station_names)):
    info_text = f"The temperature at {station_names[i]} station (ID: {station_id[i]}) is {3:.2f} degrees Celsius."
    print(info_text)