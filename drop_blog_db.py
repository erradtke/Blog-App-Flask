# create blog db

import sqlite3

with sqlite3.connect("blog.db") as connection:

	c = connection.cursor()

	c.execute("""DROP TABLE posts""")