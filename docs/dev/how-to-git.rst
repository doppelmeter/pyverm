How to git?
===========

Make a new Feature
------------------

* create a feature branch, by checking out development branch to the feature branch

  ``git checkout -b myfeature development``

* make your developements

* when finished, merge features branch into development branch, by checking out development branche

  ``git checkout development``

  mergin feature branch to development branch **Important:** ``--no-ff``

  ``git merge --no-ff myfeature``

  delet your features branch

  ``git branch -d myfeature``

  push development branch to origin (GitHub)

  ``git push origin development``


Make a Release
------------------

* check out release branch from development branch -> name = release-X.X.X

  ``git checkout -b release-X.X.X development``

* increasing version number and commit this

  ``git commit -a -m "version number changed for release"``

* make other stuff for release preparation and commit it

* to finish the release, check out the master branch

  ``git checkout master``

  merge release branch to master branch

  ``git merge --no-ff release-1.2``

  make a tag

  ``git tag -a v1.2.1``

  push released master to origin (GitHub) with all tags

  ``git push origin master``

  **and** merge release with development branch

  ``git checkout development``

  merge release branch to master branch

  ``git merge --no-ff release-1.2``

  push released master to origin (GitHub) with all tags

  ``git push origin development``

* finally delete release branch

  ``git branch -d release-1.2``


Hot Fix Branch
------------------

https://nvie.com/posts/a-successful-git-branching-model/




