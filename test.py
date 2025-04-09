import requests
for i in range(1, 26):
  for j in range(1, 6):
    r = requests.get(f"http://127.0.0.1:5000/USHistory/{i}/{j}")
    if r.status_code == 200:
      with open(f"test/ch{i}sec{j}.pdf", "wb") as f:
        f.write(r.content)
        print(f"Downloaded ch{i}sec{j}.pdf")
        f.close()
