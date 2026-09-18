# -*- coding: utf-8 -*-
"""
Générateur statique du site FIRST-COM GROUP.
Assemble chaque page HTML à partir de composants partagés (head, header, footer)
et du contenu spécifique à chaque page, puis écrit les fichiers .html finaux
à la racine du projet. Aucune dépendance : Python standard uniquement.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://www.firstcom-group.net"

# ---------------------------------------------------------------------------
# Données de référence (issues exclusivement de la plaquette officielle)
# ---------------------------------------------------------------------------

PHONES = ["27 23 29 71 54", "07 59 63 39 54", "05 76 22 52 16"]
PHONES_TEL = ["+22527232971 54".replace(" ", ""), "+22507596339 54".replace(" ", ""), "+22505762252 16".replace(" ", "")]
EMAIL = "Info@firstcom-group.net"
ADDRESS_LINES = ["Attécoubé, Avenue de Locodjro", "Quartier Jérusalem — Abidjan, Côte d'Ivoire"]
WEBSITE = "www.Firstcom-group.net"

SERVICES = [
    {
        "id": "cablage-reseau",
        "short": "Câblage réseau",
        "title": "Câblage réseaux informatique & téléphonique",
        "icon": "cable",
        "desc": "Étude, déploiement et livraison clé en main de votre infrastructure de câblage informatique et téléphonique.",
        "bullets": ["Étude", "Déploiement", "Livraison clé en main"],
        "image": "images/services/cablage-reseau.webp",
        "problem": "Un réseau mal conçu ou vieillissant ralentit vos équipes, multiplie les pannes et complique chaque nouvel aménagement de bureau.",
        "solution": "Nous étudions votre site, concevons une architecture de câblage structuré adaptée à vos usages actuels et futurs, puis la déployons et la livrons clé en main.",
    },
    {
        "id": "fibre-optique",
        "short": "Fibre optique",
        "title": "Réseau fibre optique",
        "icon": "fiber",
        "desc": "Déploiement FTTH B2B/B2C, interconnexion de sites distants en backbone ou point à point.",
        "bullets": ["Étude et déploiement FTTH (B2B/B2C)", "Cluster / désaturation / extension", "Interconnexion de sites distants (Backbone, P2P)"],
        "image": "images/services/fibre-optique.webp",
        "problem": "Vos sites sont éloignés, votre réseau fibre sature ou vous devez raccorder de nouveaux clients rapidement, sans interrompre le service existant.",
        "solution": "Nous étudions et déployons vos réseaux FTTH, gérons la désaturation et l'extension de vos clusters, et interconnectons vos sites distants en liaison backbone ou point à point.",
    },
    {
        "id": "reseau-ip-wifi",
        "short": "Réseau IP & sans fil",
        "title": "Réseau IP & sans fil",
        "icon": "wifi",
        "desc": "Étude de couverture Wi-Fi, déploiement de réseaux IP et interconnexion de sites distants.",
        "bullets": ["Étude de couverture Wi-Fi", "Déploiement des réseaux IP et Wi-Fi", "Interconnexion des sites distants"],
        "image": "images/services/reseau-ip-wifi.webp",
        "problem": "Des zones blanches, un Wi-Fi saturé aux heures de pointe ou des sites distants qui peinent à communiquer entre eux freinent votre activité.",
        "solution": "Nous réalisons l'étude de couverture, déployons vos réseaux IP et Wi-Fi et interconnectons vos sites distants pour une connectivité fiable, partout sur votre site.",
    },
    {
        "id": "data-center",
        "short": "Data Center",
        "title": "Data Center",
        "icon": "server",
        "desc": "Étude, conception et déploiement de votre data center, livré clé en main.",
        "bullets": ["Étude et conception", "Déploiement", "Livraison clé en main"],
        "image": "images/services/data-center.webp",
        "problem": "Héberger vos serveurs et vos données critiques exige une salle technique fiable, sécurisée et dimensionnée pour durer.",
        "solution": "Nous concevons et déployons votre data center — architecture, câblage, énergie et sécurité — et vous le livrons clé en main, prêt à l'exploitation.",
    },
    {
        "id": "energie",
        "short": "Énergie",
        "title": "Énergie",
        "icon": "bolt",
        "desc": "Étude et déploiement de réseaux BT, MT et HT ; fourniture et installation de groupes électrogènes, onduleurs et stabilisateurs.",
        "bullets": ["Étude et déploiement de réseaux BT, MT et HT", "Groupes électrogènes et onduleurs", "Ateliers d'énergie", "Stabilisateurs, etc."],
        "image": "images/services/energie.webp",
        "problem": "Une coupure de courant ou une alimentation instable peut interrompre votre production, endommager vos équipements ou couper vos communications au pire moment.",
        "solution": "Nous étudions et déployons vos réseaux basse, moyenne et haute tension, et fournissons vos équipements d'énergie — groupes électrogènes, onduleurs, ateliers d'énergie et stabilisateurs.",
    },
    {
        "id": "supervision-fo",
        "short": "Supervision fibre optique",
        "title": "Supervision fibre optique",
        "icon": "radar",
        "desc": "Géolocalisation des défaillances, alertes SMS/e-mail, analyse OTDR/IOLM et supervision du trafic réseau.",
        "bullets": [
            "Géolocalisation et notification des défaillances fibres par mail et/ou SMS",
            "Analyse des tests OTDR/IOLM",
            "Supervision des liens fibre actifs ou passifs",
            "Supervision monitoring du trafic réseau",
            "Vente et déploiement d'équipements",
        ],
        "image": "images/services/supervision-fo.webp",
        "problem": "Une coupure fibre non détectée immédiatement se traduit par des heures d'indisponibilité pour vos clients ou vos équipes, et par un temps précieux perdu à localiser le défaut.",
        "solution": "Nous mettons en place la géolocalisation et la notification automatique des défaillances par SMS et e-mail, l'analyse des tests OTDR/IOLM et la supervision continue de vos liens fibre et de votre trafic réseau.",
    },
    {
        "id": "metrologie",
        "short": "Métrologie",
        "title": "Métrologie",
        "icon": "gauge",
        "desc": "Installation de capteurs, mesure automatique de citerne à gaz et carburant, alertes de niveaux critiques.",
        "bullets": [
            "Étude et installation des capteurs",
            "Mesure automatique de citerne à gaz et carburant",
            "Reporting de données",
            "Analyse et vérification des données",
            "Alerte des niveaux critiques",
            "Suivi en direct du niveau de chargement des cuves",
        ],
        "image": "images/services/metrologie.webp",
        "problem": "Sans mesure fiable ni alerte automatique, une citerne de gaz ou de carburant qui atteint un niveau critique peut passer inaperçue jusqu'à la rupture.",
        "solution": "Nous installons des capteurs adaptés, automatisons la mesure de vos citernes, générons des rapports et déclenchons des alertes dès qu'un niveau critique est atteint, avec un suivi en direct du chargement.",
    },
    {
        "id": "securite",
        "short": "Sécurité",
        "title": "Sécurité",
        "icon": "shield",
        "desc": "Vidéosurveillance, contrôle d'accès et systèmes de sécurité incendie, intrusion et inondation.",
        "bullets": ["Vidéosurveillance", "Contrôle d'accès", "Système de sécurité incendie", "Système de sécurité intrusion", "Système de sécurité inondation"],
        "image": "images/services/securite.webp",
        "problem": "Protéger vos locaux, vos équipes et vos biens exige plus que des caméras : il faut détecter, alerter et pouvoir réagir à temps.",
        "solution": "Nous déployons vidéosurveillance et contrôle d'accès, ainsi que des systèmes de détection incendie, intrusion et inondation, pour une sécurité électronique cohérente sur l'ensemble de votre site.",
    },
]

CLIENTS = [
    ("orange", "Orange", "Télécommunications"),
    ("mtn", "MTN", "Télécommunications"),
    ("moov-africa", "Moov Africa", "Télécommunications"),
    ("artci", "ARTCI", "Régulation télécoms"),
    ("ciprel", "CIPREL", "Production d'électricité"),
    ("sndi", "SNDI", "Développement informatique"),
    ("fao", "FAO", "Organisation des Nations Unies"),
    ("unfpa", "UNFPA", "Organisation des Nations Unies"),
    ("unep", "UNEP / PNUE", "Programme des Nations Unies"),
    ("douanes-ivoiriennes", "Douanes Ivoiriennes", "Administration publique"),
    ("ubipharm", "UbiPharm Côte d'Ivoire", "Distribution pharmaceutique"),
    ("tedis", "TEDIS Pharma CI", "Distribution pharmaceutique"),
    ("la-loyale-vie", "La Loyale Vie", "Assurance"),
    ("fidra", "FiDRA", "Retraite & prévoyance"),
    ("bouygues", "Bouygues Énergies & Services", "Énergie & services"),
    ("abidjan-terminal", "Abidjan Terminal", "Logistique portuaire"),
    ("saco", "SACO — Société Africaine de Cacao", "Agro-industrie"),
    ("camusat", "Camusat", "Infrastructures télécoms"),
    ("ofi", "OFI", "Négoce & agro-industrie"),
]

PARTNERS = [
    ("viavi", "VIAVI Solutions", "Instruments de test et de mesure fibre optique", True),
    ("telenco-networks", "Telenco Networks", "Solutions et composants fibre optique", True),
    ("hikvision", "HIKVISION", "Vidéosurveillance et sécurité électronique", True),
    ("exfo", "EXFO", "Test, mesure et supervision de réseaux fibre", True),
    ("triton", "TRITON", "Équipements et systèmes techniques", True),
    ("airfiber", "airFiber", "Solutions de transmission sans fil", False),
    ("legrand", "Legrand", "Infrastructures électriques et numériques du bâtiment", True),
    ("acome", "ACOME", "Câbles et solutions fibre optique", False),
    ("schneider-electric", "Schneider Electric", "Gestion de l'énergie et automatismes", True),
    ("sensile-technologies", "Sensile Technologies", "Solutions IoT de télémétrie et métrologie", True),
]

APPROACH = [
    ("01", "Analyse", "Nous écoutons votre besoin et réalisons un audit de votre environnement technique, sur site ou à distance."),
    ("02", "Conseil & étude", "Nous concevons la solution adaptée à votre contexte : réseau, fibre, énergie, sécurité ou métrologie."),
    ("03", "Déploiement", "Nos équipes techniques installent et mettent en œuvre la solution retenue, dans le respect de vos contraintes d'exploitation."),
    ("04", "Configuration", "Nous configurons, testons et validons chaque équipement avant la mise en service."),
    ("05", "Accompagnement", "Nous assurons le suivi, la supervision et le support de votre installation dans la durée."),
]

WHY_US = [
    ("layers", "Une expertise multi-domaines intégrée", "Réseau, fibre optique, énergie, sécurité, data center et métrologie : un seul interlocuteur pour l'ensemble de votre infrastructure technique."),
    ("check-badge", "Un accompagnement de bout en bout", "Étude, déploiement et livraison clé en main sur chaque projet, du diagnostic initial à la mise en service."),
    ("radar", "Supervision et réactivité", "Géolocalisation des défaillances fibre, alertes SMS et e-mail, monitoring continu de vos réseaux et de vos installations critiques."),
    ("cpu", "Des équipements de marques reconnues", "Nous déployons des solutions signées HIKVISION, Schneider Electric, Legrand, VIAVI, EXFO et nos autres partenaires technologiques."),
    ("building", "Une clientèle exigeante et diversifiée", "Télécommunications, énergie, institutions publiques, organisations internationales, santé et agro-industrie nous font confiance."),
    ("map-pin", "Une équipe basée à Abidjan", "Basés à Attécoubé, nous intervenons au plus près de vos sites, en Côte d'Ivoire."),
]

# ---------------------------------------------------------------------------
# Icônes (SVG en ligne, dessinées à la main — pas de dépendance externe)
# ---------------------------------------------------------------------------

ICONS = {
    "cable": '<path d="M7 17 17 7M7 17c-1.5 1.5-4 1.5-5-.5s0-3.5 1-4.5l3-3c1-1 3-1.5 4.5 0M17 7c1.5-1.5 4-1.5 5 .5s0 3.5-1 4.5l-3 3c-1 1-3 1.5-4.5 0M9.5 14.5l-1-1M14.5 9.5l-1-1"/>',
    "fiber": '<path d="M3 12h4M17 12h4M8 12a4 4 0 0 1 4-4c2 0 3 1.5 4 3s2 3 4 3M8 12a4 4 0 0 0 4 4c2 0 3-1.5 4-3s2-3 4-3"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/>',
    "wifi": '<path d="M5 8.5a11 11 0 0 1 14 0M7.8 11.8a7 7 0 0 1 8.4 0M10.6 15a3 3 0 0 1 2.8 0"/><circle cx="12" cy="18" r="1.1" fill="currentColor" stroke="none"/>',
    "server": '<rect x="4" y="4" width="16" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="16" height="6.5" rx="1.5"/><path d="M7.5 7.25h.01M7.5 16.75h.01" stroke-width="2.4"/>',
    "bolt": '<path d="M13 3 5 13.5h5.5L11 21l8-11h-5.5z"/>',
    "radar": '<path d="M3.5 12h4l1.8-5.5L12.8 17l1.7-5h4"/>',
    "gauge": '<path d="M4.5 16.5a7.5 7.5 0 1 1 15 0"/><path d="M12 16.5 15.3 11"/><circle cx="12" cy="16.5" r="1.3" fill="currentColor" stroke="none"/><path d="M4.5 16.5h-1M20.5 16.5h-1M7 10l-.7-.7M17 10l.7-.7"/>',
    "shield": '<path d="M12 3.5 19 6.3v5.4c0 4.6-3 7.9-7 8.8-4-.9-7-4.2-7-8.8V6.3z"/><path d="m9 12 2 2 4-4.3"/>',
    "layers": '<path d="M12 3.5 20.5 8 12 12.5 3.5 8z"/><path d="m4.5 12 7.5 4.2L19.5 12M4.5 16l7.5 4.2 7.5-4.2"/>',
    "check-badge": '<path d="M12 3.2 14.4 5l3.1-.3.9 3 2.4 1.9-1.3 2.9 1.3 2.9-2.4 1.9-.9 3-3.1-.3L12 22l-2.4-1.9-3.1.3-.9-3-2.4-1.9 1.3-2.9-1.3-2.9 2.4-1.9.9-3 3.1.3z"/><path d="m8.5 12.3 2.3 2.3 4.7-4.9"/>',
    "cpu": '<rect x="7" y="7" width="10" height="10" rx="1.4"/><rect x="10" y="10" width="4" height="4" rx="0.6"/><path d="M12 3v2.3M12 18.7V21M3 12h2.3M18.7 12H21M6 6l1.6 1.6M16.4 16.4 18 18M18 6l-1.6 1.6M7.6 16.4 6 18"/>',
    "building": '<rect x="4" y="9.5" width="7" height="10.5"/><rect x="13" y="4" width="7" height="16"/><path d="M6.5 12.5h2M6.5 15.5h2M6.5 18h2M15.5 7h2M15.5 10h2M15.5 13h2M15.5 16h2"/>',
    "map-pin": '<path d="M12 21s7-6.1 7-11.5A7 7 0 0 0 5 9.5C5 14.9 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.4"/>',
    "phone": '<path d="M6.6 3.5 9.3 8l-2 2c.9 2.4 2.8 4.3 5.2 5.2l2-2 4.5 2.7v3a2 2 0 0 1-2.2 2C10.1 20.4 3.6 13.9 3.6 6.2a2 2 0 0 1 2-2Z"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="1.8"/><path d="m4.5 7 7.5 6 7.5-6"/>',
    "arrow-right": '<path d="M4.5 12h14.5M13.5 6.5 19 12l-5.5 5.5"/>',
    "arrow-up-right": '<path d="M7 17 17 7M9 7h8v8"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "chevron-left": '<path d="m14.5 6-6 6 6 6"/>',
    "chevron-right": '<path d="m9.5 6 6 6-6 6"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7"/>',
    "clock": '<circle cx="12" cy="12" r="8.3"/><path d="M12 7.5V12l3 2"/>',
    "search-check": '<circle cx="10.5" cy="10.5" r="6.3"/><path d="m20 20-4.4-4.4M8 10.6l1.6 1.6L13.2 8"/>',
    "route": '<circle cx="6" cy="18" r="2.2"/><circle cx="18" cy="6" r="2.2"/><path d="M8 18h5a3 3 0 0 0 3-3v-1a3 3 0 0 1 3-3h-.2"/>',
    "settings": '<circle cx="12" cy="12" r="2.8"/><path d="M19.4 13.5c.06-.5.1-1 .1-1.5s-.04-1-.1-1.5l2-1.5-2-3.5-2.3.9a7.4 7.4 0 0 0-2.6-1.5L14 2h-4l-.5 2.4a7.4 7.4 0 0 0-2.6 1.5l-2.3-.9-2 3.5 2 1.5c-.06.5-.1 1-.1 1.5s.04 1 .1 1.5l-2 1.5 2 3.5 2.3-.9c.76.66 1.64 1.17 2.6 1.5L10 22h4l.5-2.4a7.4 7.4 0 0 0 2.6-1.5l2.3.9 2-3.5z"/>',
    "life-buoy": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.3"/><path d="m7 7 2.8 2.8M17 7l-2.8 2.8M7 17l2.8-2.8M17 17l-2.8-2.8"/>',
    "quote": '<path d="M9.5 7.5C6.5 8.7 5 10.8 5 13.5A3.5 3.5 0 1 0 8.5 17c0-2-1-3.2-3-3.7.3-1.6 1.4-2.8 3.3-3.5zM18 7.5c-3 1.2-4.5 3.3-4.5 6a3.5 3.5 0 1 0 3.5 3.5c0-2-1-3.2-3-3.7.3-1.6 1.4-2.8 3.3-3.5z"/>',
    "sparkle": '<path d="M12 3.5 13.4 9l5.6 1.4L13.4 12l-1.4 5.5L10.6 12 5 10.4 10.6 9z"/>',
    "globe": '<circle cx="12" cy="12" r="8.3"/><path d="M3.7 12h16.6M12 3.7c2.2 2.3 3.4 5.2 3.4 8.3s-1.2 6-3.4 8.3c-2.2-2.3-3.4-5.2-3.4-8.3S9.8 6 12 3.7Z"/>',
    "play": '<path d="M8 6.5v11l9-5.5z"/>',
}

def icon(name, cls="w-6 h-6"):
    body = ICONS.get(name, ICONS["sparkle"])
    return ('<svg class="' + cls + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + body + '</svg>')


# ---------------------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------------------

NAV_ITEMS = [
    ("index.html", "Accueil"),
    ("a-propos.html", "À propos"),
    ("services.html", "Services"),
    ("realisations.html", "Références"),
    ("projets.html", "Réalisation"),
    ("contact.html", "Contact"),
]


def head(title, description, path, og_image="images/meta/og-image.jpg"):
    canonical = SITE_URL + "/" + path
    return """<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<link rel="canonical" href="{canonical}" />
