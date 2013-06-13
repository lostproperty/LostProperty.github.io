# LostProperty Company website

Lost Property marketing website.

## Development set up

### Backend

For backend development create a virtual environment then
```
python setup.py develop
python application.py
```
Site will be running on http://127.0.0.1:5000/

### Frontend

For frontend development we use SaSS with Bourbon Neat http://neat.bourbon.io/. To install
`sudo gem install sass`

To compile the css
```
cd lostproperty/static/sass
sass --watch main.scss:../css/main.css
```

## Deploying
