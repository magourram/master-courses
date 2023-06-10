# Markdown:

`pip install smdv`

`pip install pandoc`

`sudo apt-get install xdg-utils

`sudo npm -g install instant-markdown-d`



# Coc:

`yarn install` on ~/.vim/plugged/coc.nvim

`sudo apt-get -y install exuberant-ctags`



# NerdTree:

download `https://github.com/ryanoasis/nerd-fonts/blob/master/patched-fonts/FiraCode/Regular/complete/Fira%20Code%20Regular%20Nerd%20Font%20Complete.ttf` 

run `sudo mv Download/Fira Code Regular Nerd Font Complete.ttf /usr/local/share/fonts/`

set it as terminal font



# Copilot:

**Update node js to 16.x version**:
   
   

```
npm cache clean -f

npm install -g n

sudo n stable

```

# Jupyter Notebook

`pip install --upgrade jsonschema`
`pip install jupyter_contrib_nbextensions`
`jupyter contrib nbextension install --user`


```
sudo pip install jupyter_ascending && \
python3 -m jupyter nbextension    install jupyter_ascending --sys-prefix --py && \
python3 -m jupyter nbextension     enable jupyter_ascending --sys-prefix --py && \
python3 -m jupyter serverextension enable jupyter_ascending --sys-prefix --py
```

```
jupyter nbextension     list
jupyter serverextension list
```

```
$ jupyter nbextension install --py --sys-prefix jupyter_ascending
$ jupyter nbextension     enable jupyter_ascending --sys-prefix --py
$ jupyter serverextension enable jupyter_ascending --sys-prefix --py
```

```pip install jupytext```

`jupytext --set-formats ipynb,py:percent notebook.ipynb`

jupyter notebook --generate-config
set this in `~/.jupyter/jupyter_notebook_config.py` c.NotebookApp.disable_check_xsrf = True

PLUG IN in .vim/plugged
let g:jupyter_ascending_python_executable = get(g:, 'jupyter_ascending_python_executable', 'python3') !!!python3

let g:jupyter_ascending_match_pattern     = get(g:, 'jupyter_ascending_match_pattern', '.py')

# Fzf
`sudo apt-get install bat`

`sudo apt-get install ctags`

For ubuntu:

```
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat```

# Vimtex
`sudo apt install latexmk`
`:CocInstall coc-vimtex`

# Bash config

Install starship = `curl -sS https://starship.rs/install.sh | sh`
