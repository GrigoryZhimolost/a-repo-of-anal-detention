Send some files to another computer directly, without inermediars and complicated setting up such as ssh

# How to use
Copy this repo and create _config.py_ file. It must have _KEY_ and _PORT_ variables. KEY must be 32 bytes size.
Then type `python main.py -w` if you want to accept connection, so it accepts automaticly. To send some files type `python -m main.py -c <IP-OF-SERVER> -f <file(s)>` If there're more than one file separate paths only with commas with no spaces.
