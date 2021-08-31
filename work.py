import requests
import json
from tkinter import *
import string


run = True
while run:

    deadUser = input()


    def run_query(query):
        request = requests.get(f'https://api.github.com/users/{str(deadUser)}')
        if request.status_code == 200:
            return request.json()


    query = """{
      name
    }"""


    def run_query1(query1):
        request = requests.get(f'https://api.github.com/users/{str(deadUser)}/repos')
        if request.status_code == 200:
            return request.json()


    query1 = """{
      name
    }"""
    def server():
        try:
            result = run_query(query)
            name = result["name"]
            result1 = run_query1(query1)
            repo = result1
            v = open('repo.json', 'w')
            v.close()
            g = open('repo.json', 'a+')
            h = "[\n"
            g.write(h)
            g.close()
            j = open('repo.json', 'a+')
            lines = " {\n" + "  " + '"name": ' + '"' + f"{str(name)}" + '"' + ","
            j.write(lines)
            j.close()
            t = open('repo.json', 'a+')
            one = " \n" + "  " + '"repo": ['
            t.write(one)
            t.close()
            for user in repo:
                a = user["name"]
                j = open('repo.json', 'a+')
                lines = '\n    {\n' + '     "name2": "' + f"{str(a)}" + '"\n    },'
                j.write(lines)
                j.close()
            k = open('repo.json', 'a+')
            lines = '\n    {\n' + '     "name2": "it was a last one"\n' + '    }' + "\n  ]\n" + " }\n"
            k.write(lines)
            k.close()
            f = open('repo.json', 'a+')
            h = "]"
            f.write(h)
            f.close()
        except:
            v = open('repo.json', 'w')
            v.close()
            g = open('repo.json', 'a+')
            h = "[\n"
            g.write(h)
            g.close()
            j = open('repo.json', 'a+')
            lines = " {\n" + "  " + '"name": ' + '"' + "not a user" + '"' + ","
            j.write(lines)
            j.close()
            t = open('repo.json', 'a+')
            one = " \n" + "  " + '"repo": "'
            t.write(one)
            t.close()
            k = open('repo.json', 'a+')
            lines = '"\n' + " }\n"
            k.write(lines)
            k.close()
            f = open('repo.json', 'a+')
            h = "]"
            f.write(h)
            f.close()
    server()
    def all():
        query = """query{
          getRepo{
            name
            repo
          }
        }
        """
        try:
            url = 'http://127.0.0.1:8000/'
            r = requests.post(url, json={'query': query})
            json_data = json.loads(r.text)
            name = json_data['data']['getRepo']
            for name in name:
                a = name['name']
                print(a)
            repo = json_data['data']['getRepo']
            for repo in repo:
                a = repo['repo']
                b = a.split("[")[1]
                c = b.split("]")[0]
                v = c.replace("'name2': ", "")
                g = v.replace("'}", "")
                n = g.replace("{'", "")
                j = n.replace(", ", "\n")
                print(j)
        except:
            print("something went wrong")
    all()