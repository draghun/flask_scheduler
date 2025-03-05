Demo of flask scheduler. 

### to set up
    ``conda create -f cicd/environment.yaml``

### to run
    ``python app.py``

update_data writes an update message to app.json every 30 seconds. 
The index renders the templates/index.html.
The index.html code sends a request to flask /data path to retrieve 
the contents of the app.json file. 
The index.html file displays the contents of app.json as a table. 
Refresh the front page for updates of these messages. 