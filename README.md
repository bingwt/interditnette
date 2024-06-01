
# Why?
<img width="790" alt="reason" src="https://github.com/bingwt/interditnette/assets/113308514/4f892bea-dab0-40f4-aed2-06fb2ae8bd83">
<br />
also I don't know
norminette, moulinette, baguette?


---
# Download
## 1. Go to the root directory
```shell
cd ~
```
---
## 2. Clone the repo
```shell
git clone https://github.com/bingwt/interditnette.git
```
---
# Install
## zsh
### 1. Add alias to interditnette script
```shell
echo "alias interditnette=$HOME/interditnette/interditnette.py" >> ~/.zshrc
```
### 2. Source `.zshrc`
```shell
source ~/.zshrc
```
## bash
### 1. Add alias to interditnette script
```shell
echo "alias interditnette=$HOME/interditnette/interditnette.py" >> ~/.bashrc
```
### 2. Source `.zshrc`
```shell
source ~/.bashrc
```
---
# Usage
## Note
To use interditnette, your files must be [norminette friendly](https://github.com/42School/norminette).
<br />
Interditnette takes in any `*.c/*.h/*.permise` files and searches for function definitions. 
## Example
```shell
interditnette ./srcs/*.c ./includes/*.h allowed.permise
```
### `.permise`
```
open, close, read, write,
malloc, free, perror,
strerror, exit
```
The `.permise` file can be populated with any allowed functions to have them be filtered out.
<br />
I.e Just copy them from the allowd functions in the subject pdf.
