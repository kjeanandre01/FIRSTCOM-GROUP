# Site web FIRST-COM GROUP — Prototype

Site vitrine statique (HTML / CSS / JavaScript), construit à partir des informations officielles
de la plaquette FIRST-COM GROUP. Aucun serveur n'est requis pour le consulter.

## Ouvrir le site

- **Rapide** : double-cliquez sur `index.html` (fonctionne en local, sans connexion).
- **Recommandé pour la démo** : déposez tout le dossier sur un hébergement statique
  (Netlify, Vercel, GitHub Pages, OVH, o2switch, etc.) — il n'y a aucune base de données
  ni backend, tous les fichiers sont statiques.
- Le formulaire de contact ouvre le client de messagerie de l'utilisateur (mailto) avec le
  message pré-rempli. Pour un vrai envoi silencieux depuis le serveur, il faudra brancher un
  service de formulaire (ex. Formspree, Resend, ou un petit backend) sur `js/main.js`
  (section « 10. Formulaire de contact »).

## Structure

```
index.html              Accueil
a-propos.html            À propos
services.html            Détail des 8 domaines d'expertise
realisations.html        Références clients + partenaires technologiques
contact.html             Formulaire de devis + coordonnées + carte
mentions-legales.html    Mentions légales (modèle à compléter)
confidentialite.html     Politique de confidentialité (modèle à compléter)
404.html                 Page d'erreur

css/style.css             Feuille de style compilée (générée par Tailwind CSS)
css/input.css             Source des styles personnalisés (design system)
js/main.js                Animations, menu mobile, formulaire, compteurs
images/                   Logo, photos et logos clients/partenaires extraits de la plaquette
tailwind.config.js        Palette, typographies, animations (design system)
build.py                  Générateur du site (voir « Régénérer le site »)
sitemap.xml, robots.txt, site.webmanifest   Fichiers techniques SEO / PWA
```

## Modifier un texte vous-même (méthode rapide, sans rien installer)

Tous les fichiers `.html` du dossier sont le site final : vous pouvez les ouvrir avec
n'importe quel éditeur de texte (Bloc-notes, VS Code, TextEdit...) et modifier directement
le texte entre les balises. Par exemple, pour changer une phrase de la page « À propos »,
ouvrez `a-propos.html`, cherchez (Ctrl+F) le texte à remplacer, modifiez-le, enregistrez,
et rafraîchissez la page dans votre navigateur.

Points d'attention :
- Ne touchez pas aux parties entre `< >` (les balises) — modifiez seulement le texte visible.
- Ce même texte peut apparaître à plusieurs endroits (ex. menu + pied de page) : vérifiez
  les autres pages si un intitulé doit changer partout (recherchez-le dans tous les fichiers).
- Si vous régénérez le site plus tard avec `build.py` (voir plus bas), vos modifications
  manuelles directement dans les `.html` seront écrasées : dans ce cas, reportez plutôt vos
  textes dans `build.py`.

## Régénérer le site après une modification dans build.py

Tout le contenu texte (services, valeurs, coordonnées, listes de clients...) est aussi
centralisé dans `build.py`, ce qui est plus sûr pour des changements durables. Pour changer
un texte, modifiez `build.py` puis régénérez :

```bash
python3 build.py                # régénère les fichiers .html (Python standard, aucune dépendance)
npm install                     # une seule fois, installe Tailwind CSS
npx tailwindcss -i ./css/input.css -o ./css/style.css --minify
```

## Ce qui est officiel, à confirmer, ou temporaire

Conformément à la consigne « ne pas inventer », voici l'origine de chaque type de contenu :

**Informations officielles (issues de la plaquette)**
- Nom, logo, couleurs de marque, slogan (« Notre expertise à votre service »)
- Adresse, téléphones, email, site web
- Les 8 domaines d'expertise et leurs listes de prestations (texte repris ou reformulé
  fidèlement à partir des bullet points de la plaquette)
- La liste des 19 références clients et des 10 partenaires technologiques (logos extraits
  de la plaquette en haute résolution)

**Contenu structurant proposé par le design (UX, pas des faits inventés)**
- Les titres de section, les textes d'accroche, la mise en récit « contexte client / notre
  réponse » de chaque service, les 5 étapes de la section « Notre approche », le
  regroupement des clients par secteur d'activité (secteurs publics et connus : Orange,
  MTN = télécoms, FAO/UNFPA/UNEP = agences onusiennes, etc.), la présentation par métiers
  de l'équipe terrain (câblage, fibre, énergie, sécurité — des rôles, pas des noms), les
  étapes types d'un projet et d'une demande de devis.
- Les chiffres affichés (8 domaines, 19+ références, 10 partenaires) sont des **comptages
  réels** des éléments de la plaquette — aucun chiffre commercial (ancienneté, nombre de
  projets, etc.) n'a été inventé.

**Contenu clairement signalé « À compléter » dans le site**
- Page « À propos » : présentation nominative de l'équipe dirigeante (photos, bios)
- Page « Références » : études de cas détaillées par projet (aucun faux projet créé)
- Pages légales : forme juridique, RCCM, hébergeur, durée de conservation des données

Aucun faux témoignage, aucune fausse certification, aucun faux chiffre d'ancienneté et
aucune fausse photo d'équipe ou de personne n'ont été ajoutés — les visuels utilisés sont
soit des photos réelles issues de la plaquette, soit des compositions graphiques (icônes,
dégradés) quand aucune photo réelle n'était disponible.

## Envoyer une démo à un client

Deux options simples, sans rien installer :

1. **Lien de démonstration cliquable (le plus rapide)** — Claude a publié un aperçu du site
   en ligne, avec une vraie navigation entre les pages. Depuis l'aperçu (menu de partage),
   activez le partage pour obtenir un lien que vous pouvez envoyer par email ou WhatsApp.
   Le client clique et découvre le site directement, sans rien installer.
2. **Mise en ligne réelle (pour une démo qui dure)** — Déposez tout ce dossier sur un
   hébergement statique gratuit comme Netlify (glisser-déposer sur app.netlify.com/drop)
   ou Vercel : vous obtenez une adresse `https://....netlify.app` fonctionnelle en une
   minute, sans configuration, que vous pouvez partager ou même relier à votre propre
   nom de domaine plus tard.

## Prochaines étapes suggérées

1. Fournir les informations légales exactes (mentions légales, RCCM, hébergeur).
2. Fournir 2 à 4 études de cas détaillées (contexte, solution, photos du chantier) pour la
   page Références.
3. Confirmer si les numéros de téléphone sont joignables sur WhatsApp (aucun bouton
   WhatsApp n'a été ajouté sans confirmation).
4. Fournir des photos de l'équipe / des locaux si vous souhaitez renforcer la page À propos.
5. Brancher le formulaire de contact à un service d'envoi d'e-mails côté serveur si un
   envoi silencieux (sans ouvrir le client mail du visiteur) est souhaité.
