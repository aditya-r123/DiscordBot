import random
import flaskapp



array1 = ["<@830181110134210590>\n", "<@766757435955609690>\n", "<@657390777013633025>\n", "<@688840158321180761>\n"]
array2 = ['geo', 'pyt', 'jav', 'ame', 'sci', 'wri', 'fre', 'man', 'sin', 'his', 'pub', 'mat', 'deb', 'car', 'spa', 'mus', 'art', 'c++', 'bus', 'dan', 'med', 'hin', 'psy', 'env', 'ios', 'ana','eco', 'phi']
array3 = ['Geography', 'Python', 'Java', 'American Sign Language', 'Science', 'Writing', 'French', 'Mandarin', 'Singing', 'History', 'Public Speaking', 'Math', 'Debate', 'Card Making', 'Spanish', 'Music Theory', 'Art', 'C++', 'Business', 'Dance', 'Medical Enrichment', 'Hindi', 'Psychology', 'Environmental Science', 'iOS Development', 'Anatomy and Physiology','Economics', 'Philsophy and Critical Thinking']
array4 = ['<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>', '<@879866747979706409>']


def get_response(message: str) -> str:
    lower_message = message.lower()
    if lower_message == 'hello':
        return 'Hey there!'
    if lower_message == 'bye':
        return 'Goodbye!'
    if lower_message == '!help':
        return 'List of commands:\n\n•!contact: outputs the Discord ID of who you want to contact '
    if lower_message == '!contact':
      return 'Who are you looking to contact? Enter \'ProgramLead\' or \'ExecMember\''
    if lower_message == 'programlead':
      return 'Enter the first 3 letters of the program who\'s lead you want to contact'
    if len(lower_message) == 3:
      for item in array2:
        if(lower_message == item.lower()):
          i = array2.index(lower_message)
          return 'The program lead for ' + array3[i] + ' is ' + array4[i] + ". You can DM them to see if you can join their program or any other questions you may have. If you haven't already, join the program's Discord group using <#713117616037822557> " 
          i=0
    if(lower_message == 'asl'):
          i=3
          return 'The program lead for ' + array3[i] + ' is ' + array4[i] + ". You can DM them to see if you can join their program or any other questions you may have. If you haven't already, join the program's Discord group using <#713117616037822557> " 
          #return "Here you go!\n\n\n•Student Growth --> <@830181110134210590>\n•Team Expansion --> <@766757435955609690>\n•Systems --> <@657390777013633025>\n•Membership --> <@688840158321180761>\n\nYou can DM them to see if you can join their program or any other questions you may have. If you haven't already, join the program's Discord group using <#713117616037822557>!"
    if lower_message == 'execmember':
      return "Which non-teaching team you are looking to join? Enter \'StudentGrowth\', \'TeamExpansion\', \'Systems\', or \'Membership\'"
    if(lower_message == 'student' or lower_message == "studentgrowth"):
      return "You can DM " + array1[0] + " to join the Student Growth team!"
    if(lower_message == 'team' or lower_message == "teamexpansion"):
      return "You can DM " + array1[1] + " to join the Team Expansion team!"
    if(lower_message == 'systems'):
        return "You can DM " + array1[2] + " to join the Systems team!"
    if(lower_message == 'membership'):
      return "You can DM " + array1[3] + " to join the Membership team!"    
    if lower_message == 'yes':
      return "Here you go!\n\n\n•Student Growth --> <@830181110134210590>\n•Team Expansion --> <@766757435955609690>\n•Systems --> <@657390777013633025>\n•Membership --> <@688840158321180761>\n\nYou can DM them to see if you can join their team!"
    if lower_message == 'no':
      return "Consider asking your question in <#798262779006025799> or taking a look at <#806287344272801842>"