<meta name="theme-color" content="#0a1a44" />
<meta name="robots" content="index, follow" />

<link rel="icon" href="images/favicon/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="images/favicon/favicon-32.png" />
<link rel="icon" type="image/png" sizes="192x192" href="images/favicon/favicon-192.png" />
<link rel="apple-touch-icon" href="images/favicon/apple-touch-icon.png" />
<link rel="manifest" href="site.webmanifest" />

<meta property="og:type" content="website" />
<meta property="og:site_name" content="FIRST-COM GROUP" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:image" content="{site_url}/{og_image}" />
<meta property="og:locale" content="fr_FR" />
<meta property="og:url" content="{canonical}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{site_url}/{og_image}" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />

<link rel="stylesheet" href="css/style.css" />

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "FIRST-COM GROUP",
  "url": "{site_url}",
  "logo": "{site_url}/images/logo/logo-color.webp",
  "image": "{site_url}/{og_image}",
  "telephone": "{phone}",
  "email": "{email}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Attécoubé, Avenue de Locodjro, Quartier Jérusalem",
    "addressLocality": "Abidjan",
    "addressCountry": "CI"
  }},
  "areaServed": "CI",
  "sameAs": []
}}
</script>
""".format(
        title=title,
        description=description,
        canonical=canonical,
        site_url=SITE_URL,
        og_image=og_image,
        phone=PHONES_TEL[0],
        email=EMAIL,
    )


def header_nav(active_path):
    links = []
    for href, label in NAV_ITEMS:
        is_active = " is-active" if href == active_path else ""
        if href == "contact.html":
            continue
        links.append(
            '<a href="{href}" data-nav-link class="nav-link{active}">{label}</a>'.format(
                href=href, active=is_active, label=label
            )
        )
    desktop_links = "\n        ".join(links)

    mobile_links = []
    for href, label in NAV_ITEMS:
        is_active = " text-brick-600" if href == active_path else " text-navy-900"
        mobile_links.append(
            '<a href="{href}" data-mobile-link class="flex items-center justify-between border-b border-ink-100 py-4 text-lg font-semibold{active}">'
            '<span>{label}</span>{icon}</a>'.format(href=href, active=is_active, label=label, icon=icon("arrow-right", "w-5 h-5 text-ink-400"))
        )
    mobile_links_html = "\n          ".join(mobile_links)

    return """
<header data-header class="group fixed inset-x-0 top-0 z-50 transition-all duration-300">
  <div class="absolute inset-0 -z-10 bg-white/90 backdrop-blur-md transition-all duration-300 group-[.is-scrolled]:bg-white/95 group-[.is-scrolled]:shadow-[0_1px_0_0_rgba(10,26,68,0.08)]"></div>
  <div class="container">
    <div class="flex h-24 items-center justify-between sm:h-28">
      <a href="index.html" class="flex items-center gap-2.5 shrink-0" aria-label="FIRST-COM GROUP — Accueil">
        <img src="images/logo/logo-color.webp" alt="FIRST-COM GROUP" class="h-12 w-auto sm:h-14" />
      </a>

      <nav class="hidden lg:flex items-center gap-9">
        {desktop_links}
      </nav>

      <div class="hidden lg:flex items-center gap-3">
        <a href="tel:{phone_tel}" class="hidden xl:inline-flex items-center gap-2 text-sm font-semibold text-navy-700 transition-colors hover:text-brick-600">
          {phone_icon}
          {phone_display}
        </a>
        <a href="contact.html" class="btn-primary">Parlons de votre projet</a>
      </div>

      <button type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-menu" aria-label="Ouvrir le menu"
        class="lg:hidden inline-flex h-11 w-11 items-center justify-center rounded-full text-navy-900 ring-1 ring-ink-200 transition-colors">
        <span data-menu-icon-open>{menu_icon}</span>
        <span data-menu-icon-close class="hidden">{close_icon}</span>
      </button>
    </div>
  </div>

  <div id="mobile-menu" data-mobile-menu class="hidden lg:hidden fixed inset-0 top-24 sm:top-28 z-40 overflow-y-auto bg-white px-6 pb-10 pt-2">
    <nav class="flex flex-col">
      {mobile_links}
    </nav>
    <div class="mt-6 flex flex-col gap-3" data-mobile-link>
      <a href="tel:{phone_tel}" class="btn-outline w-full">{phone_icon} {phone_display}</a>
      <a href="contact.html" class="btn-primary w-full">Parlons de votre projet</a>
    </div>
  </div>
