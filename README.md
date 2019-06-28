# nqueens
python app to solve the Nqueens problem

Build docker images
```bash
docker-compose up --build
```
Usage :

```bash
app.py <N> [options]
```
Options:
```
  -s       Store the results for the given N in the database
```

Solve the nqueens problem for N = 5

```bash
 docker-compose exec src python app.py 5
```

Solve the nqueens problem for N = 5 and store the results

```bash
 docker-compose exec src python app.py 5 -s
```

Run automatic tests

```bash
docker-compose exec src pytest -s
```