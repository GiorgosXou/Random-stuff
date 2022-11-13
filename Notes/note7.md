`last update : 13/11/2022`
# ⚠️ ACTUALLY I WAS WRONG LOL, IT DOESN'T WORK AS I EXPECTED IT⚠️

# Intro
This is a step-by-step way on how to manually build and\or install lua-language-server for use through mason.nvim


# Build
*Don't get scared if it fails in the last test*

* `pkg install gcc`
* and jsut follow the [build instractions](https://github.com/sumneko/lua-language-server/wiki/Getting-Started#build)


# Install
If you are looking to install it for use within NVIM through mason.nvim and:

--------------------------------------------------------------------
 you have `pkg install lua-language-server` follow those steps:
 * `ln -s /usr/local/share/lua-language-server/bin/lua-language-server ~/.local/share/nvim/mason/bin/lua-language-server`
 * `sudo -E chmod -R 777 /usr/local/share/lua-language-server/` *( just in case? )*
 * `mkdir .local/share/nvim/mason/packages/lua-language-server`
 * and you are done

--------------------------------------------------------------------
 you have build the source-code, then follow these steps:
* `nvim ~/.local/share/nvim/mason/bin/lua-language-server`:
```sh
#!/usr/bin/env bash
exec "~/Desktop/xou/programming/lua-language-server/bin/lua-language-server" "$@"
```
* `sudo -E chmod 777 .local/share/nvim/mason/bin/lua-language-server` *( just in case )*
* `mkdir .local/share/nvim/mason/packages/lua-language-server`
* and you are done, that does the trick.


# References
* https://github.com/sumneko/lua-language-server/issues/128#issuecomment-1312598616
