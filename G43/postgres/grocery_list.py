import psycopg2

groceries = [

	"apples",

	"bananas",

	"clemintines",

	"dill",

	"eggs",

	"flour",

	"granola",

	"honey",

	"ice cream",

	"juice",

	"ketchup",

	"lemon",

	"margarine",

	"onion",

	"potatoes",

	"rosmary",

	"salt",

	"thyme",

	"vinegar",

	"watermelon",

	"pears",

	"cucumbers",

	"garlic",

	"carrots",

	"pastries",

	"eggplants",

	"milk",

	"coffee",

	"tea",

	"rice",

	"noodles",

	"lentils",

	"sweet potatoes",

	"strawberries",

	"cranberries",

	"mangos",

	"pappers",

	"zuccinis",

	"lime",

	"broth",

	"mushrooms",

	"chicken",

	"beef",

	"pork",

	"fish",

	"cream",

	"paprika",

	"tumeric",

	"cinamon",

	"pumpkin",

	"basil",

	"tomatoes",

	"bread",

	"cake",

	"chocolate",

	"gum",

	"pinapple",

	"oranges",

	"lettuce",

	"cheese",

	"cilantro"

]



groceries = sorted(groceries)

conn_string = "host='localhost' port='30001' dbname='my_db' user='postgres' password ='123456'"

connection = psycopg2.connect(conn_string)

cursor = connection.cursor()



cursor.execute("CREATE TABLE groceries (id SERIAL PRIMARY KEY, name TEXT)")



for i in range(len(groceries)):

    cursor.execute("INSERT INTO groceries (name) VALUES (%s)", [groceries[i]])

    print("added ", groceries[i])





connection.commit()

connection.close()
