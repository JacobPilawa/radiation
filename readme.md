# Details for me!

1. After making edits, re-build the book with 

```
jupyter-book build radiation
```

2. This will create all the html files and such inside the _build directory. 

3. Git add, commit, push to github. 

4. In the root file of the book, run

```
ghp-import -n -p -f _build/html
```

to sync gh-pages branch with the main branch. 