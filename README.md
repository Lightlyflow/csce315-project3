## How to Run (Option 1)
1. Requirements
   1. See [setup](./setup.md)
2. Make sure you have python version 3.11 at least
   1. If not and you're on Unix:
      1. `sudo apt update && sudo apt upgrade`
      2. `sudo add-apt-repository ppa:deadsnakes/ppa`
      3. `sudo apt-get update`
      4. `apt list | grep python3.11` to check if 3.11 is listed, if not, then we have problems
      5. `sudo apt-get install python3.11` Install python 3.11
      6. `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1` Set python3 to use 3.11 by default
      7. `sudo apt install python3.11-distutils` Download distutils
      8. `curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11` Download latest pip version
   2. If you're on Windows
      1. Go download 3.11 from the python website
      2. WIP
3. Run `./requirements.sh` to install libraries
   1. If you don't have perms `chmod u+x requirments.sh`
4. If you don't have the `.env` file in the `api` folder:
   1. Go and download the file from the Google Drive project folder
   2. Rename the file to `.env`
   3. Move the file into the `api` folder
5. Run `flask --app api/app.py run` to run server

## How to Run (Option 2 - Docker)
1. Requirements
   1. `Docker`
2. Make sure you are in the project root
3. ```docker build -t project3 .```
4. ```docker run -p 5000:5000 project3```

---
## Generate Documentation
1. Create the docstrings in the python file
2. Run `./gen_docs.sh`
3. Docs can be accessed at `/9o3yh223w8jaolp1qo2/docs/index.html`
