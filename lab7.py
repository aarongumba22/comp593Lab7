

def main():
    student_info = {
        'name': 'Aaron Gumba',
        'student_id': 10270770,
        'pizza_top': [
            'Mushrooms',
            'Pepperoni',
            'Red Pepper',
        ],
        'Movies': [
            {'Title': 'Real Steel',
             'Genre': 'Action',
             },
            {'Title': 'Home Alone',
             'Genre': 'Comedy',

             }

        ]
    }
   
    #append new movie to the end of the list 
    new_movie = {'Title' : 'Resident Evil', 'Genre':' Horror'}
    student_info ['Movies'].append(new_movie)
    

    #append new pizza in tuple 
    new_toppings = ["Pineaple","Fennel"]
    add_pizza(student_info,new_toppings)

    print_info(student_info)

def add_pizza(person_info, pizza_top):
    """adds new pizza toppings and then appends it in the student info data structure that sorts the toppings
    and transform into tuple"""
    
    for toppings in pizza_top:
        person_info['pizza_top'].append(toppings)

    tuple_mode= person_info['pizza_top'].sort()
    return tuple_mode
    tuple(tuple_mode)



def print_info(person_info):
    name = person_info ['name']
    id_num = person_info['student_id']
    
    #toppings = person_info ['pizza_top']
    


    print("Hi Joe, my name is ",name, "and my student Id is",str(id_num) +".")
    #print("My ideal pizza has", toppings)
    ingre= []
    for i in person_info['pizza_top']:

        bob=i 
        ingre.append(bob)
    print("My ideal pizza has" ,ingre[0],ingre[1],ingre[2],ingre[3],ingre[4] ,"and",ingre[-1] +".")



    move_genre= []
    for i in person_info['Movies']:

        gen= i['Genre']
        move_genre.append(gen)
    
    print("I like to watch", move_genre[0],move_genre[1]+move_genre[2] ,"movies.")
    
    move_title=[]
    for i in person_info['Movies']:
    
        title= i['Title']
        move_title.append(title)
    print("Some of my favourite are", move_title[0],move_title[1],move_title[2]+".")

        

   
        
    #print("I like to watch", movies_genre, "movies.")
    #print("Some of my favourites", movies_title, "!")
    



main()