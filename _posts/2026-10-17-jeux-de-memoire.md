---
layout: post
title: "Jeux de mémoire : entraîne ton cerveau"
date: 2026-10-17 10:00:00 +0100
tags: [Jeux]
---

<img src="{{ '/assets/images/jeux-memoire.jpg' | relative_url }}" alt="Entraîne ton cerveau avec ces jeux" style="width:100%;height:auto;border-radius:16px">

Quatre jeux pour entraîner ta mémoire et ta concentration. Chaque jeu a 5 niveaux : réussis un niveau pour débloquer le suivant et gagner jusqu’à 3 étoiles.

- **Paires de cartes** : retrouve toutes les paires.
- **Simon** : répète la suite de couleurs et de sons.
- **Qu’est-ce qui a changé ?** : observe la scène, puis trouve ce qui a changé.
- **Rappel de mots** : mémorise des mots français, puis écris-les.

<iframe id="jeux" src="{{ '/jeux-memoire.html' | relative_url }}" title="Jeux de mémoire" width="100%" height="620" scrolling="no" style="display:block;width:100%;border:0;border-radius:20px;overflow:hidden" loading="lazy"></iframe>
<script>
addEventListener("message",function(e){var f=document.getElementById("jeux");if(f&&e.source===f.contentWindow&&e.data&&e.data.jmH){f.style.height=e.data.jmH+"px"}});
</script>

<p><a href="{{ '/jeux-memoire.html' | relative_url }}" target="_blank" rel="noopener">Ouvrir les jeux en plein écran</a></p>