</header>
""".format(
        desktop_links=desktop_links,
        mobile_links=mobile_links_html,
        phone_tel=PHONES_TEL[0],
        phone_display=PHONES[0],
        phone_icon=icon("phone", "w-4 h-4"),
        menu_icon=icon("menu", "w-6 h-6"),
        close_icon=icon("close", "w-6 h-6"),
    )


def footer():
    service_links = "\n        ".join(
        '<li><a href="services.html#{id}" class="text-white/70 hover:text-white transition-colors">{short}</a></li>'.format(id=s["id"], short=s["short"])
        for s in SERVICES
    )
    nav_links = "\n        ".join(
        '<li><a href="{href}" class="text-white/70 hover:text-white transition-colors">{label}</a></li>'.format(href=href, label=label)
        for href, label in NAV_ITEMS
    )
    phones_html = "".join(
        '<a href="tel:{tel}" class="block hover:text-white transition-colors">{display}</a>'.format(tel=tel, display=display)
        for tel, display in zip(PHONES_TEL, PHONES)
    )
    return """
<footer class="relative overflow-hidden bg-navy-950 text-white">
  <div class="absolute inset-0 bg-dots-dark opacity-40"></div>
  <div class="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-navy-700/30 blur-3xl"></div>
  <div class="absolute -right-24 bottom-0 h-72 w-72 rounded-full bg-brick-600/10 blur-3xl"></div>

  <div class="container relative py-16 sm:py-20">
    <div class="grid grid-cols-1 gap-12 lg:grid-cols-12">
      <div class="lg:col-span-4">
        <img src="images/logo/logo-white.webp" alt="FIRST-COM GROUP" class="h-10 w-auto" />
        <p class="mt-5 max-w-xs text-sm leading-relaxed text-white/65">
          Réseaux, fibre optique, énergie, sécurité et data center : nous concevons, déployons et accompagnons
          les infrastructures techniques des entreprises et institutions en Côte d'Ivoire.
        </p>
        <div class="mt-6 flex items-center gap-3 text-xs font-semibold uppercase tracking-wide text-white/40">
          <span>Attécoubé — Abidjan, Côte d'Ivoire</span>
        </div>
      </div>

      <div class="lg:col-span-2">
        <p class="text-sm font-semibold text-white/90">Navigation</p>
        <ul class="mt-4 space-y-2.5 text-sm">
        {nav_links}
        </ul>
      </div>

      <div class="lg:col-span-3">
        <p class="text-sm font-semibold text-white/90">Nos domaines</p>
        <ul class="mt-4 space-y-2.5 text-sm">
        {service_links}
        </ul>
      </div>

      <div class="lg:col-span-3">
        <p class="text-sm font-semibold text-white/90">Contact</p>
        <div class="mt-4 space-y-3 text-sm text-white/70">
          <p class="leading-relaxed">{addr1}<br />{addr2}</p>
          <div class="space-y-1">{phones}</div>
          <a href="mailto:{email}" class="block hover:text-white transition-colors">{email}</a>
          <a href="https://{website}" class="block hover:text-white transition-colors">{website}</a>
        </div>
      </div>
    </div>

    <div class="mt-14 flex flex-col gap-4 border-t border-white/10 pt-8 text-xs text-white/45 sm:flex-row sm:items-center sm:justify-between">
      <p>&copy; <span data-year></span> FIRST-COM GROUP. Tous droits réservés.</p>
      <div class="flex flex-wrap gap-x-6 gap-y-2">
        <a href="mentions-legales.html" class="hover:text-white transition-colors">Mentions légales</a>
        <a href="confidentialite.html" class="hover:text-white transition-colors">Politique de confidentialité</a>
      </div>
    </div>
  </div>
</footer>
""".format(
        nav_links=nav_links,
        service_links=service_links,
        addr1=ADDRESS_LINES[0],
        addr2=ADDRESS_LINES[1],
        phones=phones_html,
        email=EMAIL,
        website=WEBSITE,
    )


def quick_contact_dock():
    return """
<div class="fixed bottom-5 right-5 z-40 flex flex-col items-end gap-3">
  <a href="tel:{phone_tel}" aria-label="Appeler FIRST-COM GROUP"
     class="group flex h-12 w-12 items-center justify-center rounded-full bg-white text-navy-800 shadow-card ring-1 ring-ink-100 transition-all hover:-translate-y-0.5 hover:shadow-card-hover hover:text-brick-600">
    {phone_icon}
  </a>
  <button type="button" data-to-top aria-label="Retour en haut de page"
     class="flex h-12 w-12 translate-y-3 items-center justify-center rounded-full bg-navy-900 text-white opacity-0 shadow-card transition-all duration-300 pointer-events-none hover:-translate-y-0.5 hover:bg-navy-800">
    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
  </button>
</div>
""".format(phone_tel=PHONES_TEL[0], phone_icon=icon("phone", "w-5 h-5"))


def scripts():
    return """
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="js/main.js" defer></script>
"""


def page(title, description, path, body, active_nav=None, extra_head=""):
    active = active_nav if active_nav else path
    return """<!doctype html>
<html lang="fr">
<head>
{head}{extra_head}
</head>
<body class="bg-white">
<a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:rounded-full focus:bg-white focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-navy-900 focus:shadow-card">Aller au contenu</a>
{header}
<main id="main">
{body}
</main>
{footer}
{dock}
{scripts}
</body>
</html>
""".format(
        head=head(title, description, path),
        extra_head=extra_head,
        header=header_nav(active),
        body=body,
        footer=footer(),
        dock=quick_contact_dock(),
        scripts=scripts(),
    )


def split_words(text):
    words = text.split(" ")
    return " ".join('<span class="inline-block overflow-hidden align-bottom"><span class="word inline-block">' + w + "&nbsp;</span></span>" for w in words)


# ---------------------------------------------------------------------------
# PAGE : ACCUEIL
# ---------------------------------------------------------------------------

def home_hero():
    return """
<section class="relative overflow-hidden bg-navy-gradient-light pb-24 pt-40 sm:pb-32 sm:pt-48">
  <div class="absolute inset-0 bg-dots-light opacity-70"></div>
  <div class="pointer-events-none absolute -left-40 top-24 h-96 w-96 rounded-full bg-navy-300/25 blur-3xl"></div>
  <div class="pointer-events-none absolute right-0 top-0 h-[32rem] w-[32rem] rounded-full bg-brick-500/10 blur-3xl"></div>
  <div class="fiber-line absolute left-0 right-0 top-20 opacity-30"></div>

  <div class="container relative grid grid-cols-1 items-center gap-16 lg:grid-cols-12 lg:gap-8">
    <div class="lg:col-span-7">
      <p data-hero-eyebrow class="eyebrow">
        <span class="h-[2px] w-6 bg-brick-500 block"></span>
        FIRST-COM GROUP — Attécoubé, Abidjan
      </p>
      <h1 data-hero-title class="mt-6 text-display-xl font-display font-bold text-navy-900 text-balance">
        <span class="text-brick-600">""" + split_words("NOTRE EXPERTISE") + """</span><br class="hidden sm:block" />
        """ + split_words("À VOTRE SERVICE") + """
      </h1>
      <p data-hero-sub class="mt-7 max-w-xl text-lg leading-relaxed text-ink-500">
        Câblage réseau, fibre optique, data center, énergie, sécurité électronique, supervision et métrologie :
        notre équipe conçoit, déploie et accompagne vos infrastructures IT &amp; télécoms clé en main, à Abidjan
        et partout en Côte d'Ivoire.
      </p>
      <div data-hero-cta class="mt-9 flex flex-col gap-4 sm:flex-row sm:items-center">
        <a href="contact.html" class="btn-primary">
          Parlons de votre projet
          """ + icon("arrow-right", "w-4 h-4") + """
        </a>
        <a href="services.html" class="btn-outline">
          Découvrir nos solutions
        </a>
      </div>

      <div data-hero-stats class="mt-14 grid max-w-lg grid-cols-3 gap-6 border-t border-navy-900/10 pt-8">
        <div>
          <p class="stat-num"><span data-count="8">0</span>+</p>
          <p class="mt-1 text-xs font-medium uppercase tracking-wide text-ink-400">Années d'expérience</p>
        </div>
        <div>
          <p class="stat-num"><span data-count="50">0</span>+</p>
          <p class="mt-1 text-xs font-medium uppercase tracking-wide text-ink-400">Projets réalisés</p>
        </div>
        <div>
          <p class="stat-num"><span data-count="10">0</span>+</p>
          <p class="mt-1 text-xs font-medium uppercase tracking-wide text-ink-400">Partenaires technologiques</p>
        </div>
      </div>
    </div>

    <div class="lg:col-span-5">
      <div data-hero-visual class="relative mx-auto max-w-md lg:max-w-none">
        <div data-hero-parallax class="relative">
          <div class="relative overflow-hidden rounded-[1.75rem] shadow-glow ring-1 ring-ink-100">
            <img src="images/hero/hero-datacenter.webp" alt="Baie de serveurs et infrastructure réseau supervisées par FIRST-COM GROUP"
                 class="h-[420px] w-full object-cover sm:h-[480px]" width="666" height="973" fetchpriority="high" />
            <div class="absolute inset-0 bg-gradient-to-t from-navy-950/70 via-navy-950/5 to-transparent"></div>
            <div class="absolute inset-0 bg-gradient-to-br from-brick-600/10 via-transparent to-navy-900/20"></div>
          </div>

          <div data-float-card class="absolute -left-6 -bottom-8 w-52 rounded-2xl bg-white/95 p-4 shadow-glow ring-1 ring-ink-100 backdrop-blur sm:-left-10">
            <div class="flex items-center gap-3">
              <span class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-navy-50 text-navy-700">""" + icon("radar", "w-5 h-5") + """</span>
              <div>
                <p class="text-sm font-bold text-navy-900">Supervision active</p>
                <p class="text-xs text-ink-400">Alertes fibre en temps réel</p>
              </div>
            </div>
          </div>

          <div data-float-card class="absolute -right-4 -top-6 flex items-center gap-2 rounded-full bg-white/95 px-4 py-2.5 shadow-glow ring-1 ring-ink-100 backdrop-blur sm:-right-8">
            <span class="relative flex h-2.5 w-2.5">
              <span class="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
              <span class="relative inline-flex h-2.5 w-2.5 rounded-full bg-emerald-500"></span>
            </span>
            <span class="text-xs font-semibold text-navy-800">Réseaux opérationnels</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""


def home_logo_strip():
    tiles = "\n      ".join(
        '<div class="logo-tile"><img src="images/clients/{slug}.webp" alt="{name}" class="max-h-10 w-auto object-contain" loading="lazy" /></div>'.format(slug=slug, name=name)
        for slug, name, _ in CLIENTS
    )
    return """
