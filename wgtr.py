# chat bot ai wgtr
# developer amirmahdi heydari 
# 
# 
# 
# 


# libreri 
import random , os , sys , time, subprocess 
#....

# data ai 
data_chat_user = {
    'nam' : None , 
    'info us ' : None
}
data_chat = {
    'hello' :  'hello are yuo ok  ? ',
   'python' : 'My friend, Python is a programming language that developers use to develop their projects. This language is popular because of its high level of development of websites, user interface, artificial intelligence, and cybersecurity. Today, this language has become very popular because of its ease. Even I have developed with this language.'
}




data_saive = True
system_key = True 


def system_os_wgtr (data_user2):  # for system 
    global data_chat_user 
    global data_chat 
    global data_saive


    if data_saive ==  True :
        data_file =  open ('data_wgtr1.wgtr','+w') # seiv data file us 
        dataf = data_file.read ()
        data_file.write (str(data_chat))
        data_file.close ()   # close file data 
        # new seiv 
        data_file2 = open ('data_wgtr2.wgtr','+w') # seiv data 
        datafs = data_file2.read ()
        data_file2.write (str( data_chat_user)) 
        data_file2.close ()  # close data file  
    else :
       print ('pay atteition /; seiv data a not active !')



def system_al_wgtr(data_user) :   # ai 
    global data_chat 
    global data_chat_user
    global system_key



    if data_chat .get (data_user) != None and system_key == True :     # system cunwestion 
        print ('in ' , data_chat[data_user], 'soly dashti bpors ! ') #...


    if  data_chat.get (data_user) == None and system_key == True :     # system ai lerning 
        print ('man nemidonam : ',data_user,' :( misheh yadam bedi ? :)') 
        ffg = input ('ok or no ? ')
        if ffg == 'ok' :
            print  ('mamnonam :)))) ')
            ss = input ('nam data gadid cheih ? ')
            ff = input ('mohtava data gadid chieh ? ')
            data_chat[ss]  = ff 
            system_os_wgtr ('tat')
            print ('.......///')
            time.sleep (4)
            print (' ok damet garm :) ')
        else :
            print ('ok :( ')  # sting data us wgtr 

   
    if data_user == "wgtr // go // system" :
      print ('going to system  ...//')
      time.sleep (5)
      za  = input ('wgtr // system // : ')
      if  za== 'wgtr // system // loce' :
        system_key = False
        system_os_wgtr ('data')
      elif za == 'wgtr // system // on' :
        system_key = True 
        print ('chat close ...//')
      if za == 'wgtr // system // off saive data' :
         data_saive == False 
         print ('saive data off ! ')
      elif za == 'wgtr // system // on saive data' : 
         data_saive = True
         print ('data saive on :)')
      if   za  == 'wgtr // system // info // us' :   # panel system for seiv data us 
         print ('going to system us ....... /// ')
         time.sleep (10)
         dd = input ('nam godet ro bego : ')
         aa = input ('darbareh goodet bogo  : ')
         if data_chat_user.get (dd) and data_chat_user.get (aa) !=  None  :
           data_chat_user[dd]= aa
           print ('darm yad migiram ......./// ')
           time.sleep (5)
           print ('ok  qut in system // info // us ')
         else :
          print ('man mashnasamet rafig ! ')
    else :
        print ('what ?')




a = True
# starting .... 
print ('starting ..//')
time.sleep (10)
system_os_wgtr ('da')
while a == True  :
   wgtr = input ('inter maseige : ')
   print ('...//')
   time.sleep (3)
   system_al_wgtr (wgtr)
