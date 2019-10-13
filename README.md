# wwuMailTrack
A simple python script for checking the status of your WWU packages

### Requirements:

First make sure you have python3 installed, then install the dependencies using the command:

```
python -m pip install -r requirements.txt
```


### Usage:

First, find the tracking number of your package by searching for your name on the WWU internal mail tracking website, found [here](https://wwu.sclintra.com/Mail). It may take some time before your package tracking number is added to the system.

Then, invoke trackMail with the tracking number of your package.

```
trackMail.py <tracking number>
```
