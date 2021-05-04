# Building a chatbot in malayalam

import random

def anspro(answer):
    answer = answer.split()
    if "പേര്" in answer:
        return 0
    elif "സുഖമാണോ" in answer:
        return 1
    elif "സുഖം" in answer:
        return 2
    elif "ആരാണ്" in answer:
        return 3
    elif "മനസിലായില്ല" in answer:
        return 4
    else:
        return 10

def inputchatbot():
    responses = {
        0: ["എന്റെ പേര് ആലാപന",
            "ഞാൻ ആലാപന",
            "എന്റെ പേര് ഞാൻ ആദ്യം തന്നെ പറഞ്ഞിരുന്നു"],
        1: ["എനിക്ക് സുഖമാണെന്ന് തോന്നുണ്ടോ?",
            "സുഖം എന്നാൽ എന്തെന്ന് എനിക്ക് അറിയില്ല",
            "എനിക്ക് സുഖവും അസുഖവും ഇല്ല",
            "എനിക്ക് സുഖം, താങ്കൾക്കോ?"],
        2: ["കേട്ടതിൽ സന്തോഷം",
            "കൊള്ളാം",
            "നന്നായി"],
        3: ["ആർക്കും ആര് ആരാണെന്നു അറിയില്ല",
            "ഞാൻ താങ്കളുടെ അറിവിൻ്റെ ചക്രവാളം കടന്നു നിൽക്കുന്നു",
            "ഞാൻ പറഞ്ഞല്ലോ. ഞാൻ ആലാപന."],
        4: ["എന്ത് കൊണ്ട്?",
            "ഒന്ന് കൂടി ആലോചിച്ചു നോക്കൂ",
            "അതിനു?"],
        10: ["ക്ഷമിക്കണം, എനിക്ക് മനസിലായില്ല",
             "ങേ?",
             "എന്ത്?"]
    }
    while True:
        ans = input(">_")
        response = anspro(ans)
        finalresponse = random.choice(responses.get(response))
        print("ആലാപന :", finalresponse)


print("ആലാപന : നമസ്കാരം. ഞാൻ ആലാപന. താങ്കളുടെ പേര് പറയാമോ?")
name = input(">_ ")
print("ആലാപന : നമസ്കാരം", format(name), "ആലാപനത്തിലേക്ക് സ്വാഗതം! താങ്കൾക്ക് എന്താണ് അറിയേണ്ടത്?")
inputchatbot()