<section class="border-b border-ink-100 bg-white py-12">
  <div class="container">
    <p data-reveal class="text-center text-xs font-semibold uppercase tracking-[0.2em] text-ink-400">
      Ils nous font confiance
    </p>
    <div class="relative mt-8 overflow-hidden">
      <div class="pointer-events-none absolute inset-y-0 left-0 z-10 w-16 bg-gradient-to-r from-white to-transparent sm:w-28"></div>
      <div class="pointer-events-none absolute inset-y-0 right-0 z-10 w-16 bg-gradient-to-l from-white to-transparent sm:w-28"></div>
      <div class="marquee-track animate-marquee" data-marquee>
        {tiles}
      </div>
    </div>
  </div>
</section>
""".format(tiles=tiles)


def home_expertise():
    cards = []
    for s in SERVICES:
        cards.append("""
        <div data-reveal data-tilt class="card card-hover group flex flex-col p-7">
          <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-navy-900 text-white transition-colors group-hover:bg-brick-500">
            {icon}
          </span>
          <h3 class="mt-5 font-display text-lg font-semibold text-navy-900">{title}</h3>
          <p class="mt-2.5 text-sm leading-relaxed text-ink-500">{desc}</p>
          <a href="services.html#{id}" class="btn-ghost mt-6">
            Découvrir {arrow}
          </a>
        </div>
        """.format(icon=icon(s["icon"], "w-6 h-6"), title=s["title"], desc=s["desc"], id=s["id"], arrow=icon("arrow-right", "w-4 h-4")))
    cards_html = "\n".join(cards)
    return """
<section id="expertise" class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Nos domaines d'expertise</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Huit domaines, une seule équipe pour piloter votre infrastructure
      </h2>
      <p data-reveal class="mt-4 text-ink-500 leading-relaxed">
        Du câblage à la supervision fibre, en passant par l'énergie et la sécurité : nous couvrons l'ensemble
        de la chaîne technique, avec la même exigence à chaque étape.
      </p>
    </div>

    <div class="mt-14 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {cards}
    </div>
  </div>
</section>
""".format(cards=cards_html)


def home_sectors_slider():
    slides = []
    for s in SERVICES:
        slides.append("""
        <div data-slide data-reveal class="group relative w-[78%] shrink-0 snap-center-slide overflow-hidden rounded-2xl bg-white shadow-card ring-1 ring-ink-100 sm:w-[46%] lg:w-[29%]">
          <div class="relative h-52 overflow-hidden sm:h-56">
            <img src="{image}" alt="{alt}" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-navy-950/75 via-navy-950/10 to-transparent"></div>
            <span class="absolute left-4 top-4 flex h-10 w-10 items-center justify-center rounded-lg bg-white/95 text-navy-800 shadow-card">{icon}</span>
            <p class="absolute bottom-4 left-4 right-4 font-display text-lg font-semibold text-white text-balance">{title}</p>
          </div>
          <div class="p-5">
            <p class="text-sm leading-relaxed text-ink-500">{desc}</p>
            <a href="services.html#{id}" class="btn-ghost mt-4">
              En savoir plus {arrow}
            </a>
          </div>
        </div>
        """.format(
            image=s["image"], alt="Illustration du secteur " + s["title"], icon=icon(s["icon"], "w-5 h-5"),
            title=s["title"], desc=s["desc"], id=s["id"], arrow=icon("arrow-right", "w-4 h-4"),
        ))
    slides_html = "\n".join(slides)
    return """
<section id="expertise" class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Nos secteurs d'intervention</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Huit domaines, une seule équipe pour piloter votre infrastructure
      </h2>
      <p data-reveal class="mt-4 text-ink-500 leading-relaxed">
        Du câblage à la supervision fibre, en passant par l'énergie et la sécurité : nous couvrons l'ensemble
        de la chaîne technique, avec la même exigence à chaque étape.
      </p>
    </div>

    <div class="mt-14">
      <div data-slider class="relative">
        <div data-slider-track class="-mx-4 flex snap-x-mandatory gap-5 overflow-x-auto px-4 pb-2 no-scrollbar sm:mx-0 sm:px-0">
          {slides}
        </div>
        <div class="mt-8 flex items-center justify-center gap-3">
          <button type="button" data-slider-prev aria-label="Secteur précédent"
            class="flex h-11 w-11 items-center justify-center rounded-full bg-white text-navy-800 ring-1 ring-ink-200 shadow-card transition-all duration-300 hover:-translate-y-0.5 hover:bg-navy-900 hover:text-white disabled:pointer-events-none">
            {chevron_left}
          </button>
          <button type="button" data-slider-next aria-label="Secteur suivant"
            class="flex h-11 w-11 items-center justify-center rounded-full bg-white text-navy-800 ring-1 ring-ink-200 shadow-card transition-all duration-300 hover:-translate-y-0.5 hover:bg-navy-900 hover:text-white disabled:pointer-events-none">
            {chevron_right}
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
""".format(slides=slides_html, chevron_left=icon("chevron-left", "w-5 h-5"), chevron_right=icon("chevron-right", "w-5 h-5"))


def home_why_us():
    items = []
    for i, (ic, title, desc) in enumerate(WHY_US):
        items.append("""
        <div data-reveal class="flex gap-4">
          <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-white text-brick-600 shadow-card ring-1 ring-ink-100">
            {icon}
          </span>
          <div>
            <h3 class="font-display text-base font-semibold text-navy-900">{title}</h3>
            <p class="mt-1.5 text-sm leading-relaxed text-ink-500">{desc}</p>
          </div>
        </div>
        """.format(icon=icon(ic, "w-5 h-5"), title=title, desc=desc))
    items_html = "\n".join(items)
    return """
<section class="section overflow-hidden">
  <div class="container grid grid-cols-1 items-center gap-14 lg:grid-cols-12">
    <div class="lg:col-span-5">
      <div data-reveal class="relative">
        <div class="relative overflow-hidden rounded-[1.75rem] shadow-card ring-1 ring-ink-100">
          <img src="images/hero/hero-cabling.webp" alt="Baie de brassage réseau installée par FIRST-COM GROUP" class="h-[420px] w-full object-cover" loading="lazy" width="1400" height="2099" />
          <div class="absolute inset-0 bg-gradient-to-t from-navy-950/50 via-transparent to-transparent"></div>
        </div>
        <div class="absolute -bottom-7 -right-5 w-56 rounded-2xl bg-navy-900 p-5 text-white shadow-glow sm:-right-9">
          <p class="font-display text-3xl font-bold text-brick-500">100%</p>
          <p class="mt-1 text-xs leading-relaxed text-white/70">de nos projets suivent le même cycle : étude, déploiement, livraison clé en main.</p>
        </div>
      </div>
    </div>

    <div class="lg:col-span-7">
      <p data-reveal class="eyebrow">Pourquoi nous choisir</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Nous comprenons vos contraintes avant de parler de technologie
      </h2>
      <p data-reveal class="mt-4 max-w-xl text-ink-500 leading-relaxed">
        Chaque environnement est différent. Notre rôle est d'écouter votre besoin réel, puis de concevoir et
        d'installer la solution adaptée &mdash; avec un accompagnement de proximité, du premier diagnostic à la
        supervision continue.
      </p>
      <div class="mt-10 grid grid-cols-1 gap-x-8 gap-y-8 sm:grid-cols-2">
        {items}
      </div>
    </div>
  </div>
</section>
""".format(items=items_html)


def home_approach():
    steps = []
    for i, (num, title, desc) in enumerate(APPROACH):
        last = i == len(APPROACH) - 1
        connector = "" if last else '<div class="hidden h-px flex-1 bg-gradient-to-r from-navy-200 to-transparent lg:block"></div>'
        steps.append("""
        <div data-reveal class="flex flex-1 flex-col items-start lg:items-center lg:text-center">
          <div class="flex items-center gap-3 lg:flex-col lg:gap-4">
            <span class="font-display text-2xl font-bold text-brick-500">{num}</span>
            <span class="hidden h-10 w-px bg-navy-100 lg:hidden"></span>
          </div>
          <h3 class="mt-3 font-display text-base font-semibold text-navy-900 lg:mt-2">{title}</h3>
          <p class="mt-2 max-w-[15rem] text-sm leading-relaxed text-ink-500">{desc}</p>
        </div>
        {connector}
        """.format(num=num, title=title, desc=desc, connector=connector if not last else ""))
    steps_html = "\n".join(steps)
    return """
<section class="section bg-navy-50/40 relative overflow-hidden">
  <svg class="pointer-events-none absolute -right-16 -top-16 h-72 w-72 text-navy-200/70 sm:h-96 sm:w-96" viewBox="0 0 200 200" fill="none" aria-hidden="true">
    <circle cx="40" cy="40" r="3.5" fill="currentColor" />
    <circle cx="120" cy="25" r="3" fill="currentColor" />
    <circle cx="170" cy="70" r="4" fill="currentColor" />
    <circle cx="90" cy="90" r="3" fill="currentColor" />
    <circle cx="150" cy="140" r="3.5" fill="currentColor" />
    <circle cx="60" cy="150" r="3" fill="currentColor" />
    <circle cx="30" cy="110" r="2.5" fill="currentColor" />
    <path d="M40 40 90 90M120 25 90 90M120 25 170 70M170 70 90 90M90 90 60 150M90 90 30 110M60 150 150 140" stroke="currentColor" stroke-width="1.2" />
  </svg>
  <div class="container relative">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Notre approche</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Une méthode claire, du diagnostic à l'accompagnement
      </h2>
    </div>
    <div class="mt-16 flex flex-col gap-10 lg:flex-row lg:items-start lg:gap-4">
      {steps}
    </div>
  </div>
</section>
""".format(steps=steps_html)


def home_trust():
    client_tiles = "\n      ".join(
        '<div class="logo-tile"><img src="images/clients/{slug}.webp" alt="{name}" class="max-h-9 w-auto object-contain" loading="lazy" /></div>'.format(slug=slug, name=name)
        for slug, name, _ in CLIENTS
    )
    partner_cards = []
    for slug, name, desc, has_logo in PARTNERS:
        if has_logo:
            mark = '<img src="images/partners/{slug}.webp" alt="{name}" class="max-h-8 w-auto object-contain" loading="lazy" />'.format(slug=slug, name=name)
        else:
            mark = '<span class="font-display text-lg font-bold italic text-navy-800">{name}</span>'.format(name=name)
        partner_cards.append("""
        <div data-reveal class="card card-hover flex h-28 items-center justify-center p-6">
          {mark}
        </div>
        """.format(mark=mark))
    partners_html = "\n".join(partner_cards)
    return """
<section id="confiance" class="section">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Ils nous font confiance</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Des références qui témoignent de notre exigence</h2>
      <p data-reveal class="mt-4 text-ink-500 leading-relaxed">
        Opérateurs télécoms, institutions internationales, énergie, santé, industrie&nbsp;: des organisations aux besoins
        exigeants nous confient leurs infrastructures.
      </p>
    </div>

    <div class="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-5">
      {client_tiles}
    </div>

    <div class="mt-8 text-center">
      <a href="realisations.html" class="btn-ghost justify-center">
        Voir toutes nos références {arrow}
      </a>
    </div>

    <div class="mt-20">
      <p data-reveal class="text-center text-xs font-semibold uppercase tracking-[0.2em] text-ink-400">
        Nos partenaires technologiques
      </p>
      <div class="mt-8 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-5">
        {partners}
      </div>
    </div>
  </div>
</section>
""".format(client_tiles=client_tiles, partners=partners_html, arrow=icon("arrow-right", "w-4 h-4"))


def home_cta():
    return """
