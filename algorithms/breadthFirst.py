from collections import deque


# Implementing the graph with a dictionary
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


 # Breadth-first algorithm
def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False


search("you")
