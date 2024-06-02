`last update : 1/6/2024`

So.. *(I use arch btw and)* I wanted to store my open-tabs of this subject somewhere so here we go... *(nothing too formally structured but anyways)*

## Android - Emulator - Setup
- [Have a brief look here](https://wiki.archlinux.org/title/Android)
- `yay -S android-emulator android-sdk-build-tools android-sdk-platform-tools`
- Into `.bashrc` or `.zshrc` add:
```bash
export ANDROID_HOME=/opt/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin/
export PATH="$HOME/.local/bin:$PATH"
```

## apk-tool
- `yay -S android-apktool`
- `apktool d ./app.apk` decompile
- `apktool b ./app` recompile


## sdkmanager
> [!NOTE]  
> You might need to `sudo pacman -S jdk8-openjdk` and temporarly swich to it later *(for `sdkmanager`)* using `sudo archlinux-java set java-8-openjdk`

- `sdkmanager --list`
- `sdkmanager --install "system-images;android-27;default;x86"` if not through aur I guess

## avdmanager + AVD emulator
- `avdmanager create avd --name my_avd27_2 --package "system-images;android-27;default;x86"`
- `emulator -avd my_avd27_2`


## Rooting AVD
- `git clone https://gitlab.com/newbit/rootAVD.git` 
- `cd` and `sh rootAVD.sh /opt/android-sdk/system-images/android-27/default/x86/ramdisk.img`
- [rooting process doesn't start #94](https://github.com/newbit1/rootAVD/issues/94)
- [Stuck at "Searching for pre installed Magisk Apps" due to "No unzip binary found"](https://gitlab.com/newbit/rootAVD/-/issues/105)

## sign an apk 
*(using sign scheme v2)* | Assuming you already decompiled edited and recompiled an apk *(based on the ## Sources and stuff)*... to install it on a device, you have to first sign it like:
- `keytool -genkeypair -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000`
- `apksigner sign --ks my-release-key.keystore --ks-key-alias my-key-alias my-app.apk`
- [source](https://stackoverflow.com/a/40064199/11465149)

## Sources and stuff
> [!NOTE]  
> For some tools *(I don't remember exactly which)*, you might need to ["Increase heap size in Java"](https://stackoverflow.com/questions/1565388/increase-heap-size-in-java) by edditing the entry of the executable\command *(eg. for `/usr/bin/apktool` you'll definately need more than `javaOpts="-Xmx256M"`)*

- ***✨ Highlighted:***
- - [Tutorial: Android Network Traffic Interception](https://github.com/LabCIF-Tutorials/Tutorial-AndroidNetworkInterception?tab=readme-ov-file)
- - [Configuring Burp Suite With Android Nougat](https://blog.ropnop.com/configuring-burp-suite-with-android-nougat)
- - [Manually installing split APK files (App Bundles) via ADB](https://raccoon.onyxbits.de/blog/install-split-apk-adb/)
- ***StackOverflow:***
- - [Android emulator: How to monitor network traffic?](https://stackoverflow.com/questions/2453949/android-emulator-how-to-monitor-network-traffic?answertab=scoredesc#tab-top)
- - [How can I shutdown my Android phone using an adb command?](https://android.stackexchange.com/questions/47989/how-can-i-shutdown-my-android-phone-using-an-adb-command)
- - [Android: adb pull file on desktop](https://stackoverflow.com/questions/17629889/android-adb-pull-file-on-desktop)
- - [How do I get an apk file from an Android device?](https://stackoverflow.com/a/18003462/11465149)
- ***Tools:*** 
- - ***Other:***
- - - ✨ [android-unpinner](https://github.com/mitmproxy/android-unpinner) + [FIX?](https://github.com/mitmproxy/android-unpinner/discussions/26#discussioncomment-9528502)
- - ***Interception:***
- - - [apk-mitm](https://github.com/shroudedcode/apk-mitm/)
- - - `sudo pacman -S mitmproxy`
- - - `yay -S httptoolkit-bin`
- - - [Burp Suite](https://wiki.archlinux.org/title/Burp_Suite)
- - ***Frida:***
- - - [just and interesting issue?](https://github.com/Eltion/Instagram-SSL-Pinning-Bypass/issues/59#issuecomment-2025892004)
- ***Random:***
- - [How to use mitmproxy in android system wide?](https://discourse.mitmproxy.org/t/how-to-use-mitmproxy-in-android-system-wide/1636)
- - [BUG Recompilation error: "invalid value for type 'layout'. Expected a reference"](https://github.com/iBotPeaches/Apktool/issues/2618)
- - [Error parsing XML: not well-formed (invalid token) #1407](https://github.com/iBotPeaches/Apktool/issues/1407)
- - [Difference between signature versions - V1 (Jar Signature) and V2 (Full APK Signature) while generating a signed APK in Android Studio?](https://stackoverflow.com/questions/42648499/difference-between-signature-versions-v1-jar-signature-and-v2-full-apk-sign)
- - https://github.com/HexNio/ssl_pinning_remover
- - [charles](https://www.charlesproxy.com/)

http toolkit
