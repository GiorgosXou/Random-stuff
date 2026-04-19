`Created At: 2026-04-05 01:20:16 AM`


# Intro

A way of building and installing Ncurses without breaking your system thanks to chat-GPT :P


# Installation

*(If you want you can download any other specific version of Ncurses source-code from [here](https://invisible-island.net/archives/ncurses))*

1. Ensure those packages are installed
```
sudo pacman -S base-devel wget
```


2. Download&Extract Ncurses
```
wget https://invisible-island.net/archives/ncurses/current/ncurses.tar.gz
tar -xzf ncurses.tar.gz
cd ncurses-*
```

3. Pick a directory you can delete later
```
mkdir -p $HOME/opt/ncurses-test
```


4. Configure Ncurses
```
./configure --prefix=$HOME/opt/ncurses-test \
            --with-shared \
            --with-termlib \
            --enable-widec
```

5. Build & Install
```
make -j$(nproc)
make install
```

> [!TIP]
> For `clangd`-autocomplete in Neovim, Build & Install with:
> ```
> bear -- make -j$(nproc)
> bear --append -- make install
> ```


# Usage

You may simply temporarily set evn-variables to:
```
export LD_LIBRARY_PATH=$HOME/opt/ncurses-test/lib:$LD_LIBRARY_PATH
export PATH=$HOME/opt/ncurses-test/bin:$PATH
export PKG_CONFIG_PATH=$HOME/opt/ncurses-test/lib/pkgconfig:$PKG_CONFIG_PATH
```

and then simply run any app you want to test. If you want to build your app  with it, you may do something like:

```
PKG_CONFIG_PATH=$HOME/opt/ncurses-test/lib/pkgconfig \
LD_LIBRARY_PATH=$HOME/opt/ncurses-test/lib \
gcc ncurses_mouse.c -o ncm.o $(pkg-config --cflags --libs ncursesw)

```