<section class="relative overflow-hidden bg-navy-gradient py-24 sm:py-28">
  <div class="absolute inset-0 bg-dots-dark opacity-50"></div>
  <div class="pointer-events-none absolute left-1/2 top-0 h-72 w-[40rem] -translate-x-1/2 rounded-full bg-brick-600/20 blur-3xl"></div>
  <div class="container relative text-center">
    <p data-reveal class="eyebrow justify-center !text-brick-400">Un projet en tête ?</p>
    <h2 data-reveal class="mx-auto mt-4 max-w-2xl text-display-md font-bold text-white text-balance">
      Un projet&nbsp;? Parlons-en.
    </h2>
    <p data-reveal class="mx-auto mt-4 max-w-xl text-white/70 leading-relaxed">
      Décrivez-nous votre besoin : notre équipe revient vers vous pour construire la solution la plus adaptée
      à votre environnement.
    </p>
    <div data-reveal class="mt-9 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="contact.html" class="btn-primary">
        Demander une étude {arrow}
      </a>
      <a href="mailto:{email}" class="btn-secondary">
        {mail_icon} {email}
      </a>
    </div>
  </div>
</section>
""".format(arrow=icon("arrow-right", "w-4 h-4"), mail_icon=icon("mail", "w-4 h-4"), email=EMAIL)


def page_banner(eyebrow, title, subtitle, extra=""):
    return """
<section class="relative overflow-hidden bg-navy-gradient-light pb-20 pt-36 sm:pb-24 sm:pt-44">
  <div class="absolute inset-0 bg-dots-light opacity-70"></div>
  <div class="pointer-events-none absolute -right-32 -top-16 h-96 w-96 rounded-full bg-navy-300/20 blur-3xl"></div>
  <div class="container relative">
    <p data-reveal class="eyebrow">
      <span class="h-[2px] w-6 bg-brick-500 block"></span>
      {eyebrow}
    </p>
    <h1 data-reveal class="mt-5 max-w-3xl text-display-lg font-bold text-navy-900 text-balance">{title}</h1>
    <p data-reveal class="mt-5 max-w-2xl text-lg leading-relaxed text-ink-500">{subtitle}</p>
    {extra}
  </div>
</section>
""".format(eyebrow=eyebrow, title=title, subtitle=subtitle, extra=extra)


TEAM_ROLES = [
    ("cable", "Techniciens câblage & réseau", "Déploiement du câblage informatique, téléphonique et des réseaux IP/Wi-Fi sur site."),
    ("fiber", "Techniciens fibre optique", "Déploiement FTTH, raccordement, tests OTDR/IOLM et supervision des liens fibre."),
    ("bolt", "Techniciens énergie", "Installation des groupes électrogènes, onduleurs, ateliers d'énergie et réseaux BT/MT/HT."),
    ("shield", "Techniciens sécurité électronique", "Installation de la vidéosurveillance, du contrôle d'accès et des systèmes de détection."),
]


def team_roles_html():
    return "\n".join("""
      <li class="flex items-start gap-3 rounded-xl bg-navy-50/60 p-4">
        <span class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-white text-navy-700 shadow-card">{icon}</span>
        <div>
          <p class="text-sm font-semibold text-navy-900">{title}</p>
          <p class="mt-1 text-xs leading-relaxed text-ink-500">{desc}</p>
        </div>
      </li>
    """.format(icon=icon(i, "w-4 h-4"), title=t, desc=d) for i, t, d in TEAM_ROLES)


PROJECT_DELIVERABLES = [
    ("search-check", "Étude technique", "Audit de votre site et de vos besoins, avant toute proposition."),
    ("route", "Plan de déploiement", "Un calendrier clair des étapes d'installation, adapté à vos contraintes d'exploitation."),
    ("check-badge", "Recette & mise en service", "Tests et validation de chaque équipement avant la mise en production."),
    ("life-buoy", "Accompagnement", "Un suivi et, selon les domaines, une supervision continue après l'installation."),
]


def project_deliverables_html():
    return "\n".join("""
      <div data-reveal class="card p-6">
        <span class="flex h-11 w-11 items-center justify-center rounded-xl bg-navy-900 text-white">{icon}</span>
        <h3 class="mt-4 font-display text-sm font-semibold text-navy-900">{title}</h3>
        <p class="mt-2 text-sm leading-relaxed text-ink-500">{desc}</p>
      </div>
    """.format(icon=icon(i, "w-5 h-5"), title=t, desc=d) for i, t, d in PROJECT_DELIVERABLES)


def approach_recap_html():
    return "\n".join("""
      <div data-reveal class="card p-6 text-center">
        <p class="font-display text-2xl font-bold text-brick-500">{num}</p>
        <p class="mt-2 font-display text-sm font-semibold text-navy-900">{title}</p>
        <p class="mt-1.5 text-xs leading-relaxed text-ink-500">{desc}</p>
      </div>
    """.format(num=num, title=title, desc=desc) for num, title, desc in APPROACH)


def todo_note(text):
    return """
<div data-reveal class="flex items-start gap-3 rounded-2xl border border-dashed border-amber-300 bg-amber-50/70 p-5">
  <span class="tag-todo mt-0.5 shrink-0">À compléter</span>
  <p class="text-sm leading-relaxed text-amber-800">{text}</p>
</div>
""".format(text=text)


# ---------------------------------------------------------------------------
# PAGE : À PROPOS
# ---------------------------------------------------------------------------

def build_about():
    values = [
        ("layers", "Expertise multi-domaines", "Réseau, fibre, énergie, sécurité, data center, métrologie : nous réunissons ces compétences pour simplifier votre quotidien."),
        ("check-badge", "Rigueur & méthode", "Étude, déploiement, configuration, accompagnement : chaque projet suit un processus structuré, du premier échange à la mise en service."),
        ("radar", "Réactivité", "Nos outils de supervision et de géolocalisation des défaillances nous permettent d'agir vite, avant que l'incident n'affecte votre activité."),
        ("map-pin", "Proximité", "Basés à Attécoubé, à Abidjan, nous restons proches de nos clients pour intervenir rapidement sur le terrain."),
    ]
    values_html = "\n".join("""
    <div data-reveal class="card p-7">
      <span class="flex h-11 w-11 items-center justify-center rounded-xl bg-navy-50 text-navy-700">{icon}</span>
      <h3 class="mt-4 font-display text-base font-semibold text-navy-900">{title}</h3>
      <p class="mt-2 text-sm leading-relaxed text-ink-500">{desc}</p>
    </div>
    """.format(icon=icon(i, "w-5 h-5"), title=t, desc=d) for i, t, d in values)

    body = page_banner(
        "À propos de FIRST-COM GROUP",
        "Une équipe technique au service de vos infrastructures",
        "FIRST-COM GROUP conçoit, déploie et supervise des solutions réseau, fibre optique, énergie, sécurité et "
        "data center pour des entreprises et institutions en Côte d'Ivoire.",
    ) + """
<section class="section">
  <div class="container grid grid-cols-1 gap-14 lg:grid-cols-12 lg:gap-10">
    <div class="lg:col-span-6">
      <p data-reveal class="eyebrow">Notre mission</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Mettre la technologie au service de votre activité, pas l'inverse
      </h2>
      <p data-reveal class="mt-5 leading-relaxed text-ink-500">
        Nous concevons et installons des solutions adaptées à votre environnement &mdash; réseau informatique et
        téléphonique, fibre optique, énergie, sécurité électronique, data center ou métrologie &mdash; avec un
        accompagnement de proximité, de l'étude initiale à la supervision au quotidien.
      </p>
      <p data-reveal class="mt-4 leading-relaxed text-ink-500">
        Notre objectif n'est pas de vendre de la technologie pour elle-même, mais de comprendre vos contraintes
        réelles &mdash; continuité de service, sécurité de vos sites, fiabilité de vos réseaux &mdash; pour construire
        la solution qui y répond durablement.
      </p>
    </div>
    <div class="lg:col-span-6">
      <p data-reveal class="eyebrow">Notre vision</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">
        Un partenaire technique unique pour des infrastructures qui durent
      </h2>
      <p data-reveal class="mt-5 leading-relaxed text-ink-500">
        Réseau, énergie et sécurité sont aujourd'hui indissociables. En réunissant ces expertises au sein d'une
        même équipe, nous simplifions la gestion de vos projets techniques et assurons une cohérence entre chaque
        brique de votre infrastructure.
      </p>
      <p data-reveal class="mt-4 leading-relaxed text-ink-500">
        Nous travaillons avec des marques reconnues internationalement &mdash; HIKVISION, Schneider Electric,
        Legrand, VIAVI, EXFO et nos autres partenaires technologiques &mdash; pour garantir la fiabilité de chaque
        installation.
      </p>
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Nos valeurs</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Ce qui guide chacune de nos interventions</h2>
    </div>
    <div class="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {values}
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid grid-cols-1 items-center gap-12 lg:grid-cols-12">
    <div class="lg:col-span-5">
      <div data-reveal class="relative overflow-hidden rounded-[1.75rem] bg-navy-gradient p-8 shadow-card sm:p-10">
        <div class="absolute inset-0 bg-dots-dark opacity-40"></div>
        <p class="relative eyebrow !text-brick-400">4 pôles techniques</p>
        <p class="relative mt-3 text-lg font-semibold text-white text-balance">Mobilisés selon la nature de votre projet</p>
        <div class="relative mt-8 grid grid-cols-2 gap-4">
          <div class="rounded-2xl bg-white/10 p-5 ring-1 ring-inset ring-white/15 backdrop-blur">
            {ic_cable}
            <p class="mt-3 text-sm font-semibold text-white">Câblage & réseau</p>
          </div>
          <div class="rounded-2xl bg-white/10 p-5 ring-1 ring-inset ring-white/15 backdrop-blur">
            {ic_fiber}
            <p class="mt-3 text-sm font-semibold text-white">Fibre optique</p>
          </div>
          <div class="rounded-2xl bg-white/10 p-5 ring-1 ring-inset ring-white/15 backdrop-blur">
            {ic_bolt}
            <p class="mt-3 text-sm font-semibold text-white">Énergie</p>
          </div>
          <div class="rounded-2xl bg-white/10 p-5 ring-1 ring-inset ring-white/15 backdrop-blur">
            {ic_shield}
            <p class="mt-3 text-sm font-semibold text-white">Sécurité électronique</p>
          </div>
        </div>
      </div>
    </div>
    <div class="lg:col-span-7">
      <p data-reveal class="eyebrow">Une équipe terrain</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Des techniciens qui interviennent sur vos sites</h2>
      <p data-reveal class="mt-5 leading-relaxed text-ink-500">
        Derrière chaque installation &mdash; câblage, fibre, énergie ou sécurité &mdash; nos équipes techniques se
        déplacent sur site pour étudier, déployer et configurer vos équipements, puis assurer le suivi dans la
        durée. Selon la nature du projet, votre interlocuteur mobilise les bonnes compétences internes&nbsp;:
      </p>
      <ul class="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-2">
        {roles}
      </ul>
      <div class="mt-6">
        {todo}
      </div>
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Notre méthode</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">La même rigueur, sur chaque projet</h2>
    </div>
    <div class="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-5">
      {approach_recap}
    </div>
    <div class="mt-10 text-center">
      <a href="services.html" class="btn-ghost justify-center">Découvrir nos domaines d'expertise {arrow}</a>
    </div>
  </div>
</section>

<section class="section bg-navy-950">
  <div class="container text-center">
    <p data-reveal class="eyebrow justify-center !text-brick-400">Travaillons ensemble</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-white text-balance">Envie d'échanger sur votre projet&nbsp;?</h2>
    <div data-reveal class="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="contact.html" class="btn-primary">Parlons de votre projet {arrow}</a>
      <a href="services.html" class="btn-secondary">Découvrir nos solutions</a>
    </div>
  </div>
