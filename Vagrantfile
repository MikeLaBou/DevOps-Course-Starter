Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", privileged: true, inline: <<-SHELL 
    
  sudo apt-get update
  sudo apt-get install build-essential
  
  # TODO: Install pyenv prerequisites
  sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git 

  # TODO: Install pyenv
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv 
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile 
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile 
  echo 'eval "$(pyenv init -)"' >> ~/.profile
  export PYENV_ROOT="$HOME/.pyenv"
	export PATH="$PYENV_ROOT/bin:$PATH"
  source ~/.profile
  eval "$(pyenv init -)"
	pyenv install 3.8.3
	pyenv global 3.8.3
  

  # TODO: Install poetry
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
  echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.profile
  export PATH="$HOME/.poetry/bin:$PATH"
SHELL

  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO application setup script"
    trigger.run_remote = {privileged: false, inline: "
      cd /vagrant
      poetry install
      nohup poetry run flask run --host=0.0.0.0 > logs.txt 2>&1 &
    "}
end
end
