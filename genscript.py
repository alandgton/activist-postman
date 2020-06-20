import json

subjects = [] #possible subjects (chosen randomly with equal probability). these are json objects of format:
"""
    {
        "subjects": ['The subject of this email', 'Email subject', 'This is the subject that corresponds to the following email you are abou to read! And it is quite a good subject']
    }
"""
recipients = []
chunks = '' #user-defined chunks of body.  these are json objects of format:
"""
    {
    "type": "This type can either be 'fixed' or 'random'. If fixed, it is printed no matter what. If random, it is an array of equiprobable options of which one will be selected to print",
    "fixed_field": "text to be used if type is fixed",
    "random_field": ['options to randomize from', 'equiprobable options to randomize and print', 'options, one of which will be printed']
    }
    """

#name = [] #this actually wouldn't be needed as an arg
#bodyargs = [] #user defined body args -- this may be pretty difficult and somewhat unecessary


"""
EMAIL format
____________
The generated email body is organized here as just a set of chunks, nothing else. chunks are either fixed or randomized.
See the chunks variable at the bottom of this code for how the email body is organized in JSON.
"""

def code_start():
    return """
# -*- coding: utf-8 -*-
import random
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)

@app.route("/p/genmsg/")
def gen_msg():
    #return "%s;%s" % (gen_subject(), gen_body())
    return "Subject: " + gen_subject() + "\\n\\nBody:\\n" + gen_body()

def gen_subject():
    return random.choice(subjects)

subjects = """ + str(json.loads(subjects)['subjects']) + "\n" + code_chunks()

#generates code for all chunks
def code_chunks():
    acc = 0
    chunkfuncs = """"""
    chunktion_calls = """"""
    for c in chunks:
        chunkfuncs += code_chunkfunc(c, acc)

        if acc != 0:
            chunktion_calls += " + chunk%d()" %acc
        else:
            chunktion_calls += "return chunk%d()" %acc

        acc += 1
    return chunkfuncs + "def gen_body():\n\t" + chunktion_calls + "\n"

#generates code for a given chunk
def code_chunkfunc(chunk, numchunk):
    chunkfunc = """def chunk%d():\n""" % numchunk
    c = json.loads(chunk, strict=False)
    if c['type'] == 'fixed':
        chunkfunc += ('\treturn """' + c['fixed_field'] + '"""\n') #maybe should implement string checking, but i doubt they will put triple quotes...this is intended to be approved by humans anyway so should be ok, just make sure to check here
        #CHECK THAT THEY DIDN'T PUT TRIPLE QUOTES IN THEIR INPUT...or they can execute arbitrary python code on our server haha

    elif c['type'] == 'random':
        chunkfunc += '\tchoices=' + str(c['random_field']) + '\n\treturn random.choice(choices)' + '\n'

    else:
        raise NameError('Error: chunk is missing valid "type" field')

    return chunkfunc

def code_end():
    return """\nprint(gen_msg())"""


#now that it's all set up, manually set the arguments (for now) and run the code
subjects = """{"subjects": ["CHECK OUT THIS GREAT EMAIL:", "YOU HAVE RECEIVED AN EMAIL"]}"""
chunks = [
    """
    {
    "type": "random",
    "fixed_field": "",
    "random_field": ["Howdy,\n", "Good Evening,\n", "options, one of which will be printed"]
    }
    """,
    """
    {
    "type": "fixed",
    "fixed_field": "How's it going?",
    "random_field": []
    }
    """,
    """
    {
    "type": "random",
    "fixed_field": "",
    "random_field": ["Hopefully, pretty terrible!\n", "Hopefully well!\n", "®"]
    }
    """
    ]

print(code_start())
print(code_chunks())
print(code_end())
