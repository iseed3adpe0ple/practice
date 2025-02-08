movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def func1(name):
    for i in movies:
        if i["name"] == name:
            if i["imdb"] > 5.5:
                return True
    return False
print(func1("Exam"))

def filt(a):
    if a["imdb"] > 5.5:
        return True
    else:
        return False

def func2(a):
    b = list(filter(filt, a))
    return b
print(func2(movies))

def func3(name):
    for i in movies:
        if i["category"] == name:
            print(i)
func3("Romance")

def func4(a):
    g = 0
    t = 0
    for i in a:
        g += i['imdb']
        t += 1
    return g/t
print(func4(movies))

def func5(a, name):
    g = 0
    t = 0
    for i in a:
        if i['category'] == name:
            g += i['imdb']
            t += 1
    return g/t
print(func5(movies, "Romance"))