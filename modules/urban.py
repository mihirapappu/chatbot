from bs4 import BeautifulSoup
import lxml.html
import requests

# Urbandictionary.com
def urban(term):
    term = term.split("!urban ")[1]
    try:
        url = "http://urbandictionary.com/define.php?term={0}".format(term)
        resource = BeautifulSoup(requests.get(url).content, "lxml")
        content = resource.find('div', {"class":"meaning"})
        if content is None:
            content = "¯\\_(ツ)_/¯"
        else:
            content = resource.find('div', {"class":"meaning"}).text.strip()
        return content

    except Exception as e:
        print(e)
        return "Error Beep Boop"

# Dictionary.com
def define(term):
    term = term.split("!define ")[1]
    try:
        url = "https://dictionary.com/browse/{}".format(term)
        resource = BeautifulSoup(requests.get(url).content, "lxml")
        content = resource.find('div', {"class":"def-content"})
        example = resource.find('div', {"class":"def-inline-example"})

        if content is None:
            content = "Couldn't find {}.".format(term)
            example = ""
        else: 
            content = content.text.strip()
            if example is None:
                example = "No example available."
            else:
                example = example.text.strip()

        string = "{0}&+{1}".format(content, example)
        #print(string)
        return string

    except Exception as e:
        print(e)
        return e