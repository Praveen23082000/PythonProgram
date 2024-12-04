f=open("C:\\Users\\praveen\\Desktop\\python\\DATA FILES\\frame work.txt","a")

frame_works=["wordpress","spring boot"]
for fw in frame_works:
    f.write(fw+"\n")
f.close()