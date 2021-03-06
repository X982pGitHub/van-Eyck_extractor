# van Eyck extractor
A quick way to extract very large image from *Closer to Van Eyck.*

โปรแกรมในการสกัดภาพขนาดใหญ่มาก ๆ อย่างรวดเร็ว จาก *Closer to Van Eyck*

* [How to use - วิธีการใช้](#how-to-use---วิธีการใช้)
* [Installation - การติดตั้ง](#installation---การติดตั้ง)
* [Reporting bugs - รายงานข้อบกพร่อง](#reporting-bugs---รายงานข้อบกพร่อง)
* [Legality - ทางด้านกฎหมาย](#legality---ทางด้านกฎหมาย)
* [Licensing - ลิขสิทธิ์](#licensing---ลิขสิทธิ์)

## How to use - วิธีการใช้
### English
The program has 4 input. Three are required and another one is optional.
***The process to get the information needed REQUIRED web inspection, which may not be avialable on mobile devices.***
 - **URL** — the URL is where the image is located. in *Closer to van Eyck,* the full image is cut into many small image for display. The program will both download the image and compile those to large file. The URL should start with *http://data.closertovaneyck.be/...* **NOT** *http://closertovaneyck.kikirpa.be/...*
   - **How to get the URL**
     - Apple Safari (macOS) 
         1. Zoom to desire resolution (The more you zoom, the higher resolution image cell becomes) and move to the painting bottom-most right edge.
         2. Press ***⌥ Option + ⌘ + C*** to open web inspector
         3. Select *Sources* tab.
     - Google Chrome (Desktop)
         1. Zoom to desire resolution (The more you zoom, the higher resolution image cell becomes) and move to the painting bottom-most right edge.
         2. Press ***⇧ Shift + Ctrl + J*** (Windows) or ***⌥ Option + ⌘ + J*** (macOS) to open web inspector
         3. Select *Sources* tab.
     - Mozilla Firefox (Desktop)
         1. Zoom to desire resolution (The more you zoom, the higher resolution image cell becomes) and move to the painting bottom-most right edge.
         2. Press ***⇧ Shift + Ctrl + J*** (Windows) or ***⇧ Shift + ⌘ + J*** (macOS) to open web inspector
     - Microsoft Edge (Windows)
         1. Zoom to desire resolution (The more you zoom, the higher resolution image cell becomes) and move to the painting bottom-most right edge.
         2. Press ***Ctrl + ⇧ Shift + I*** to open web inspector
         3. Select *Sources* tab. If it cannot be found. You may need to press **≫** (more tabs) first. Then a drop down would list *Sources* tab.
  - **URL format**
    - Example: http://data.closertovaneyck.be/verona/tiles/26-VIS-UH/13/12_17.jpg
      - Image: 
        
        ![Arnolfini Portrait bottom-most right edge](http://data.closertovaneyck.be/verona/tiles/26-VIS-UH/13/12_17.jpg)
        - Image size: This image is 256 pixels high and 148 pixels wide. This cell is clipped since it's on the edge. Normal image cell is a square of 256 pixels on each side. 
        - Image name: **12_17.jpg** The name is format in ***(x dimension)***_***(y dimension)***.jpg The number is not in pixels but in the amount of image cell.
      - Domain: It **MUST** be *data.closertovaneyck.be/* which is the image database. **NOT** *closertovaneyck.kikirpa.be/*
      - Sub-folders:
        - First and second sub-folder is usually ***verona/tiles/***
        - Third sub-folder is the i.d. of the painting. In this case ***26-VIS-UH/*** but it would be different on different painting.
        - Fourth sub-folder is the amount of zoom (resolution) of the image.  In this case ***13/*** Higher the number, higher the resolution. But changing the resolution would shift the relative location of the image cell to the real painting. **NOTE:** This number doesn't increase the size of the cell. The cell size is constant at 256 pixels. But each cell will be *closer* to the painting. So it required more cell to fill the whole painting. Hence the higher resolution. The resolutio is not limited and must be found by afforemention process. Changing the resolution, one must find new *x and y dimension* since it will have moved.
      - How to use this URL:
        - Copy all of the URL **EXCEPT** the image name onto the URL input. In this case ***http://data.closertovaneyck.be/verona/tiles/26-VIS-UH/13/*** should be inputted.
        - Input the *x dimension* from the image name to **Image width** and *y dimension* from the image name to **Image height**
       
 - **Image width** — the width of the image. **NOT** the size in pixel. But the amount of the image cell. To convert to pixel, simply multiply by 256.
 - **Image height** — the height of the image. **NOT** the size in pixel. But the amount of the image cell. To convert to pixel, simply multiply by 256.
 - **Result name** *(optional)* — enter *Result name* to name the result. Otherwise it would be named *"result.jpg"*
## Installation - การติดตั้ง
 The installation are blessfully truly simple. There're two  method with it own limitation.
  - **On computer** 
    1. Just clone the repo to your PC. It's **required** python IDE on your computer, you may want to download it [here!](https://www.jetbrains.com/pycharm/download/)
    2. Put your files on desired directory. It works everywhere.
    
    **Limitation** - This process cannot be follow in mobile device. You may try to implement the code at yours own risk.
  - **Online IDE**
    1. Copy the python code as raw text
    2. Paste it on your online IDE of choice. I would recommend [Replit](https://replit.com/)
    3. Create two folder in the IDE. Name it exactly:
       - Cell
       - Vertical
    4. It should work now. Many online interpreter doesn't support file saving so you may need to switch if error repeatedly occured. If you believe it's a bug, go and read [Reporting bugs](#reporting-bugs---รายงานข้อบกพร่อง). Follows the steps there.
    
    **Limitation** - This process doesn't work on many interpreter. Even it *Replit,* maximum memory is 400Mb, which meant you may not be able to compile very large image.
## Reporting bugs - รายงานข้อบกพร่อง
 If you believe you had encounter a bug. First, please read the [How to use](#How-to-use---วิธีการใช้) first. Mark sure you follow the step. If the bug still persist. Please contact me at thee.thitut@gmail.com with following information:
 1. Title the email "Attention: bug found on van Eyck extractor"
 2. Write the exact step you use to recreate the bug. If it cannot be repeat then I may not be able to help you.
 3. Write the error code given by the ternimal at the end of the email.
 4. Do not sign the email.
 5. Do not format the email/clear all formatting on the email.

***The steps must be followed rigourously. Otherwise you would be ignored.***
## Legality - ทางด้านกฎหมาย
The result given by the program is a faithful photographic reproduction of a two-dimensional, public domain work of art. The work of art itself is in the public domain because the author's life plus 100 years or fewer. This work is in the public domain in the United States because it was published (or registered with the U.S. Copyright Office) before January 1, 1926. This photographic reproduction is therefore also considered to be in the public domain in the United States. In other jurisdictions, re-use of this content may be restricted

According to http://closertovaneyck.kikirpa.be/ (paraphased): 

> the image on this website (which is extracted and is a result of the program) may be used freely by anyone for research and educational purposes, as long as the website Closer to Van Eyck is clearly cited as their source. For any such use, please include the URL, or web address, of the original site (closertovaneyck.kikirpa.be)

> These image may **not** be use for any **for-profit activities**, such as commercial publications or advertisements. If you wish to order any of the images for a scholarly publication, please email info@artinflanders.be
## Licensing - ลิขสิทธิ์
The program is distributed under the GNU General Public License v3.0

You are free for:
- Commercial use — The licensed material and derivatives may be used for commercial purposes.
- Modification — The licensed material may be modified.
- Distribution — The licensed material may be distributed.
- Patent use — This license provides an express grant of patent rights from contributors.
- Private use — The licensed material may be used and modified in private.

The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:
- License and copyright notice — A copy of the license and copyright notice must be included with the licensed material.
- State changes — Changes made to the licensed material must be documented.
- Disclose source — Source code must be made available when the licensed material is distributed.
- Same license — Modifications must be released under the same license when distributing the licensed material. In some cases a similar or related license may be used.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Limitation:
 - This license includes a limitation of liability.
 - This license explicitly states that it does **NOT** provide any warranty.
