# Java is also required
sudo apt update -y
sudo apt install python3-pip graphviz -y
pip3 install --upgrade pipenv==2021.5.29  # because of pipenv bug #4829
pip3 install jsonschema
wget https://github.com/joelittlejohn/jsonschema2pojo/releases/download/jsonschema2pojo-1.1.1/jsonschema2pojo-1.1.1.tar.gz
tar zxvf jsonschema2pojo-1.1.1.tar.gz && rm jsonschema2pojo-1.1.1.tar.gz
export PATH=${PATH}:$(pwd)/jsonschema2pojo-1.1.1/bin
