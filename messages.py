# -*- coding: utf-8 -*-

import random
import inquire as inq
import demand as dem


#excluding George Floyd as he's first (for people to recognize what the list is of)
saytheirnames_list = ["Eric Garner","John Crawford III","Michael Brown","Ezell Ford","Dante Parker","Michelle Cusseaux","Laquan McDonald","George Mann","Tanisha Anderson","Akai Gurley","Tamir Rice","Rumain Brisbon","Jerame Reid","Matthew Ajibade","Frank Smart","Natasha McKenna","Tony Robinson","Anthony Hill","Mya Hall","Phillip White","Eric Harris","Walter Scott","William Chapman II","Alexia Christina","Brendon Glenn","Victor Manuel Larosa","Jonathan Sanders","Freddie Blue","Joseph Mann","Salvado Ellswood","Sandra Bland","Albert Joseph Davis","Darrius Stewart","Billy Ray Davis","Samuel Dubose","Michael Sabbie","Brian Keith Day","Christian Taylor","Troy Robinson","Asshams Pharaoh Manley","Felix Kumi","Keith Harrison McLeod","Junior Prosper","Lamontez Jones","Paterson Brown","Dominic Hutchinson","Anthony Ashford","Alonzo Smith","Tyree Crawford","India Kager","La’vante Biggs","Michael Lee Marshall","Jamar Clark","Richard Perkins","Nathaniel Harris Pickett","Benni Lee Tignor","Miguel Espinal","Michael Noel","Kevin Matthews","Bettie Jones","Quintonio Legrier","Keith Childress Jr.","Janet Wilson","Randy Nelson","Antronie Scott","Wendell Celestine","David Joseph","Calin Roquemore","Dyzhawn Perkins","Christopher Davis","Marco Loud","Peter Gaines","Torrey Robinson","Darius Robinson","Kevin Hicks","Mary Tuxillo","Demarcus Semer","Willie Tillman","Terrill Thomas","Sylville Smith","Alton Sterling","Philando Castle","Terence Crutcher","Paul O\'Neal","Alteria Woods","Jordan Edwards","Aaron Bailey","Ronell Foster","Stephon Clark","Antwon Rose II","Botham Jean","Pamela Turner","Dominique Clayton","Atatiana Jefferson","Christopher Whitfield","Christopher McCorvey","Eric Reason","Michael Lorenzo Dean","Breonna Taylor","Tony McDade","Nina Pop"]

# Generates a list of num names killed by police #saytheirnames
def saytheirnames_sublist(num, seen):
    if num == 0:
        return ""
    elif num == 1:
        name = random.choice(saytheirnames_list)
        while name in seen:
            name = random.choice(saytheirnames_list)
        seen.append(name)
        return name
    else:
        name = random.choice(saytheirnames_list)
        while name in seen:
            name = random.choice(saytheirnames_list)
        seen.append(name)
        return name + ", " + saytheirnames_sublist(num-1, seen)

# Randomly generates the subject header of the email
def gen_subject(): #note can this function be used later if its part of the app route? (im very new to flask)
    s = ["Human Rights Inquiry","Thoughts of a Concerned Citizen","In Light of Recent Human Rights Abuses","The Need for Police Oversight","The Need for Police Accountability","The Failures of Modern Law Enforcement","Law Enforcement Must Change","The Voice of a Troubled Citizen","The Need for Law Enforcement Reform","Reforms to Law Enforcement Needed","Your Duty as a Public Servant","Your Responsibility as a Public Servant","Allaying Systemic Racism","Allaying Systemic Racism & Preventing Police Brutality","Preventing Police Brutality & Allaying Systemic Racism","Ameliorating Systemic Racism","Ameliorating Systemic Racism & Preventing Police Brutality","Preventing Police Brutality & Ameliorating Systemic Racism","Mitigating Systemic Racism","Mitigating Systemic Racism & Preventing Police Brutality","Preventing Police Brutality & Mitigating Systemic Racism","Systemic Racism & Police Brutality","We need your help","Please help us","Concerns About Systemic Racism & Police Brutality","Concerns About Police Brutality & Systemic Racism","Policies for Police Brutality & Addressing Systemic Racism","Addressing Systemic Racism","Addressing Systemic Racism & Police Brutality","Black Lives & Police Brutality","Black Lives & Police Brutality","Black Lives & Systemic Racism","Black Lives & Police Policy","Black Lives & Police","Police Policy & Black Lives","Police Brutality & Black Lives","Allaying Systemic Racism and Preventing Police Brutality","Preventing Police Brutality and Allaying Systemic Racism","Ameliorating Systemic Racism and Preventing Police Brutality","Preventing Police Brutality and Ameliorating Systemic Racism","Mitigating Systemic Racism and Preventing Police Brutality","Preventing Police Brutality and Mitigating Systemic Racism","Systemic Racism and Police Brutality","Concerns About Systemic Racism and Police Brutality","Concerns About Police Brutality and Systemic Racism","Policies for Police Brutality and Addressing Systemic Racism","Addressing Systemic Racism and Police Brutality","Black Lives and Police Brutality","Black Lives and Police Brutality","Black Lives and Systemic Racism","Black Lives and Police Policy","Black Lives and Police","Police Policy and Black Lives","Police Brutality and Black Lives","The Murder of Innocents by our Police"]

    #return a list of randomly generated names affect by police brutality a given percent of gen_subject calls
    percent_for_list = 25
    if random.randint(1,100) > percent_for_list:
        return random.choice(s)
    else:
        suffix = ["...","...and Many More","...and So Many More","...and Many Others","...and So Many Others"] 
        return "George Floyd, " + saytheirnames_sublist(4, []) + random.choice(suffix)


# Randomly generates the body of the email, follows structure of template and swaps out select words/phrases
def gen_body(src_name, dst_name, location):
    r = random.randint(0,100)
    if r < 50:
        return f'{gen_greeting(dst_name)}\t{inq.gen_message(location)}\n{gen_closing(src_name)}'
    else:
        return f'{gen_greeting(dst_name)}\t{dem.gen_message(src_name)}\n{gen_closing(src_name)}'

# Generates the greeting to the recipient of the email
def gen_greeting(person):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return f'{random.choice(s)} {person},\n\n'

# Prepends greeting statement to a user-generated message
def attach_greeting(person, body):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return f'{random.choice(s)} {person},\n\n{body}'


def gen_closing(name):
    c = [
            "Signed",
            "Sincerely",
            "From",
            "Regards",
            "Best",
    ]
    return f'\n{random.choice(c)},\n{name}'