</section>
""".format(
        values=values_html,
        roles=team_roles_html(),
        approach_recap=approach_recap_html(),
        todo=todo_note(
            "Présentation nominative de l'équipe dirigeante (photos et bios) &mdash; à intégrer par "
            "FIRST-COM GROUP. Aucune photo ni biographie fictive n'a été ajoutée."
        ),
        arrow=icon("arrow-right", "w-4 h-4"),
        ic_cable=icon("cable", "w-7 h-7 text-brick-400"),
        ic_fiber=icon("fiber", "w-7 h-7 text-brick-400"),
        ic_bolt=icon("bolt", "w-7 h-7 text-brick-400"),
        ic_shield=icon("shield", "w-7 h-7 text-brick-400"),
    )

    return page(
        title="À propos — FIRST-COM GROUP",
        description="Découvrez la mission, la vision et les valeurs de FIRST-COM GROUP, spécialiste des infrastructures réseau, énergie et sécurité à Abidjan.",
        path="a-propos.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGE : SERVICES
# ---------------------------------------------------------------------------

def build_services():
    subnav_items = "\n      ".join(
        '<a href="#{id}" class="shrink-0 rounded-full bg-white px-4 py-2 text-sm font-semibold text-navy-700 ring-1 ring-ink-100 transition-colors hover:bg-navy-900 hover:text-white">{short}</a>'.format(id=s["id"], short=s["short"])
        for s in SERVICES
    )

    blocks = []
    for i, s in enumerate(SERVICES):
        reverse = i % 2 == 1
        img_order = "lg:order-2" if reverse else ""
        text_order = "lg:order-1" if reverse else ""
        bullets_html = "\n          ".join(
            '<li class="flex items-start gap-3"><span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-emerald-50 text-emerald-600">{check}</span><span class="text-sm leading-relaxed text-ink-600">{b}</span></li>'.format(
                check=icon("check", "w-3.5 h-3.5"), b=b
            )
            for b in s["bullets"]
        )
        blocks.append("""
<section id="{id}" class="scroll-mt-28 border-t border-ink-100 py-16 sm:py-20">
  <div class="container grid grid-cols-1 items-center gap-12 lg:grid-cols-12 lg:gap-14">
    <div class="lg:col-span-6 {img_order}">
      <div data-reveal class="relative overflow-hidden rounded-[1.75rem] shadow-card ring-1 ring-ink-100">
        <img src="{image}" alt="{title} — FIRST-COM GROUP" class="h-[340px] w-full object-cover sm:h-[400px]" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-navy-950/55 via-transparent to-transparent"></div>
        <div class="absolute left-5 top-5 flex h-11 w-11 items-center justify-center rounded-xl bg-white/95 text-navy-800 shadow-card">
          {icon}
        </div>
      </div>
    </div>

    <div class="lg:col-span-6 {text_order}">
      <p data-reveal class="eyebrow">Domaine d'expertise</p>
      <h2 data-reveal class="mt-3 text-display-md font-bold text-balance">{title}</h2>

      <div data-reveal class="mt-5 space-y-4">
        <div class="rounded-xl bg-brick-50/70 p-4">
          <p class="text-xs font-semibold uppercase tracking-wide text-brick-600">Votre contexte</p>
          <p class="mt-1.5 text-sm leading-relaxed text-ink-600">{problem}</p>
        </div>
        <div class="rounded-xl bg-navy-50/70 p-4">
          <p class="text-xs font-semibold uppercase tracking-wide text-navy-700">Notre réponse</p>
          <p class="mt-1.5 text-sm leading-relaxed text-ink-600">{solution}</p>
        </div>
      </div>

      <p data-reveal class="mt-6 text-sm font-semibold text-navy-900">Ce que nous faisons</p>
      <ul data-reveal class="mt-3 space-y-2.5">
          {bullets}
      </ul>

      <a data-reveal href="contact.html?service={id}" class="btn-primary mt-8">
        Parler à un expert {arrow}
      </a>
    </div>
  </div>
</section>
""".format(
            id=s["id"], img_order=img_order, text_order=text_order, image=s["image"], title=s["title"],
            icon=icon(s["icon"], "w-5 h-5"), problem=s["problem"], solution=s["solution"], bullets=bullets_html,
            arrow=icon("arrow-right", "w-4 h-4"),
        ))
    blocks_html = "\n".join(blocks)

    body = page_banner(
        "Nos services",
        "Des solutions techniques pensées pour votre activité",
        "Huit domaines d'expertise, une même méthode : comprendre votre besoin, concevoir la solution adaptée, "
        "la déployer et vous accompagner dans la durée.",
    ) + """
<div class="sticky top-20 z-30 border-b border-ink-100 bg-white/90 backdrop-blur sm:top-24">
  <div class="container">
    <div class="flex gap-2.5 overflow-x-auto py-4 [-ms-overflow-style:none] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
      {subnav}
    </div>
  </div>
</div>

{blocks}

<section class="section bg-navy-950">
  <div class="container text-center">
    <p data-reveal class="eyebrow justify-center !text-brick-400">Une question sur un projet&nbsp;?</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-white text-balance">Discutons de la solution la plus adaptée à votre besoin</h2>
    <div data-reveal class="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="contact.html" class="btn-primary">Demander une étude {arrow}</a>
      <a href="tel:{phone_tel}" class="btn-secondary">{phone_icon} {phone}</a>
    </div>
  </div>
</section>
""".format(subnav=subnav_items, blocks=blocks_html, arrow=icon("arrow-right", "w-4 h-4"), phone_tel=PHONES_TEL[0], phone=PHONES[0], phone_icon=icon("phone", "w-4 h-4"))

    return page(
        title="Nos services — Réseau, fibre, énergie, sécurité | FIRST-COM GROUP",
        description="Câblage réseau, fibre optique, réseau IP & Wi-Fi, data center, énergie, supervision fibre, métrologie et sécurité : découvrez nos solutions en détail.",
        path="services.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGE : RÉFÉRENCES / RÉALISATIONS
# ---------------------------------------------------------------------------

def build_realisations():
    categories = {}
    for slug, name, sector in CLIENTS:
        categories.setdefault(sector, []).append((slug, name))

    cat_blocks = []
    for sector, items in categories.items():
        tiles = "\n        ".join(
            '<div class="logo-tile !opacity-100 !grayscale-0 sm:!h-24 sm:!w-52"><img src="images/clients/{slug}.webp" alt="{name}" class="max-h-12 w-auto object-contain" loading="lazy" /></div>'.format(slug=slug, name=name)
            for slug, name in items
        )
        cat_blocks.append("""
      <div data-reveal>
        <p class="text-xs font-semibold uppercase tracking-[0.16em] text-ink-400">{sector}</p>
        <div class="mt-4 flex flex-wrap gap-4">
          {tiles}
        </div>
      </div>
        """.format(sector=sector, tiles=tiles))
    cat_html = "\n".join(cat_blocks)

    partner_cards = []
    for slug, name, desc, has_logo in PARTNERS:
        mark = ('<img src="images/partners/{slug}.webp" alt="{name}" class="max-h-9 w-auto object-contain" loading="lazy" />'.format(slug=slug, name=name)
                if has_logo else
                '<span class="font-display text-xl font-bold italic text-navy-800">{name}</span>'.format(name=name))
        partner_cards.append("""
        <div data-reveal class="card card-hover flex flex-col items-start gap-4 p-6">
          <div class="flex h-12 items-center">{mark}</div>
          <p class="text-sm leading-relaxed text-ink-500">{desc}</p>
        </div>
        """.format(mark=mark, desc=desc))
    partners_html = "\n".join(partner_cards)

    body = page_banner(
        "Références &amp; partenaires",
        "Ils nous font confiance",
        "Opérateurs télécoms, institutions internationales, énergie, santé, industrie&nbsp;: un aperçu des "
        "organisations qui nous ont confié leurs projets techniques, et des partenaires technologiques avec "
        "lesquels nous déployons nos solutions.",
    ) + """
<section class="section">
  <div class="container">
    <p data-reveal class="eyebrow">Références projets</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Un panel d'organisations exigeantes</h2>
    <div class="mt-12 space-y-12">
      {categories}
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container">
    <p data-reveal class="eyebrow">Partenaires technologiques</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Des équipements de marques reconnues</h2>
    <p data-reveal class="mt-4 max-w-2xl text-ink-500 leading-relaxed">
      Nous sélectionnons et déployons des équipements de fabricants internationaux reconnus pour leur fiabilité,
      afin de garantir la performance et la pérennité de vos installations.
    </p>
    <div class="mt-12 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
      {partners}
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">Ce que comprend un projet</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Ce que vous recevez, à chaque étape</h2>
      <p data-reveal class="mt-4 text-ink-500 leading-relaxed">
        Quel que soit le domaine &mdash; réseau, fibre, énergie ou sécurité &mdash; chaque projet suit le même
        cadre, pour que vous sachiez toujours où vous en êtes.
      </p>
    </div>
    <div class="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {deliverables}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <p data-reveal class="eyebrow">Études de cas</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Des projets détaillés, bientôt en ligne</h2>
    <div class="mt-8 max-w-2xl">
      {todo}
    </div>
  </div>
</section>

<section class="section bg-navy-950">
  <div class="container text-center">
    <p data-reveal class="eyebrow justify-center !text-brick-400">Rejoignez nos références</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-white text-balance">Votre projet mérite la même exigence</h2>
    <div data-reveal class="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="contact.html" class="btn-primary">Demander une étude {arrow}</a>
    </div>
  </div>
