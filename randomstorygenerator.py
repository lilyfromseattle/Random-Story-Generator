from random import randint
nouns = ["pumpkin", "cat", "princess", "turtle", "banana", "dentist", "sandwich", "bandaid", "old shoe", "bulldog"]
adjectives = ["silly", "ugly", "rotund", "sneaky", "magical", "chubby", "stupid", "illusive", "famous", "mythical"]
places = ["Disneyland", "the beach", "Dubai", "the rainforest", "Brooklyn", "the dump", "Palm Beach", "the bottom of the ocean", "The Cheesecake Factory", "New Zealand"]



print "Welcome to the random story generator!"
adj1 = adjectives[randint(1,10)]
noun1 = nouns[randint(1,10)]
noun2 = nouns[randint(1,10)]
place1 = places[randint(1,10)]

print "Once upon a time there was a " + adj1 +" "+ noun1 + "." + " The " + noun1 + " lived in a " + noun2 + " in the middle of " + place1 + "." 

