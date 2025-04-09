import os

os.chdir("books")
for i in range(21):
  i += 5
  i = "%02d" % i
  os.system(f"wget https://icomets.org/ush-textbook/ch{i}.pdf")
  print(f"Downloaded ch{i}.pdf")
