import time

import cv2
from PIL import  ImageGrab
import os
# os.system("Rundll32.exe CameraDll.dll, CameraSubArea")  #QQ截图dll
# os.system("Rundll32.exe PrScrn.dll, PrScrn")  #微信截图dll
# screenshot=ImageGrab.grab(bbox=(12,12,120,120))
# screenshot.show()

import pyautogui
from PIL import ImageGrab
import tkinter as tk

import win32clipboard
from io import BytesIO
from PIL import Image
import win32con

def get_file_from_clipboard():
    try:
        win32clipboard.OpenClipboard()
        # # Check if the clipboard contains file data
        # if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
        #     file_list = win32clipboard.GetClipboardData(win32con.CF_HDROP)
        #     return file_list

        # Check if the clipboard contains image data
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_DIB):
            image_data = win32clipboard.GetClipboardData(win32con.CF_DIB)
            image = Image.open(BytesIO(image_data))
            print("get")
            return image

        else:
            return  None
            # print("Clipboard does not contain image data.")
    except TypeError:
        print("none")
    finally:
        win32clipboard.CloseClipboard()
# Example usage
def monitor_change():
    previous_image=get_file_from_clipboard()
    while True:
        current_image=get_file_from_clipboard()
        if current_image != previous_image:
            print("get image")

            previous_image=current_image
        time.sleep(1)
if __name__ == '__main__':
    monitor_change()

