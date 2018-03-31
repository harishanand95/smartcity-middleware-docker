#!/usr/bin/env bash
cd build/
pwd
sudo dpkg -i ideam_0.0-1.deb
sudo dpkg --remove ideam
sudo apt-get -y update && sudo apt-get install -y software-properties-common && sudo apt-add-repository ppa:ansible/ansible -y && sudo apt-get -y update && sudo apt-get install -y ansible
sudo apt-get install -y apt-transport-https  ca-certificates curl software-properties-common
sudo apt install python -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" -y
sudo apt-get update -y
sudo apt-get install docker-ce -y
sudo usermod -aG docker $USER
ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N ''
sudo sysctl -w vm.max_map_count=662144
sudo dpkg -i ideam_0.0-1.deb