</section>
""".format(
        categories=cat_html,
        partners=partners_html,
        deliverables=project_deliverables_html(),
        todo=todo_note(
            "Études de cas détaillées par projet (contexte, solution déployée, photos du chantier) &mdash; à "
            "fournir par FIRST-COM GROUP pour publication. Aucun projet fictif n'a été inventé pour ce prototype."
        ),
        arrow=icon("arrow-right", "w-4 h-4"),
    )

    return page(
        title="Références & partenaires — FIRST-COM GROUP",
        description="Découvrez les organisations qui font confiance à FIRST-COM GROUP et les partenaires technologiques (HIKVISION, Schneider Electric, VIAVI, EXFO...) qui équipent nos projets.",
        path="realisations.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGE : RÉALISATION (galerie de projets)
# ---------------------------------------------------------------------------
#
# Structure prête à recevoir de vrais projets (photos de chantier, avant/après,
# vidéos courtes) fournis par FIRST-COM GROUP. Tant que PROJECTS est vide, la
# page affiche une galerie illustrant les domaines d'intervention (mêmes
# photos que la page Services — aucune image inventée) avec un encart
# "à compléter". Pour publier un vrai projet, ajoutez un dict à la liste avec
# les mêmes clés que cet exemple, puis régénérez le site :
#
# PROJECTS = [
#     {
#         "title": "Câblage réseau — Siège client",
#         "sector": "Câblage réseau",
#         "location": "Abidjan",
#         "desc": "Refonte du câblage structuré sur plusieurs étages.",
#         "image": "images/realisations/exemple-01.webp",
#         "image_after": "",   # optionnel : 2e photo pour un rendu avant / après
#         "video": "",         # optionnel : chemin ou URL vers une courte vidéo
#     },
# ]
PROJECTS = []


def realisation_cards_html():
    cards = []
    for p in PROJECTS:
        media = '<img src="{image}" alt="{title}" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" />'.format(
            image=p["image"], title=p["title"]
        )
        after_badge = ""
        if p.get("image_after"):
            after_badge = '<span class="absolute right-4 top-4 badge">Avant / après</span>'
        video_badge = ""
        if p.get("video"):
            video_badge = (
                '<span class="absolute inset-0 flex items-center justify-center bg-navy-950/25 opacity-0 '
                'transition-opacity duration-300 group-hover:opacity-100">'
                '<span class="flex h-14 w-14 items-center justify-center rounded-full bg-white/95 text-navy-900 shadow-card">'
                + icon("play", "w-6 h-6") + "</span></span>"
            )
        cards.append("""
        <div data-reveal class="group relative overflow-hidden rounded-2xl bg-white shadow-card ring-1 ring-ink-100">
          <div class="relative h-56 overflow-hidden">
            {media}
            {video_badge}
            <div class="absolute inset-0 bg-gradient-to-t from-navy-950/70 via-navy-950/5 to-transparent"></div>
            {after_badge}
            <p class="absolute bottom-4 left-4 right-4 font-display text-base font-semibold text-white text-balance">{title}</p>
          </div>
          <div class="p-5">
            <div class="flex flex-wrap items-center gap-2">
              <span class="badge">{sector}</span>
              {location_badge}
            </div>
            <p class="mt-3 text-sm leading-relaxed text-ink-500">{desc}</p>
          </div>
        </div>
        """.format(
            media=media,
            video_badge=video_badge,
            after_badge=after_badge,
            title=p["title"],
            sector=p["sector"],
            location_badge='<span class="badge-red">{loc}</span>'.format(loc=p["location"]) if p.get("location") else "",
            desc=p["desc"],
        ))
    return "\n".join(cards)


# Photos libres de droit (gratuites, sans attribution requise) choisies pour illustrer la
# page Réalisation avec des visuels de terrain/intervention plutôt que les photos produit de
# la page Services. Utilisées uniquement ici ; la page Services garde ses images d'origine.
REALISATION_IMAGES = {
    "cablage-reseau": "images/realisations/cablage-reseau-intervention.webp",
    "fibre-optique": "images/realisations/fibre-optique-baie.webp",
    "reseau-ip-wifi": "images/realisations/reseau-ip-wifi-antenne.webp",
    "securite": "images/realisations/securite-cctv-installation.webp",
}


def sector_gallery_html():
    cards = []
    for s in SERVICES:
        image = REALISATION_IMAGES.get(s["id"], s["image"])
        cards.append("""
        <div data-reveal class="group relative overflow-hidden rounded-2xl bg-white shadow-card ring-1 ring-ink-100">
          <div class="relative h-56 overflow-hidden">
            <img src="{image}" alt="Illustration : {title}" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" />
            <div class="absolute inset-0 bg-gradient-to-t from-navy-950/70 via-navy-950/5 to-transparent"></div>
            <span class="absolute left-4 top-4 flex h-10 w-10 items-center justify-center rounded-lg bg-white/95 text-navy-800 shadow-card">{icon}</span>
          </div>
          <div class="p-5">
            <p class="badge">{short}</p>
            <p class="mt-3 text-sm leading-relaxed text-ink-500">{desc}</p>
          </div>
        </div>
        """.format(image=image, title=s["title"], icon=icon(s["icon"], "w-5 h-5"), short=s["short"], desc=s["desc"]))
    return "\n".join(cards)


def build_realisation_gallery():
    has_projects = bool(PROJECTS)
    gallery_html = realisation_cards_html() if has_projects else sector_gallery_html()

    body = page_banner(
        "Réalisation",
        "Nos interventions sur le terrain",
        "Chantiers, installations et équipes en action : un aperçu visuel de la manière dont nous déployons, "
        "sur site, les solutions présentées dans nos domaines d'expertise.",
    ) + """
<section class="section">
  <div class="container">
    <p data-reveal class="eyebrow">{eyebrow}</p>
    <h2 data-reveal class="mt-4 max-w-2xl text-display-md font-bold text-balance">{heading}</h2>
    <div class="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {gallery}
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container">
    <div class="mx-auto max-w-2xl text-center">
      <p data-reveal class="eyebrow justify-center">À venir</p>
      <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Avant / après &amp; vidéos d'intervention</h2>
    </div>
    <div class="mt-10 grid grid-cols-1 gap-6 lg:grid-cols-2">
      <div data-reveal class="flex flex-col items-center gap-4 rounded-2xl border-2 border-dashed border-ink-200 p-8 text-center">
        <span class="flex h-12 w-12 items-center justify-center rounded-full bg-white text-navy-700 shadow-card">{layers_icon}</span>
        <p class="font-display text-lg font-semibold text-navy-900">Avant / après</p>
        <p class="max-w-sm text-sm leading-relaxed text-ink-500">Dès réception de photos de chantier avant et après travaux, cette section présentera nos interventions sous cette forme.</p>
      </div>
      <div data-reveal class="flex flex-col items-center gap-4 rounded-2xl border-2 border-dashed border-ink-200 p-8 text-center">
        <span class="flex h-12 w-12 items-center justify-center rounded-full bg-white text-navy-700 shadow-card">{play_icon}</span>
        <p class="font-display text-lg font-semibold text-navy-900">Vidéos d'intervention</p>
        <p class="max-w-sm text-sm leading-relaxed text-ink-500">Cet emplacement accueillera de courtes vidéos (formats légers) de nos équipes en intervention sur le terrain.</p>
      </div>
    </div>
    <div class="mt-8 max-w-2xl">
      {todo}
    </div>
  </div>
</section>

<section class="section bg-navy-950">
  <div class="container text-center">
    <p data-reveal class="eyebrow justify-center !text-brick-400">Un projet en tête&nbsp;?</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-white text-balance">Discutons de votre prochaine installation</h2>
    <div data-reveal class="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="contact.html" class="btn-primary">Demander un devis {arrow}</a>
    </div>
  </div>
</section>
""".format(
        eyebrow="Nos réalisations" if has_projects else "Galerie",
        heading="Nos projets récents" if has_projects else "Nos domaines d'intervention en images",
        gallery=gallery_html,
        layers_icon=icon("layers", "w-6 h-6"),
        play_icon=icon("play", "w-6 h-6"),
        todo=todo_note(
            "Cette galerie affiche pour l'instant des illustrations de nos domaines d'intervention. Pour "
            "publier vos vraies réalisations (photos de chantier, équipements installés, équipes sur site, "
            "avant/après, vidéos courtes), transmettez-les à FIRST-COM GROUP&nbsp;: elles remplaceront "
            "automatiquement cette galerie, projet par projet, sans autre modification du site. Aucun projet "
            "fictif n'a été inventé pour ce prototype."
        ),
        arrow=icon("arrow-right", "w-4 h-4"),
    )

    return page(
        title="Réalisation — FIRST-COM GROUP",
        description="Découvrez nos interventions sur le terrain : chantiers, installations et équipes FIRST-COM GROUP en action sur les réseaux, la fibre optique, l'énergie et la sécurité électronique.",
        path="projets.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGE : CONTACT
# ---------------------------------------------------------------------------

NEXT_STEPS = [
    ("mail", "1. Réception", "Votre demande arrive directement à notre équipe, avec le détail de votre besoin."),
    ("search-check", "2. Qualification", "Nous analysons votre demande et revenons vers vous, par téléphone ou email, pour la préciser."),
    ("check-badge", "3. Proposition", "Selon le besoin, nous planifions une visite technique puis vous transmettons une proposition adaptée."),
]


def next_steps_html():
    return "\n".join("""
      <div data-reveal class="flex items-start gap-4">
        <span class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-navy-50 text-navy-700">{icon}</span>
        <div>
          <p class="font-display text-sm font-semibold text-navy-900">{title}</p>
          <p class="mt-1.5 text-sm leading-relaxed text-ink-500">{desc}</p>
        </div>
      </div>
    """.format(icon=icon(i, "w-5 h-5"), title=t, desc=d) for i, t, d in NEXT_STEPS)


def build_contact():
    service_options = "\n          ".join(
        '<option value="{id}">{title}</option>'.format(id=s["id"], title=s["title"]) for s in SERVICES
    )
    maps_query = "Att%C3%A9coub%C3%A9%20Avenue%20de%20Locodjro%2C%20Quartier%20J%C3%A9rusalem%2C%20Abidjan%2C%20C%C3%B4te%20d%27Ivoire"

    faq = [
        ("Sous quel délai obtiens-je une réponse à ma demande ?", "Notre équipe revient vers vous après étude de votre demande afin de qualifier votre besoin et, si nécessaire, planifier une visite technique sur site."),
        ("Intervenez-vous en dehors d'Abidjan ?", "Notre équipe est basée à Attécoubé, à Abidjan. Contactez-nous pour vérifier la faisabilité d'une intervention sur votre site, où qu'il se trouve en Côte d'Ivoire."),
        ("Proposez-vous un accompagnement après l'installation ?", "Oui : selon les domaines (fibre, métrologie, réseaux), nous proposons des solutions de supervision et de suivi continu, avec alertes en cas d'anomalie."),
        ("Comment se déroule une demande de devis ?", "Après réception de votre demande, nous qualifions votre besoin, réalisons si nécessaire une étude ou une visite technique, puis vous transmettons une proposition adaptée."),
    ]
    faq_html = "\n".join("""
    <div data-accordion-item data-open="false" class="border-b border-ink-100 py-5">
      <button type="button" data-accordion-trigger class="flex w-full items-center justify-between gap-4 text-left">
        <span class="font-display text-base font-semibold text-navy-900">{q}</span>
        <span data-accordion-icon class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-navy-50 text-navy-700 transition-transform duration-300">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>
        </span>
      </button>
      <div data-accordion-panel class="overflow-hidden transition-[max-height] duration-300 ease-out">
        <p class="pt-3 pr-10 text-sm leading-relaxed text-ink-500">{a}</p>
      </div>
    </div>
    """.format(q=q, a=a) for q, a in faq)

    body = page_banner(
        "Contact",
        "Un projet ? Parlons-en.",
        "Décrivez-nous votre besoin&nbsp;: notre équipe vous recontacte pour qualifier votre demande et construire "
        "la solution la plus adaptée à votre environnement.",
    ) + """
