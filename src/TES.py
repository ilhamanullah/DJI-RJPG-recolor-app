import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cv2

import sys

from thermal_parser_master.thermal_parser import Thermal


# Definisikan warna gradasi
# colors = ['#FFA200', '#FFDF00', '#FBFD01', '#C9E01F', '#98C43B', '#69AA56', '#1E7878', '#0F3E3E', '#000000']
colors = ['#000000', '#1E7878', '#98C43B', '#FBFD01']
# Rentang suhu yang dinormalisasi
temperatures_range = [0, 0.33, 0.67, 1]
# temperatures_range = [1, 0.89, 0.79, 0.66, 0.58, 0.38, 0.27, 0.17, 0]

# Konversi HEX ke RGB
colors_rgb = [mcolors.hex2color(c) for c in colors]

def get_color_from_normalized_temp(normalized_temp):
    # Cari posisi rentang suhu yang sesuai
    for i in range(len(temperatures_range) - 1):
        if temperatures_range[i] <= normalized_temp <= temperatures_range[i + 1]:
            # Interpolasi warna antara dua warna terdekat
            fraction = (normalized_temp - temperatures_range[i]) / (temperatures_range[i + 1] - temperatures_range[i])
            color = (1 - fraction) * np.array(colors_rgb[i]) + fraction * np.array(colors_rgb[i + 1])
            return color
    return np.array(colors_rgb[-1])

def temperature_to_color_image(temperature_array):
    min_temp = np.min(temperature_array)
    max_temp = np.max(temperature_array)
    diff = max_temp - min_temp

    height, width = temperature_array.shape
    color_image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            temp = temperature_array[y, x]
            normalized_temp = (temp - min_temp) / diff  # Normalisasi suhu ke rentang [0, 1]
            color = get_color_from_normalized_temp(normalized_temp)
            color_image[y, x] = (np.array(color) * 255).astype(np.uint8)

    return color_image

def add_text_to_image(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, color=(0, 0, 0), thickness=1):
    cv2.putText(image, text, position, font, font_scale, color, thickness, lineType=cv2.LINE_AA)



thermal = Thermal(dtype = np.float32)
temperature_array = thermal.parse(filepath_image = 'C:/Users/lenovo/Documents/ngoding/magangers/early-coal-detection/experimental/test/01. Foto Thermal/B West T.JPG')

color_image = temperature_to_color_image(temperature_array)

height, width, _ = color_image.shape
# print(f"Image width: {width}")
# print(f"Image height: {height}")

# add_text_to_image(color_image, 'Max Temp: 70C', (10, 50))
add_text_to_image(color_image, 'Min Temp: ' + str(round(np.min(temperature_array),2)) + 'C', (10, height - 40))
add_text_to_image(color_image, 'Max Temp: ' + str(round(np.max(temperature_array),2)) + 'C', (10, height - 10))

# Tampilkan gambar
plt.imshow(color_image)
plt.axis('off')
plt.show()

# Simpan gambar
cv2.imwrite('./temperature_color_image.jpg', cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR))