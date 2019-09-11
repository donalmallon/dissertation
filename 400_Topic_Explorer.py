
# Before running program insure that the configuration script path is set to this file
# Python interpretor  Python 3.6.1
# Also insure the following libraries are installed on your system


import pandas as pd
from functools import partial
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import*
import webbrowser



## Load in df of documents that are most representative of each topic


petitions_topics= pd.read_pickle("petitions_topics_sorteddf.pickle")
tscript_topics= pd.read_pickle("tscript_topics_sorteddf.pickle")

## Load in short version of petition and transcript info

petitions_info = pd.read_pickle("short_petitions_info.pickle")

## load in topic similarity data frame
topic_sim = pd.read_pickle("topic_sim.pickle")


####### Create Window ########



class main:

    def __init__(self, master):
        ## create frame for grid containing topic words
        frame = Frame(master)
        frame.grid(row=0,column=0, sticky='n')

        def graph(topicNum, isPetition):
            if isPetition==True:

                if labels[int(topicNum)].cget("text") !=' ✓ ':
                    labels[int(topicNum)]["text"]=' ✓ '
                else:
                    labels[int(topicNum)]["text"] = ''

                # find reference of all ticked items

                topicNumbers= []
                for i in range(0, len(set(petitions_topics.Keywords))):
                    if labels[i].cget("text") ==' ✓ ':
                        topicNumbers.append(i)

                    #create graph
                fig = Figure(figsize=(5.5,5 ), dpi=100)

                ax = fig.add_subplot(111)
                ax.set(xlabel='Debates Topic Number', ylabel='Similarity',
                       title='Topic Similarity')
                ax.xaxis.set_ticks(np.arange(1, 21, 1))
                print(topicNumbers)
                for topics in topicNumbers:
                    x = np.arange(1, 21)
                    y = topic_sim.iloc[topics]

                    ax.plot(x, y)


                self.canvas = FigureCanvasTkAgg(fig, master=frame)
                self.canvas.draw()
                self.canvas.get_tk_widget().grid(row=0, column= 4,rowspan=20)

            else: # if a debate
                print('')


            #reset



        def topics_window(df,topicNum):  # new petitions window definition


            newwin = Toplevel(root)
            newwin.geometry('720x480')
            txt = df.Keywords.iloc[2]
            ' '.join(word[0] for word in txt)
            txt = txt.split()
            title = Label(newwin, height=2, width=50,
                          text='Petitions Topic ' + str(topicNum),
                          font=("CMU Sans Seriff", 28))
            title.pack()
            # display top 5 topics
            topics = Label(newwin, height=2, width=50,
                          text=txt[0:5],
                          font=("CMU Sans Seriff", 28), fg= 'green')
            topics.pack()

            docNumbers = df.Document.values
            for i in docNumbers:
                display = Button(newwin, text=petitions_info.Petition[i], command= partial(openPetition,i))
                display.pack()

 # open petition website
        def openPetition(petNum):
            webbrowser.open_new(str(petitions_info['URL'][petNum]))

        ## create a list of labels
        labels = []
        for i in range(1, len(set(petitions_topics.Keywords))+1):
            l = Label(frame, text="")
            labels.append(l)
            l.grid(row=i, column=3, padx=(0.5, 0.5), pady=(0.5, 0.5), sticky=W)

        # petitions topics
        self.T= Label(frame,height =1 , width = 10, text= "Petitions", font= ("CMU Sans Seriff",20))
        self.T.grid(row=0,column=2,sticky=W)

        # create petitions topics buttons
        for i in range (1, len(set(petitions_topics.Keywords))+1):
            # create a temp df for only one df
            tempdf = petitions_topics.loc[petitions_topics.Topic_Num == i-1]
            self.topic = Button(frame, text='Topic ' + str(i),
                                command=partial(topics_window,tempdf, i),
                                font=("CMU Serif Extra", 16))

            self.topic.grid(row=i ,padx=(1, 1), pady=(1, 1),sticky=W)

            self.petition = Button(frame, text=petitions_topics.Keywords[(i-1)*5].split()[0:5],
                                   command=partial(graph,petitions_topics.Topic_Num[(i-1)*5],1),
                                   font=("CMU Sans Serif", 12))



            self.petition.grid(row=i,  column= 2, pady=(2,2),sticky=W)


        # debate transcript topics
        self.T2 = Label(frame, height=1, width=10, text = "Debates", font= ("CMU Sans Seriff",20))
        self.T2.grid(row=0,column=7,sticky=W)

        for i in range (1, len(set(tscript_topics.Keywords))+1):
            self.topic = Label(frame, text='Topic '+str(i), font=("CMU Serif Extra", 16))
            self.topic.grid(row=i, column=6, padx=(0.5, 0.5), pady=(1, 1),sticky=W)

            self.tscript = Label(frame, text=tscript_topics.Keywords[(i-1)*5].split()[0:5],
                                 font=("CMU Sans Seriff", 12))
            self.tscript.grid(row=i, column =7,padx= (0.5,0.5), pady=(2,2),sticky=W)


        # create list of labels so can tell which is ticked






















root = Tk()
b = main(root)
root.mainloop()