<section class="section">
  <div class="container grid grid-cols-1 gap-14 lg:grid-cols-12">
    <div class="lg:col-span-7">
      <div data-reveal class="card p-7 sm:p-9" data-contact-form-wrap>
        <h2 class="font-display text-xl font-bold text-navy-900">Demander un devis</h2>
        <p class="mt-2 text-sm text-ink-500">Les champs marqués d'un * sont obligatoires.</p>

        <form data-contact-form class="mt-7 grid grid-cols-1 gap-5 sm:grid-cols-2" novalidate>
          <div data-field class="sm:col-span-1">
            <label for="f-name" class="text-sm font-semibold text-navy-800">Nom complet *</label>
            <input id="f-name" name="name" type="text" required
              class="mt-2 w-full rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors placeholder:text-ink-400 focus:border-navy-300 focus:outline-none" placeholder="Votre nom" />
            <p data-field-error class="mt-1.5 hidden text-xs font-medium text-brick-600">Merci d'indiquer votre nom.</p>
          </div>
          <div data-field class="sm:col-span-1">
            <label for="f-company" class="text-sm font-semibold text-navy-800">Entreprise</label>
            <input id="f-company" name="company" type="text"
              class="mt-2 w-full rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors placeholder:text-ink-400 focus:border-navy-300 focus:outline-none" placeholder="Nom de votre structure" />
          </div>
          <div data-field class="sm:col-span-1">
            <label for="f-phone" class="text-sm font-semibold text-navy-800">Téléphone *</label>
            <input id="f-phone" name="phone" type="tel" required
              class="mt-2 w-full rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors placeholder:text-ink-400 focus:border-navy-300 focus:outline-none" placeholder="07 XX XX XX XX" />
            <p data-field-error class="mt-1.5 hidden text-xs font-medium text-brick-600">Merci d'indiquer un numéro valide.</p>
          </div>
          <div data-field class="sm:col-span-1">
            <label for="f-email" class="text-sm font-semibold text-navy-800">Email *</label>
            <input id="f-email" name="email" type="email" required
              class="mt-2 w-full rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors placeholder:text-ink-400 focus:border-navy-300 focus:outline-none" placeholder="vous@entreprise.com" />
            <p data-field-error class="mt-1.5 hidden text-xs font-medium text-brick-600">Merci d'indiquer un email valide.</p>
          </div>
          <div data-field class="sm:col-span-2">
            <label for="f-service" class="text-sm font-semibold text-navy-800">Service recherché</label>
            <select id="f-service" name="service"
              class="mt-2 w-full appearance-none rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors focus:border-navy-300 focus:outline-none">
              <option value="">Sélectionnez un domaine</option>
              {service_options}
              <option value="autre">Autre / je ne sais pas encore</option>
            </select>
          </div>
          <div data-field class="sm:col-span-2">
            <label for="f-message" class="text-sm font-semibold text-navy-800">Message *</label>
            <textarea id="f-message" name="message" rows="5" required
              class="mt-2 w-full rounded-xl border border-ink-100 bg-white px-4 py-3 text-sm text-navy-900 ring-1 ring-transparent transition-colors placeholder:text-ink-400 focus:border-navy-300 focus:outline-none" placeholder="Décrivez votre besoin, votre site, vos contraintes..."></textarea>
            <p data-field-error class="mt-1.5 hidden text-xs font-medium text-brick-600">Merci de décrire votre besoin.</p>
          </div>

          <div class="sm:col-span-2">
            <button type="submit" class="btn-primary w-full sm:w-auto">
              Demander un devis {arrow}
            </button>
            <p data-form-feedback class="mt-4 hidden text-sm leading-relaxed"></p>
          </div>
        </form>
      </div>
    </div>

    <div class="lg:col-span-5">
      <div class="space-y-5">
        <div data-reveal class="card flex items-start gap-4 p-6">
          <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-navy-50 text-navy-700">{pin}</span>
          <div>
            <p class="font-display text-sm font-semibold text-navy-900">Adresse</p>
            <p class="mt-1 text-sm leading-relaxed text-ink-500">{addr1}<br />{addr2}</p>
          </div>
        </div>
        <div data-reveal class="card flex items-start gap-4 p-6">
          <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-navy-50 text-navy-700">{phone_icon}</span>
          <div>
            <p class="font-display text-sm font-semibold text-navy-900">Téléphone</p>
            <div class="mt-1 space-y-1 text-sm text-ink-500">{phones}</div>
          </div>
        </div>
        <div data-reveal class="card flex items-start gap-4 p-6">
          <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-navy-50 text-navy-700">{mail_icon}</span>
          <div>
            <p class="font-display text-sm font-semibold text-navy-900">Email</p>
            <a href="mailto:{email}" class="mt-1 block text-sm text-ink-500 hover:text-brick-600">{email}</a>
          </div>
        </div>

        <div data-reveal class="overflow-hidden rounded-2xl shadow-card ring-1 ring-ink-100">
          <iframe
            title="Localisation de FIRST-COM GROUP — Attécoubé, Abidjan"
            src="https://www.google.com/maps?q={maps_query}&output=embed"
            class="h-64 w-full grayscale-[15%]" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-3">
      {next_steps}
    </div>
  </div>
</section>

<section class="section bg-navy-50/40">
  <div class="container max-w-3xl">
    <p data-reveal class="eyebrow">Questions fréquentes</p>
    <h2 data-reveal class="mt-4 text-display-md font-bold text-balance">Avant de nous écrire</h2>
    <div data-accordion data-reveal class="mt-8">
      {faq}
    </div>
  </div>
</section>
""".format(
        service_options=service_options,
        arrow=icon("arrow-right", "w-4 h-4"),
        pin=icon("map-pin", "w-5 h-5"),
        addr1=ADDRESS_LINES[0],
        addr2=ADDRESS_LINES[1],
        phone_icon=icon("phone", "w-5 h-5"),
        phones="".join('<a href="tel:{tel}" class="block hover:text-brick-600">{d}</a>'.format(tel=t, d=d) for t, d in zip(PHONES_TEL, PHONES)),
        mail_icon=icon("mail", "w-5 h-5"),
        email=EMAIL,
        maps_query=maps_query,
        next_steps=next_steps_html(),
        faq=faq_html,
    )

    return page(
        title="Contact — Demander un devis | FIRST-COM GROUP",
        description="Contactez FIRST-COM GROUP à Attécoubé, Abidjan : téléphone, email, formulaire de devis pour vos projets réseau, fibre optique, énergie et sécurité.",
        path="contact.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGES LÉGALES
# ---------------------------------------------------------------------------

def legal_shell(eyebrow, title, content_html):
    body = page_banner(eyebrow, title, "Ce contenu est fourni à titre de structure pour le site. Les informations juridiques précises doivent être complétées par FIRST-COM GROUP.") + """
<section class="section">
  <div class="container max-w-3xl">
    {todo}
    <div class="prose-legal mt-10 space-y-8">
      {content}
    </div>
  </div>
</section>
""".format(
        todo=todo_note("Ce texte est un modèle de structure. Les informations légales officielles (forme juridique, RCCM, régime fiscal, etc.) doivent être fournies et validées par FIRST-COM GROUP avant mise en ligne."),
        content=content_html,
    )
    return body


def build_mentions_legales():
    content = """
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Éditeur du site</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">
          Le présent site est édité par FIRST-COM GROUP, dont le siège est situé Attécoubé, Avenue de Locodjro,
          Quartier Jérusalem, Abidjan, Côte d'Ivoire.<br />
          Téléphone&nbsp;: {phones}<br />
          Email&nbsp;: <a href="mailto:{email}" class="text-navy-700 underline">{email}</a><br />
          Forme juridique, capital social et numéro RCCM&nbsp;: <em>à compléter</em>.
        </p>
      </div>
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Hébergement</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">Coordonnées de l'hébergeur du site&nbsp;: <em>à compléter</em>.</p>
      </div>
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Propriété intellectuelle</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">
          L'ensemble des contenus présents sur ce site (textes, logos, images) est la propriété de FIRST-COM GROUP,
          sauf mention contraire, et ne peut être reproduit sans autorisation préalable.
        </p>
      </div>
    """.format(phones=" / ".join(PHONES), email=EMAIL)
    return page(
        title="Mentions légales — FIRST-COM GROUP",
        description="Mentions légales du site FIRST-COM GROUP.",
        path="mentions-legales.html",
        body=legal_shell("Informations légales", "Mentions légales", content),
    )


def build_confidentialite():
    content = """
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Données collectées</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">
          Le formulaire de contact de ce site permet de collecter votre nom, votre entreprise, votre téléphone,
          votre email, le service recherché et votre message, dans le seul but de répondre à votre demande.
        </p>
      </div>
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Utilisation des données</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">
          Les informations transmises via le formulaire sont utilisées exclusivement pour traiter votre demande de
          devis ou de contact, et ne sont pas cédées à des tiers.
        </p>
      </div>
      <div data-reveal>
        <h2 class="font-display text-lg font-bold text-navy-900">Vos droits</h2>
        <p class="mt-3 text-sm leading-relaxed text-ink-500">
          Politique de conservation des données, durée de conservation et modalités d'exercice de vos droits
          (accès, rectification, suppression)&nbsp;: <em>à compléter</em> par FIRST-COM GROUP.
        </p>
      </div>
    """
    return page(
        title="Politique de confidentialité — FIRST-COM GROUP",
        description="Politique de confidentialité et protection des données du site FIRST-COM GROUP.",
        path="confidentialite.html",
        body=legal_shell("Vie privée", "Politique de confidentialité", content),
    )


def build_home():
    body = "\n".join([
        home_hero(),
        home_logo_strip(),
        home_sectors_slider(),
        home_why_us(),
        home_approach(),
        home_trust(),
        home_cta(),
    ])
    return page(
        title="FIRST-COM GROUP — Réseaux, fibre optique, énergie & sécurité à Abidjan",
        description="FIRST-COM GROUP conçoit, déploie et supervise vos infrastructures réseau, fibre optique, data center, énergie et sécurité électronique à Abidjan, Côte d'Ivoire.",
        path="index.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# PAGE 404
# ---------------------------------------------------------------------------

def build_404():
    body = """
<section class="relative overflow-hidden bg-navy-gradient py-32 sm:py-40">
  <div class="absolute inset-0 bg-dots-dark opacity-50"></div>
  <div class="container relative text-center">
    <p class="font-display text-7xl font-bold text-brick-500">404</p>
    <h1 class="mt-4 text-display-md font-bold text-white text-balance">Cette page n'existe pas ou plus</h1>
    <p class="mx-auto mt-4 max-w-md text-white/70">
      Le lien que vous avez suivi est peut-être incorrect, ou la page a été déplacée.
    </p>
    <div class="mt-9 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="index.html" class="btn-primary">Retour à l'accueil</a>
      <a href="contact.html" class="btn-secondary">Nous contacter</a>
    </div>
  </div>
</section>
"""
    return page(
        title="Page introuvable — FIRST-COM GROUP",
        description="Cette page n'existe pas ou plus.",
        path="404.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# FICHIERS TECHNIQUES : sitemap, robots, manifest
# ---------------------------------------------------------------------------

def build_sitemap():
    pages = ["index.html", "a-propos.html", "services.html", "realisations.html", "projets.html", "contact.html", "mentions-legales.html", "confidentialite.html"]
    urls = "\n".join(
        """  <url>
    <loc>{site}/{p}</loc>
    <changefreq>monthly</changefreq>
    <priority>{prio}</priority>
  </url>""".format(site=SITE_URL, p=p, prio="1.0" if p == "index.html" else "0.7")
        for p in pages
    )
    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""".format(urls=urls)


def build_robots():
    return """User-agent: *
Allow: /

Sitemap: {site}/sitemap.xml
""".format(site=SITE_URL)


def build_manifest():
    return """{
  "name": "FIRST-COM GROUP",
  "short_name": "FIRST-COM",
  "description": "Réseaux, fibre optique, énergie et sécurité à Abidjan.",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#0a1a44",
  "theme_color": "#0a1a44",
  "icons": [
    { "src": "images/favicon/favicon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "images/favicon/favicon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
"""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def write(path, content):
    full = os.path.join(ROOT, path)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path, len(content), "bytes")


def main():
    write("index.html", build_home())
    write("a-propos.html", build_about())
    write("services.html", build_services())
    write("realisations.html", build_realisations())
    write("projets.html", build_realisation_gallery())
    write("contact.html", build_contact())
    write("mentions-legales.html", build_mentions_legales())
    write("confidentialite.html", build_confidentialite())
    write("404.html", build_404())
    write("sitemap.xml", build_sitemap())
    write("robots.txt", build_robots())
    write("site.webmanifest", build_manifest())


if __name__ == "__main__":
    main()
