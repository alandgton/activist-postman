import random

"""
def ___________():
My name is [Name], and I am reaching out to demand that the Mayor and City Council redirect money away from the police department and invest into community resources.

def ___________():
It has been proven time and time again that police brutality is a systemic issue and has racially targeted Black and Brown people for hundreds of years.


"""
def gen_message(name):
    return f"\t{gen_thesis(name)} {gen_elaborate()} {gen_more()}\n\n\t{gen_redirect()}\n\n\t{gen_final()}"

def gen_thesis(name):
    n = [ "My name is", "I'm" ]
    contact = ["getting in touch", "reaching out", "contacting you", "sending you this message"]
    verb = ["demand for", "ask for", "request for"]
    money = ["funds", "public funds", "taxpayer money"]
    scale = ["community", "local"]
    service = ["programs", "services", "resources"]

    return f'{random.choice(n)} {name} and I am {random.choice(contact)} to {random.choice(verb)} the redirection of {random.choice(money)} away from the police department and into other {random.choice(scale)} {random.choice(service)}.'

def gen_elaborate():
    h = ["It has been proven time and time again", "History has shown", "Recent events have shown"]
    adjective = ["an institutional", "a systemic"]
    noun = ["issue", "problem"]
    adverb = ["disproportionately", "unfairly", "unevenly", "unequally"]
    verb = ["targets", "affects", "victimizes", "preys upon"]
    p = ["Black and Brown people", "the African-American and Latinx communities"]
    scale = ["across the nation", "throughout the country", "nationwide", "across the country", "throughout the nation"]

    return f"{random.choice(h)} that police brutality is {random.choice(adjective)} {random.choice(noun)} that {random.choice(adverb)} {random.choice(verb)} {random.choice(p)} {random.choice(scale)}."

def gen_more():
     i = ["This is unacceptable.", "This is intolerable.", "The status quo is failing us.", "The current system is failing us.", "The status quo needs to be reformed.", "The law enforcement system needs to be reformed."]
     n = ["desire", "need", "yearning", "craving"]
     a = ["systemic", "structural", "institutional"]
     c = ["change", "reform"]
     p = ["policing", "law enforcement"]
     r = ["manifested in", "resulted in", "brought about"]
     u = ["public unrest", "civil unrest", "protests and riots across the nation"]

     return f"{random.choice(i)} At this time, the {random.choice(n)} for {random.choice(a)} {random.choice(c)} to {random.choice(p)} has {random.choice(r)} {random.choice(u)}."

def gen_suggest():
     f = ["funds", "resources", "energy", "money"]
     a = ["must", "should", "need to"]
     v = ["redirected", "diverted"]
     s = ["services", "programs", "resources"]
     r = ["reflect", "support"]
     n = ["needs", "concerns", "desires"]

     return f"The city's {random.choice(f)} {random.choice(a)} be {random.choice(v)} to {random.choice(s)} that {random.choice(r)} the {random.choice(n)} of our community: {gen_interests()}."

def gen_turnpoint():
	unacceptable = ["unacceptable", "indefensible", "inexcusable"]
	change = ["systemic change to policing", "upheaval of current methods when it comes to policing", "eradication of racism in policing", "fundamental change to policing"]
	covid = ["COVID19", "coronavirus", "the global pandemic"]
	community = ["preserving community resources", "protecting community assets", "bolstering community healthcare"]
	bolstering = ["excessively bolstering", "unnecessarily strengthening","toxically reinforcing", "disproportionately aiding"]

	r = random.randint(0,100)
	if r < 33:
		return f'This is {random.choice(unacceptable)}. At this time Black people and their allies are demanding {random.choice(change)}, and in light of {random.choice(covid)}, we need to restructure funding to focus on {random.choice(community)} instead of {random.choice(bolstering)} the police.\n'
	elif r < 66:
		return f'In this current political climate, while Black people and their allies are demanding {random.choice(change)}, this is {random.choice(unacceptable)}. We need to examine funding and ensure that it is {random.choice(community)}, as opposed to {random.choice(bolstering)} the police.\n'
	else:
		return f'We cannot continue to keep {random.choice(bolstering)} the police. The treatment of Black people in this country is {random.choice(unacceptable)}, and they alongside with their allies are demanding {random.choice(change)}. Especially given the extenuating circumstance of {random.choice(covid)}, we need to restructure funding to focus on {random.choice(community)}.\n'


def gen_redirect():
	programs = ["quality housing for all", "educational enrichment", "good jobs", "free and quality public transportation", "universal access to healthy food", "climate justice", "mental healthcare"]
	needs = ["needs", "wants", "desires", "goals", "demands", "requirements"]
	people = ["our community", "our society", "the people that make up our community", "the members of our community"]
	redirect = ["redirect", "divert", "channel", "pivot"]
	deserving = ["deserving", "worthy", "warranted", "commendable"]

	r = random.randint(0,100)
	if r < 50:
		return f'The budget of this city should be {random.choice(redirect)}ed into programs that support the {random.choice(needs)} of {random.choice(people)}: {", ".join(random.sample(programs, len(programs)-3))}, and small business resources amongst others.'
	else:
            return f'There are many programs that the city could invest in that would greatly benefit {random.choice(people)} like: {", ".join(random.sample(programs, len(programs)-3))} (only to name a few). You have the obligation to {random.choice(redirect)} the funds of your city from the police to a more {random.choice(deserving)} cause.' 


def gen_final():
	nominer = ["As an elected official,", "Being that you have been elected to office,", "You are an elected official and", "As a public servant,", "You are a public servant and"]
	choice = ["duty", "obligation", "responsibility", "requirement"]
	wellbeing = ["benefiting all of", "serving", "helping", "taking care of", "assisting"]
	people = ["your constituents", "those who elected you", "the people who put you in office", "your voters", "the members in your community"]
	protection = ["overprotecting", "unfairly aiding", "shielding", "protecting"]
	voices = ["make our voices heard", "speak out against injustice", "make our voices known", "speak up for our black community", "speak up until change is delivered"]
	seek = ["seek", "intend", "toil", "make it a priority"]
	
	r = random.randint(0,100)
	if r < 33:
	    return f'You should understand that {random.choice(protection)} the police is no longer an option. We will continue to {random.choice(voices)}, and you should {random.choice(seek)} to take action that benfits us. We are {random.choice(people)} and we deserve to be heard.'
	elif r < 66:
	    return f'It is our {random.choice(choice)} to {random.choice(voices)} and it is yours to listen. You should {random.choice(seek)} to help {random.choice(people)}, instead of {random.choice(protection)} the police.'
	else:
		return f'{random.choice(nominer)} you have a {random.choice(choice)} to listen to your community, and focus on {random.choice(wellbeing)} {random.choice(people)} rather than {random.choice(protection)} the police. We will continue to {random.choice(voices)}.'
