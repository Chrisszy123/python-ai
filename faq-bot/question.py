# from knowledgebase import knowledge_base
import json

# load knowlege
with open("knowledgebase.json", 'r') as file:
    knowledge_base = json.load(file)
# we want to take an input from the user, as a question

while True: 
    question = input("Ask me a question: ").lower()

    if question == "quit":
        break

    found = False

    for keyword in knowledge_base: # create a keyword variable for the data in the knowledge base
        if keyword in question: # check is the keyword in the knowledge base is in the question
            print(knowledge_base[keyword]) # print the the value for the particular keyword
            found = True
            break

    if not found: 
        answer = input("I don't know the answer, please Teach me: ")
        knowledge_base[question] = answer

        #save to json
        with open("knowledgebase.json", "w") as file:
            json.dump(knowledge_base, file, indent=4)
        
        print("oH thanks I have learnt something new!")


# if question in knowledge_base:
#     print(knowledge_base[question])
# else: 
#     print("I don't know the answer")