# ⚠️UPDATE - 22-6-2022

> **The old method** of specifying images based on the theme, by using a fragment appended to the URL (#gh-dark-mode-only or #gh-light-mode-only), **is deprecated and will be removed ...**  [[SOURCE]](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#specifying-the-theme-an-image-is-shown-to)

# ✨ NEW METHOD
<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w2.png">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b2.png">
      <img alt="Shows a black logo in light color mode and a white one in dark color mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
    </picture>
</p>

```html
<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/w2.png">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/GiorgosXou/Random-stuff/main/Programming/StackOverflow/Answers/70200610_11465149/b2.png">
      <img alt="Shows a black logo in light color mode and a white one in dark color mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
    </picture>
</p>
```


# ⚠️ OLD METHOD
<p align="center">
    <img src="./b2.png#gh-light-mode-only" height="300" width="1080"/>
    <img src="./w2.png#gh-dark-mode-only" height="300" width="1080"/>
</p>

```html
<p align="center">
    <img src="./b2.png#gh-light-mode-only" height="300" width="1080"/>
    <img src="./w2.png#gh-dark-mode-only" height="300" width="1080"/>
  </a>
</p>
```

| Test with GitHub iamge-links|
|:---:|
|![GitHub-Mark-Light](./b.png#gh-light-mode-only)![GitHub-Mark-Dark ](./w.png#gh-dark-mode-only)|
```
![GitHub-Mark-Light](./b.png#gh-light-mode-only)
![GitHub-Mark-Dark ](./w.png#gh-dark-mode-only)
```

| Test with non-GitHub iamge-links|
|:---:|
|![GitHub-Mark-Light](https://i.stack.imgur.com/IF6pt.png#gh-light-mode-only)![GitHub-Mark-Dark](https://i.stack.imgur.com/t2bMr.png#gh-dark-mode-only)|

```
![GitHub-Mark-Light](https://i.stack.imgur.com/IF6pt.png#gh-light-mode-only)
![GitHub-Mark-Dark](https://i.stack.imgur.com/t2bMr.png#gh-dark-mode-only)
```
