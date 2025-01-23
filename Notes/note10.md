`Created At: 2025-01-22 08:47:27 AM`

# Intro
This is a *(Linux)* step-by-step *(no-root needed)* tutorial on how to install [LinageOS](https://lineageos.org/) on [Galaxy-S7,](https://www.gsmarena.com/samsung_galaxy_s7-7821.php) using FOSS tools. *(That worked for me)*


# Preperation
Before getting started, you will need to:

- ([repo](https://github.com/Benjamin-Dobell/Heimdall)) `yay -S heimdall`
- [Download LinageOS](https://ivanmeler.github.io/) `.zip` *[<sub><sup>(source)</sup></sub>](https://xdaforums.com/t/lineageos-21-0-android-14-signature-spoofing-ota-updates-for-s7-exynos.4655853/)*
- 📱 Enable developer-options
- 📱 Developer Options > OEM Unlock


# Install TWRP
Once you [downloaded TWRP](https://twrp.me/Devices/Samsung/#:~:text=S7) `.img` file based on:

| Model|Region/Processor|Model Number|
| --- | --- | --- |
| Galaxy S7 (Exynos) | Global/EU | SM-G930F |
| Galaxy S7 (Qualcomm) | China/USA | SM-G9300, SM-G930V (Verizon), etc. |
| Galaxy S7 edge (Exynos) | Global/EU | SM-G935F |
| Galaxy S7 edge (Qualcomm)| China/USA | SM-G9350, SM-G935V, etc. |

*<sub><sup>(WARNING: The table above is mostly CHAT-GPT generated) (See: Settings > About Phone)</sup></sub>*

1. 📱 Connect you phone
2. 📱 Press "power + volume_up + home" until Download-Mode *(Odin-Mode)* appears
3. 📱 Press "volume_up" to continue
4. `heimdall flash --RECOVERY ./Downloads/twrp-XYZ.img --no-reboot` <!-- twrp-3.7.0_9-1-herolte.img  -->
5. Wait until it's *(100%)* done ...
6. **Now finally and most importantly!** press "power + volume_up + home" and imidiatily after the screen get black 📱 Press "Power + volume_down + home". If not TWRP appears you must redo the aobve 1-6 steps because *["The stock ROM will overwrite the custom recovery with the stock recovery..."](https://xdaforums.com/t/how-to-flash-recovery-using-linux-and-heimdall-solved.4238595/#post-84559747)*

# Install LinageOS
Assuming you followed TWRP installation steps and already [downloaded LinageOS](https://ivanmeler.github.io/), "Swipe to Allow Modifications" and select:

1. `Wipe > Format Data > yes`
2. `Wipe > Advanced Wipe`
3. - [x] Dalvik / ART Cache
4. - [x] System
5. - [x] Data
6. - [x] Cache
7. Swipe to Wipe 
8. Navigate back
9. Swipe to Factory Reset
10. `Wipe > Format Data > yes`
11. Home > Reboot > **Recovery**

Now connect phone to PC and move lineageos zip file into the "Internal Storage". If not mounted automatically then select 📱 "Mount > USB Storage". If the phone won't appear automatically in your PC *(like in my case)* you may need to manually `aft-mtp-mount ~/mnt/galaxy_s7`, but if you find your PC's file-manager freezing when you move any file to it, [redo](https://xiaomi.eu/community/threads/twrp-infinite-loop-cant-copy-files-to-phone.54994/) steps from 1-11. If still having the issue *(as in my case)*, just move the file to an external SD and insert it to the phone. Alternatively use adb tools to push the file [...] **finally:**

1. Install > Swipe to Confirm Flash
2. Reboot System
3. Done

<br>

*<sub><sup>(You may find [this video](https://www.youtube.com/watch?v=BoUNYgHR8PM) handy)</sup></sub>*



