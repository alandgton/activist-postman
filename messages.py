import random
from email.message import EmailMessage
from email.mime.text import MIMEText
import mimetypes
import base64

"""
    Template credit: nomoreracistcops.github.io
    Additional demands from:
    https://secure.everyaction.com/eR7GA7oz70GL8doBq19LrA2
    https://docs.google.com/document/d/1V2l7bdg6QeqtqVWDr5HFzVzieiT0vg6jZASN6syBNyY/edit
"""

# Randomly generates the subject header of the email
def gen_subject():
    s = ["Human Rights Inquiry", "Thoughts of a Concerned Citizen", "In Light of Recent Human Rights Abuses", "The Need for Police Oversight", "The Need for Police Accountability", "The Failures of Modern Law Enforcement", "Law Enforcement Must Change", "The Voice of a Troubled Citizen", "The Need for Law Enforcement Reform", "Reforms to Law Enforcement Needed", "Your Duty as a Public Servant"]
    return random.choice(s)

# Randomly generates the body of the email, follows structure of template and swaps out select words/phrases
def gen_body(src_name, dst_name, location):
    return "%s\t%s\t%s\t%s" % (gen_greeting(dst_name), gen_intro(location), gen_curiosity(), gen_conclusion(src_name))

# Generates the greeting to the recipient of the email
def gen_greeting(person):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return "%s %s,\n\n" % (random.choice(s), person)

# Prepends greeting statement to a user-generated message
def attach_greeting(person, body):
    s = ["Dear", "Hello", "Greetings", "Hi"]
    return "%s %s,\n\n%s" % (random.choice(s), person, body)

# Generates the first sentence of the email.
def gen_intro(location):
    mess = ["in shambles", "in ruins", "a disaster", "a mess"]
    nominer = ["As a concerned resident of the US,", "I am a resident of the United States and", "As a concerned American,"]
    contact = ["getting in touch", "reaching out to you", "contacting you", "sending you this message"]
    adverb = ["deeply", "very", "greatly", "extremely", "especially", "immensely"]
    concern = ["troubled", "concerned", "disturbed"]
    reason = ["unfair treatment of African-Americans", "blatant racism against African-Americans"]
    scale = ["across the nation", "throughout the country", "nationwide", "across the country", "throughout the nation"]

    if random.randint(0,100) % 2:
        return "The current law enforcement system is %s. I am %s because I am %s %s by the %s by police %s.\n" % (random.choice(mess), random.choice(contact), random.choice(adverb), random.choice(concern), random.choice(reason), random.choice(scale))
    else:
        return "%s I am %s because I am %s %s by what I have seen recently regarding the %s by police %s.\n" % (random.choice(nominer), random.choice(contact), random.choice(adverb), random.choice(concern), random.choice(reason), random.choice(scale))

# Randomly generates a message rooted on human curiosity to expose the inadequacies of the current system
def gen_curiosity():
    verb = ["know", "inquire", "ask"]
    noun = ["safeguards", "policies", "provisions"]
    work = ["commitments", "efforts", "actions"]
    crime = ["incidents of racism", "violations of human rights", "occurrences of racism", "exploitations of human rights"]

    if random.randint(0,100) % 2:
        return "As a public servant, what %s will you make to protect black lives? In addition, what %s are in place to prevent %s by officers? %s" % (random.choice(work), random.choice(noun), random.choice(crime), gen_rhetorical_questions())
    else:
        return "I would like to %s what %s our police departments have in place to prevent %s by officers, and what %s you will make to protect black lives. %s\n" % (random.choice(verb), random.choice(noun), random.choice(crime), random.choice(work), gen_rhetorical_questions())

#{NOTE} I might want to change the ones that just say "incidents of racism" to stronger statements

# Randomly generates a relentless stream of hard-hitting rhetorical questions
def gen_rhetorical_questions():
    q = [
            "Are all officers required to wear body cameras to record their responses to calls on video?",
            "Do departments perform any form of anti-racism training for officers?",
            "How do internal affairs investigate and respond to reports of discrimination, racism, and unjust brutality?",
            "How can the general public be ensured that incidences of racist violence by police are not simply swept under the rug? In particular, how can I be sure that police officers are held accountable for their actions?",
            "Have you pledged to never again support increased police funding?",
            "Will you develop a plan for defunding law enforcement, and reallocate these funds to critical social services?",
            "Will you protect and expand current investment in community-led health and safety strategies, instead of investing in police?",
            "What have you done to compel local law enforcement agencies to immediately cease enacting violence on community members?",
            "How are you working on eliminating qualified immunity for police officers that has allowed too many incidents of police misconduct to disappear without consequence?",
            
    ]
    
    return ' '.join(random.sample(q, k=len(q)))


def gen_conclusion(name):
    noun = ["safeguards", "policies", "provisions"]
    verb = ["support", "want", "approve of"]
    place = ["law enforcement agencies", "police departments", "government institutions", "public institutions"]
    return "If these %s are not in place, then they certainly should be. %s I do not %s my local taxes being used to fund %s that perpetuate racism and violence. %s\n%s\n%s" % (random.choice(noun), gen_action(), random.choice(verb), random.choice(place), gen_interests(), gen_gratitude(), gen_closing(name))

def gen_action():
    bank = [
        "The status quo is failing us. Reforms to law enforcement agencies, along with the redirection of funds, must be enacted.",
        "The current system isn't working and changes must be made to how law is enforced and funded in this country.",
        "This issue is nothing new. The frequency of these incidents suggest that law enforcement is a force of violence, not public safety, in our country.",
    ]

    return random.choice(bank)

def gen_interests():
    preambles = [
            "Services that I would rather see funded include",
            "I would like to redirect funding to"
            "Areas that I would like funds to be redirected to include",
    ]
    i = [
            "mental health professionals,",
            "crisis de-escalators,",
            "support for victims of domestic abuse and addiction,",
            "public education,",
            "scientific research,",
            "increased social services for formerly incarcerated residents",
            "increased funding for nutrition and food access programs"
    ]
    return "Services that I would rather see funded include: %s to name only a few." % (' '.join(random.sample(i, k=len(i))))

def gen_gratitude():
    clauses = [
            "Thank you for your attention to my concerns.",
            "Thanks for taking the time to read my message.",
            "Your attention to my concerns are very appreciated.",
    ]
    finale = [
            "I hope to hear back from you soon.",
            "I'm hoping to hear back from you soon.",
            "I look forward to hearing back from you.",
    ]

    return "%s %s" % (random.choice(clauses), random.choice(finale))

def gen_closing(name):
    c = [
            "Signed",
            "Sincerely",
            "From",
            "Regards",
            "Best",
    ]
    return "\n%s,\n%s" % (random.choice(c), name)


def gen_messages(recv, subject, message, src_name, src_email, smtp=False):
    while recv:
        recipient = recv.pop()
        dst_name = recipient[0]
        location = recipient[1]
        dst_email = recipient[2]

        subject = subject if subject else gen_subject()
        body = attach_greeting(dst_name, message) if message else gen_body(src_name, dst_name, location)

        if smtp:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = src_email
            msg['To'] = dst_email


            msg.set_content(body)
        else:
              message = MIMEText(body)
              message['to'] = dst_email
              message['from'] = src_email
              message['subject'] = subject
              raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
              msg = {'raw': raw}
        yield msg
