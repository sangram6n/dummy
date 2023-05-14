x = "hello world"

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    
    
if __name__ == "__main__":
    with open("file.txt","a") as f:
        m = f.write(x)
        f.close()



