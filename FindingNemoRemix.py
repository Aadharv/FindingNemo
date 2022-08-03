
story="A fish called Nemo was stuck in an underwater prison because he stole gold coins from the underwater bank.To escape from the prison he needed to sneak past many sword fish and sharks .He made a spoon from the mirrors material and cut the bars of his prison cell at midnight.On his way he saw a baby sea turtle who was lost.Nemo took the sea turtle with him because it was near a dangerous place.Nemo saw a swordfish who had spooted him.The swordfish alerted the whole prison there was an escape .All sharks and swordfish came to find out what was going on.Nemo was doomed but he took out his shark disguise he made from the bedsheets and blended with all the guards.The turtle was with Nemo under the belly of the disguise . Nemo went to the front gate of the prison and ran away to freedom with his new turtle friend."
word='Nemo'
def check(story, word):
    if (story.find(word)== -1):
        print("This word isnt present in the story")
    else:
       print("This word is present in the story")

check(story, word)
