# Weechat-Matrix on TERMUX
`last update : 4/11/2022`

*Considering that you already `pkg install weechat`:*
* `pkg install build-essential` and\\or `cmake` *(NOT SURE if those needed)* 
* `pkg install libolm rust weechat-python-plugin`
* `python -m pip install --upgrade pip setuptools wheel`
* `export RUSTFLAGS=" -C lto=no" && export CARGO_BUILD_TARGET="$(rustc -vV | sed -n 's|host: ||p')" && pip install cryptography` <sup>[source][1]</sup>
* Run the Above commands <sup>[look also here][2]</sup>:
```terminal
git clone https://github.com/poljar/weechat-matrix.git
cd weechat-matrix
pip install --user -r requirements.txt
make install DESTDIR=~/.local/share/weechat PREFIX= 
```
* And you are Done!


In case that you want matrix to auto-load, just move the folder `matrix` and file `matrix.py` under the `~/.local/share/weechat/python/autoload/`.
run inside `weechat` `/python` to check if installed


[1]:https://github.com/termux/termux-packages/issues/9982#issuecomment-1283449362
[2]:https://github.com/poljar/weechat-matrix#other-platforms
