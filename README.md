# LostProperty Company website

Lost Property marketing website http://lostpropertyhq.com/.

## Development set up
### Backend
For backend development create a virtual environment then
```
python setup.py develop
python application.py
```
Site will be running on http://127.0.0.1:5000/ development should be done in the source branch.

### Adding portfolio pieces
Currently the portfolio is generated by adding items to the work.csv file. This
allows reuse across the homepage and the portfolio page. The homepage relies on
hardocded references to work items by name but the portfolio page automatically
renders every item added to the csv. It is expected that each portfolio piece
will have a corresponding image in `'/static/images/work/' + slug`.
Either a `.jpg` or a `.png` file extension will be detected.

### Frontend
For frontend development we use SaSS with Bourbon Neat http://neat.bourbon.io/. To install
`sudo gem install sass`

To compile the css
```
cd lostproperty/static/sass
sass --watch main.scss:../css/main.css
```

## Deploying
- Freeze the site via `python frozen.py`
- Push it on the remote (origin)
- Merge it on master via `git pull -s subtree origin source` (or `git merge -s subtree source` if you have set `git-pull` to rebase by default instead of merge)
