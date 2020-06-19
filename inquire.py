import random
"""
    Template credit: nomoreracistcops.github.io
    Additional demands from:
    https://secure.everyaction.com/eR7GA7oz70GL8doBq19LrA2
    https://docs.google.com/document/d/1V2l7bdg6QeqtqVWDr5HFzVzieiT0vg6jZASN6syBNyY/edit
"""

def gen_message(location):
    return f'{gen_intro(location)}\n\t{gen_curiosity()}\n\t{gen_conclusion()}'

# Generates the first sentence of the email.
def gen_intro(location):
    mess = ["in shambles", "in ruins", "a disaster", "a mess"]
    nominer = ["As a concerned US resident,", "I am a resident of the United States and", "As a concerned American,"]
    contact = ["getting in touch", "reaching out to you", "contacting you", "sending you this message"]
    adverb = ["deeply", "very", "greatly", "extremely", "especially", "immensely"]
    concern = ["troubled", "concerned", "disturbed", "distressed", "distraught", "worried", "devastated"]
    reason = ["unfair treatment of African-Americans", "blatant racism against African-Americans", "unjust treatment of African-Americans", "violence against African-Americans", "atrocities against the African-American community"]
    scale = ["across the nation", "throughout the country", "nationwide", "across the country", "throughout the nation"]

    r = random.randint(0,100)
    if r < 33:
        return f'The current law enforcement system is {random.choice(mess)}. I am {random.choice(contact)} because I am {random.choice(adverb)} {random.choice(concern)} by the {random.choice(reason)} by police {random.choice(scale)}.\n'
    elif r < 66:
        return f'I am {random.choice(contact)} because of the {random.choice(adverb)} disturbing cases of {random.choice(reason)} by law enforcement officers {random.choice(scale)}.\n'
    else:
        return f'{random.choice(nominer)} I am {random.choice(contact)} because I am {random.choice(adverb)} {random.choice(concern)} by what I have seen recently regarding the {random.choice(reason)} by police {random.choice(scale)}.\n'

# Randomly generates a message rooted on human curiosity to expose the inadequacies of the current system
def gen_curiosity():
    verb = ["know", "inquire", "ask"]
    noun = ["safeguards", "policies", "provisions"]
    work = ["commitments", "efforts", "actions"]
    crime = ["incidents of racism", "violations of human rights", "occurrences of racism", "exploitations of human rights"]

    if random.randint(0,100) % 2:
        return f'As a public servant, what {random.choice(work)} will you make to protect black lives? In addition, what {random.choice(noun)} are in place to prevent {random.choice(crime)} by officers? {gen_rhetorical_questions()}\n'
    else:
        return f'I would like to {random.choice(verb)} what {random.choice(noun)} our police departments have in place to prevent {random.choice(crime)} by officers, and what {random.choice(work)} you will make to protect black lives. {gen_rhetorical_questions()}\n'

#{NOTE} I want to change the ones that just say "incidents of racism" to stronger statements

# Randomly generates a relentless stream of hard-hitting rhetorical questions
def gen_rhetorical_questions():
    q1 = [
            "Are all officers required to wear body cameras to record their responses to calls on video?",
            "Do departments perform any form of anti-racism training for officers?",
            "How do internal affairs investigate and respond to reports of discrimination, racism, and unjust brutality?",
            "How can the general public be ensured that incidences of racist violence by police are not simply swept under the rug? In particular, how can I be sure that police officers are held accountable for their actions?",
    ]
    q2 = [
            "Will you develop a plan for defunding law enforcement, and reallocate these funds to critical social services?",
            "Will you protect and expand current investment in community-led health and safety strategies, instead of investing in police?",
            "What have you done to compel local law enforcement agencies to immediately cease enacting violence on community members?",
            "How are you working on eliminating qualified immunity for police officers that has allowed too many incidents of police misconduct to disappear without consequence?",
    ]
    
    return f"{' '.join(random.sample(q1,k=len(q1)))} {' '.join(random.sample(q2,k=len(q2)))}"

def gen_conclusion():
    noun = ["safeguards", "policies", "provisions"]
    adverb = ['certainly', 'definitely', 'absolutely', 'undoubtedly']
    verb = ["support", "want", "approve of"]
    place = ["law enforcement agencies", "police departments", "government institutions", "public institutions"]

    r = random.randint(0,100)
    if r % 2:
        return f'If these {random.choice(noun)} are not in place, then they {random.choice(adverb)} should be. {gen_action()} I do not {random.choice(verb)} my local taxes being used to fund {random.choice(place)} that perpetuate racism and violence. {gen_interests()}\n\n\t{gen_gratitude()}'
    else:
        return f'These {random.choice(noun)} must be put into place to protect American rights and lives. As a taxpayer, I do not {random.choice(verb)} my taxes being used to fund {random.choice(place)} that perpetuate institutional racism and violence. {gen_interests()}\n\n\t{gen_gratitude()}'

def gen_action():
    bank = [
        "The status quo is failing us. Reforms to law enforcement agencies, along with the redirection of funds, must be enacted.",
        "The current system isn't working and changes must be made to how law is enforced and funded in this country.",
        "This issue is nothing new. The frequency of these incidents suggest that law enforcement is a force of violence, not public safety, in our country.",
    ]

    return random.choice(bank)

def gen_interests():
    noun = [ 'Services', 'Programs']
    preamble = [
            f'{random.choice(noun)} that I would rather see funded include: ',
            'I would like to redirect funding to',
    ]
    return f'{random.choice(preamble)} {gen_services()} to name only a few.'

def gen_services():
    i = [
            "mental health professionals,",
            "crisis de-escalators,",
            "support for victims of domestic abuse and addiction,",
            "public education,",
            "scientific research,",
            "increased social services for formerly incarcerated residents",
            "increased funding for nutrition and food access programs"
    ]
    return ' '.join(random.sample(i, k=len(i)))

def gen_gratitude():
    clauses = [
            "Thank you for your attention to my concerns.",
            "Thanks for taking the time to read my message.",
            "Your attention to my concerns is very appreciated.",
    ]
    finale = [
            "I hope to hear back from you soon.",
            "I'm hoping to hear back from you soon.",
            "I look forward to hearing back from you.",
    ]

    return f'{random.choice(clauses)} {random.choice(finale)}'
