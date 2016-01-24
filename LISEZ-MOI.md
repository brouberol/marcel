# Marcel, docker à la française

![logo](https://brouberol.github.io/marcel/images/logo/marcel-logo.png)

Marcel est une surcouche française qui se base sur l'interface de commande docker et qui a pour but de remplacer docker, afin de préparer le chemin pour le nouveau Système d'Exploitation souverain Français.

## Exemples

* ``docker run`` → ``marcel chauffe``
* ``docker images`` → ``marcel cederoms``
* ``docker login`` → ``marcel vos-papiers``
* ``docker logs`` → ``marcel bûches``
* ``docker pause`` → ``marcel rtt``
* ``docker suspend`` → ``marcel grève``
* ``docker tag`` → ``marcel graffiti``
* ``docker rmi`` → ``marcel rsa``

## RecetteÀMarcel

Pour des raisons évidentes, ``Dockerfile`` ne nous semble pas assez souverain, c'est pourquoi marcel utilise ``RecetteÀMarcel`` en lieu et place de ``Dockerfile``.

Pour que cela fonctionne, il vous suffit d'intégrer le fichier ``RecetteÀMarcel`` dans votre dossier courant où vous exécuterez ensuite ``marcel construis``. Et voilà, vous pouvez travailler !

## Comment contribuer ?

Pour commencer, merci de contribuer à la splendeur de le "french tech". Vous aurez besoin pour cela d'installer les dépendances dans vorte environnement virtuel:

```$ pip install -r requirements/dev.txt```

Puis, créez une branche à partir de la branche maître et publiez vos fonctionnalités (et tests ;). Vous pouvez vérifier si tout fonctionne en lançant le commande tox. Quand tous les test seront au vert, poussez votre fonctionnalité et créez une requète d'intégration. C'est tout!

## En quoi marcel est-il lié au système d'exploitation souverain français ?

Ce projet vise à fournir un socle technologique acceptable pour le Grand SE de France. Vous pouvez jetez un coup d'œil au [document officiel](http://www.assemblee-nationale.fr/14/amendements/3318/CION_LOIS/CL129.asp) pour constater à quelle point nous sommes enthousiastes et engagés dans le développement des technologies néccessaires au SE de demain, à l'instar de RedStar OS. Aidez-nous à rendre le monde meilleur en annihilant les SE non authorisés, comme ceux qui ont le culot d'intégrer des tehcnologies de chiffrement sans fournir au préalable la clé à la DST ou aux services secrets français, si volontaires pour défendre les intérèts et les droits de nos concitoyens.

## Remerciements
L'[idée originelle](https://github.com/docker/docker/issues/19396) revient à [@ndeloof](https://github.com/ndeloof).
Le logo a été conçu par [jkneb](https://github.com/jkneb).
