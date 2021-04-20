# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
### From your Office make sure you unset the proxy ###

```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

#################################################
Testing
Unit testing
To run unit tests use the command:

$ pytest .\tests\
Integration testing to follow
#################################################

# Vagrant
On a mac download ind install the official version https://www.vagrantup.com 

Make sure proxy's are unset or disabled

run vagrant up from your cloned directory 
You'll be asked to choose a switch to attach to the Hyper-V instance. Select the external switch created during the Hyper-V setup.

The machine will now report it's IP address. Take note of this as it will be used to access the application later.

The command may request your username and password. Enter your Windows credentials (the @domain is optional).

The Vagrantfile within this repo will:

Pull down a Ubuntu Linux image to run the app
Prep your VM for Python installation
Install Python 3.6.6
Install poetry and load any dependencies
Launch the TODO app
Add the IP of the VM to your browser with the port of 5000 to see the TODO application.

access the todo app from http://0.0.0.0:5000/ 