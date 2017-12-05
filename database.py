import sqlite3

def main():
    db = sqlite3.connect("test.db")
    
    db.row_factory = sqlite3.Row
    
    db.execute("drop table if exists test")
    db.execute("create table test (index01 int, text01 text)")
    db.execute("insert into test (index01, text01) values (?, ?)", (1, "text01"))
    db.execute("insert into test (index01, text01) values (?, ?)", (2, "text02"))
    db.execute("insert into test (index01, text01) values (?, ?)", (3, "text03"))
    db.execute("insert into test (index01, text01) values (?, ?)", (4, "text04"))    
    
    db.commit()
    
    cursor = db.execute("select index01, text01 from test order by index01")
    for row in cursor:
        print(row["index01"], row["text01"])
        
if __name__ == "__main__": main()

