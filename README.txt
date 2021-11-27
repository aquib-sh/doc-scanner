        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$ GOOGLE DOCS SCANNER $$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


## INSTALLATION
------------------------------------------------------------------------------------------------
DOWNLOAD THE LATEST VERSION OF PYTHON FROM: 
https://www.python.org/downloads/

$> For Windows 10
==========================================================================================
While running the installer you will see an option to 'Add to PATH'
at the very beginning of the installer page.
Make sure to check(tick) that option.

Now open your PowerShell or CMD and run the below command
________________________________________________________________________________________
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
________________________________________________________________________________________
==========================================================================================

$> For MacOS or Linux
==========================================================================================
Now open your Terminal and run the below command
________________________________________________________________________________________
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
________________________________________________________________________________________
----------------------------------------------------------------------------------



## RUNNING
---------------------------------------------------------------
For Windows 10
==========================================================================================
Open your PowerShell/CMD and navigate to the directory(folder) where script is installed
navigate using cd command
(or you can open the folder in explorer and copy the path on top and paste it in cmd/PowerShell)

Now, run the below command on your PowerShell/CMD
____________________________________________
python scan.py
____________________________________________
==========================================================================================

For MacOS or Linux
==========================================================================================
Open your Terminal and navigate to the directory(folder) where script is installed
navigate using cd command

Now, run the below command on your Terminal
____________________________________________
python3 scan.py
____________________________________________
==========================================================================================


## PROVIDING INPUT TO THE SCRIPT
---------------------------------------------------------------
The inputs are taken from input.json file present in the same directory as script:

Here is an example:
-------------------------------------------------------------------------------------------------
    "1":{
        "link":"https://docs.google.com/document/d/1w4gSqDc1K-Hh3LMKY1ZT0qua5z6L0Ym1s75eOOWf_Tk/edit",
        "keywords":[
            "COVID"
        ],
        "case_sensitive":true
    },
-------------------------------------------------------------------------------------------------

$> Keys & their meanings:

1> "1": This is just the number of entry, when you add a new entry below you should increment it,
        like next will be "2", "3" and so on...

Each {} specifies the boundry. when you add a new entry a comma (,) must be added

2> "link": This is the link of document which is to be scanned for sentences with keywords
3> "keywords": This is a list of keywords to search the brackets[] means list,
               each value in list must be seperated by a comma 
               (example: ["hairs", "nose", "cats", "dogs"] )
4> "case_sensitive": This specifies whether to search case sensitively or not
                (example:
                    when it is set to true then "hair" is not equal to "Hair" or "HAIR"
                    when it is set to false then "hair" = "Hair" = "HAIR"
                )

    
