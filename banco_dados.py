import sqlite3

con = sqlite3.connect('metas.db')
cursor = con.cursor()

'''
cursor.execute("""
INSERT INTO metas (tipo, nome, custo, prazo, finalidade)
VALUES(3, 'juca', 3000, 40, 'nadinha')
""")
'''

cursor.execute("""
SELECT * FROM metas;
""")

for linha in cursor.fetchall():
    print(linha)
con.close()