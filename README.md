[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/apcvbojB)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12489224&assignment_repo_type=AssignmentRepo)


## How to Run
1. Make sure you have python version 3.11 at least
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
2. Run `./requirements.sh` to install libraries
3. Run `flask --app api/app.py run` to run server