#!/usr/bin/bash

# Colours
declare -r greenColour="\e[0;32m\033[1m"
declare -r endColour="\033[0m\e[0m"
declare -r redColour="\e[0;31m\033[1m"
declare -r blueColour="\e[0;34m\033[1m"
declare -r yellowColour="\e[0;33m\033[1m"
declare -r purpleColour="\e[0;35m\033[1m"
declare -r turquoiseColour="\e[0;36m\033[1m"
declare -r grayColour="\e[0;37m\033[1m"

# Global Variables
declare -r pythonLibrary=(termcolor)
declare -r dependencies=(aircrack-ng)

function dependencies(){
	clear

	echo -e "\n"
	read -rp "Cual es su OS >> Arch Linux[a/A] or Ubuntu[u/U]: " sys

	for program in "${dependencies[@]}"; do
		echo -ne "\n\t${yellowColour}[*]${endColour}${blueColour} Herramienta${endColour}${purpleColour} $program${endColour}${blueColour}...${endColour}"

		test -f /usr/bin/$program

		if [ "$(echo $?)" == "0" ]; then
			echo -e " ${greenColour}(V)${endColour}"
	
		else
			echo -e " ${redColour}(X)${endColour}\n"
			
			if [ "$sys" == "a" ] || [ "$sys" == "A" ]; then	
				sudo pacman -S $program
			
			elif [ "$sys" == "u" ] || [ "$sys" == "U" ]; then
				sudo apt-get install $program	
			fi
		fi
	done
}

function installPythonLibrary(){
	for library in "${pythonLibrary[@]}"; do
		pip install $library 2>/dev/null
		pip3 install $library 2>/dev/null
	done
}

if [ "$(id -u)" == "0" ]; then
	dependencies
	installPythonLibrary
else
	echo -e 'sudo chmod +x ./install.sh && sudo bash ./install.sh'
fi
