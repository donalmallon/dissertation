# Do UK Petitions persuade Debates on New Topics? 

# Donal Mallon's Final Year Project- 40154387

The aim of this project is to compare the lanuage used in petitions 
submitted through  with the UK petitions website with laguage used in 
parliamentary debates through topic modeling. This will give an insight 
into which topics  

All results are repreoducable, to run them on a different system simply 
run each Jupyter Notebook in JupyterLab/JupyterNotebook from 000-300.
Subsequently the Python program 400_UI.py should be run. 
*Note 000_Petitions_Data_Collection.ipynb requires additional CSV files 
as included. 

The requirements to run each program can be found in the file Requirements.md


I have included data frames (in pickle form) obtained through the data 
collection and analysis so that the Python program 400_Topic_Explorer.py
can be run by itself without going through the time consuming data collection 
and modelling process. A user manual is provided for this in UserGuide_400.md. 

## Files Included:

### Jupytyer Notebook Files:
    
    000_Petitions_Data_Collection.ipynb 
    100_Transcripts_Data_Collection.ipynb
    200_Model_Creation.ipynb
    300_Analysis.ipynb

### Python Files: 
    
    400_Topic_Explorer.py

    
### CSV Files:

        published_petitions-2015–2017.csv:
            A CSV file containing published peitions between 2015-2017
        published_petitions-2010-2015.csv:
            A CSV file containing published peitions between 2010-2015
        closed_petitions.csv:
            A CSV file containing closed peitions from 2017-present

### Data Frame Files for 400_Topic_Explorer.py:
     petitions_topics_sorteddf.pickle
     petitions_info.pickle
     topic_sim.pickle
     tscript_topics_sorteddf.pickle
     
