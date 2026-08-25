/* =========================================================================
   FIRST-COM GROUP — main.js
   Navigation, révélations au scroll, compteurs, formulaire, micro-interactions.
   Écrit en JavaScript natif + GSAP/ScrollTrigger (chargés en CDN dans le HTML).
   ========================================================================= */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = typeof window.gsap !== "undefined";
  if (hasGSAP && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ---------------------------------------------------------------------
     0. Année dans le footer
  --------------------------------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------------------------------------------------------------------
     1. Header : état "scrolled" + menu mobile
  --------------------------------------------------------------------- */
  var header = document.querySelector("[data-header]");
  function onScrollHeader() {
    if (!header) return;
    if (window.scrollY > 24) {
      header.classList.add("is-scrolled");
    } else {
      header.classList.remove("is-scrolled");
    }
  }
  onScrollHeader();
  window.addEventListener("scroll", onScrollHeader, { passive: true });

  var menuBtn = document.querySelector("[data-menu-toggle]");
  var mobileMenu = document.querySelector("[data-mobile-menu]");
  var menuOpenIcon = document.querySelector("[data-menu-icon-open]");
  var menuCloseIcon = document.querySelector("[data-menu-icon-close]");

  function setMenu(open) {
    if (!mobileMenu) return;
    mobileMenu.classList.toggle("hidden", !open);
    document.documentElement.classList.toggle("overflow-hidden", open);
    if (menuBtn) menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (menuOpenIcon && menuCloseIcon) {
      menuOpenIcon.classList.toggle("hidden", open);
      menuCloseIcon.classList.toggle("hidden", !open);
    }
    if (open && hasGSAP) {
      gsap.fromTo(
        "[data-mobile-menu] [data-mobile-link]",
        { opacity: 0, y: 14 },
        { opacity: 1, y: 0, duration: 0.45, stagger: 0.05, ease: "power2.out" }
      );
    }
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var isOpen = mobileMenu && !mobileMenu.classList.contains("hidden");
      setMenu(!isOpen);
    });
  }
  document.querySelectorAll("[data-mobile-link]").forEach(function (link) {
    link.addEventListener("click", function () { setMenu(false); });
  });

  /* ---------------------------------------------------------------------
     2. Ancre active dans la nav (page d'accueil, sections)
  --------------------------------------------------------------------- */
  var sections = document.querySelectorAll("main [id]");
  var navLinks = document.querySelectorAll("[data-nav-link]");
  if (sections.length && navLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    navLinks.forEach(function (l) {
      var href = l.getAttribute("href") || "";
      var id = href.split("#")[1];
      if (id) byId[id] = l;
    });
    var navObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = byId[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("is-active"); });
            link.classList.add("is-active");
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach(function (s) { navObserver.observe(s); });
  }

  /* ---------------------------------------------------------------------
     3. Révélations au scroll
  --------------------------------------------------------------------- */
  document.documentElement.classList.add("reveal-ready");
  var revealEls = document.querySelectorAll("[data-reveal]");
  if (reduceMotion) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else if (hasGSAP && window.ScrollTrigger) {
    revealEls.forEach(function (el, i) {
      ScrollTrigger.create({
        trigger: el,
        start: "top 88%",
        once: true,
        onEnter: function () {
          el.classList.add("is-visible");
        },
      });
    });
  } else if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------------------------------------------------------------------
     4. Compteurs animés (chiffres réels uniquement — voir data-count)
  --------------------------------------------------------------------- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count") || "0");
    var suffix = el.getAttribute("data-suffix") || "";
    var decimals = el.getAttribute("data-decimals") ? parseInt(el.getAttribute("data-decimals"), 10) : 0;
    if (reduceMotion) {
      el.textContent = target.toFixed(decimals) + suffix;
      return;
    }
    var obj = { val: 0 };
    if (hasGSAP) {
      gsap.to(obj, {
        val: target,
        duration: 1.8,
        ease: "power2.out",
        onUpdate: function () {
          el.textContent = obj.val.toFixed(decimals) + suffix;
        },
      });
    } else {
      var start = null;
      var duration = 1400;
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / duration, 1);
        el.textContent = (target * p).toFixed(decimals) + suffix;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
  }
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    if (hasGSAP && window.ScrollTrigger) {
      counters.forEach(function (el) {
        ScrollTrigger.create({
          trigger: el,
          start: "top 90%",
          once: true,
          onEnter: function () { animateCount(el); },
        });
      });
    } else if ("IntersectionObserver" in window) {
      var ioC = new IntersectionObserver(
        function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCount(entry.target);
              obs.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      counters.forEach(function (el) { ioC.observe(el); });
    } else {
      counters.forEach(animateCount);
    }
  }

  /* ---------------------------------------------------------------------
     5. Hero : entrée animée + parallaxe légère
  --------------------------------------------------------------------- */
  if (hasGSAP && !reduceMotion) {
    var heroTl = gsap.timeline({ defaults: { ease: "power3.out" } });
    if (document.querySelector("[data-hero-eyebrow]")) {
      heroTl
        .fromTo("[data-hero-eyebrow]", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.6 }, 0.1)
        .fromTo("[data-hero-title] .word", { opacity: 0, y: "110%" }, { opacity: 1, y: "0%", duration: 0.9, stagger: 0.06 }, 0.2)
        .fromTo("[data-hero-sub]", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.7 }, 0.55)
        .fromTo("[data-hero-cta]", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.7 }, 0.68)
        .fromTo("[data-hero-stats]", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.7 }, 0.78)
        .fromTo("[data-hero-visual]", { opacity: 0, scale: 0.94 }, { opacity: 1, scale: 1, duration: 1 }, 0.35);
    }
    document.querySelectorAll("[data-float-card]").forEach(function (card, i) {
      gsap.fromTo(
        card,
        { opacity: 0, y: 30 },
        { opacity: 1, y: 0, duration: 0.8, delay: 0.9 + i * 0.15, ease: "power3.out" }
      );
    });

    if (window.ScrollTrigger) {
      var heroVisual = document.querySelector("[data-hero-parallax]");
      if (heroVisual) {
        gsap.to(heroVisual, {
          yPercent: 10,
          ease: "none",
          scrollTrigger: {
            trigger: heroVisual,
            start: "top top",
            end: "bottom top",
            scrub: 0.6,
          },
        });
      }
    }
  } else {
    document.querySelectorAll("[data-hero-eyebrow],[data-hero-title],[data-hero-sub],[data-hero-cta],[data-hero-stats],[data-hero-visual],[data-float-card]")
      .forEach(function (el) { el.style.opacity = 1; });
  }

  /* ---------------------------------------------------------------------
     6. Cartes "tilt" légères au survol (desktop uniquement)
  --------------------------------------------------------------------- */
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches && !reduceMotion) {
    document.querySelectorAll("[data-tilt]").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = "perspective(900px) rotateX(" + (y * -4) + "deg) rotateY(" + (x * 5) + "deg) translateY(-4px)";
      });
      card.addEventListener("mouseleave", function () {
        card.style.transform = "";
      });
    });
  }

  /* ---------------------------------------------------------------------
     7. Accordéon (FAQ / process details)
  --------------------------------------------------------------------- */
  document.querySelectorAll("[data-accordion]").forEach(function (acc) {
    var items = acc.querySelectorAll("[data-accordion-item]");
    items.forEach(function (item) {
      var trigger = item.querySelector("[data-accordion-trigger]");
      var panel = item.querySelector("[data-accordion-panel]");
      if (!trigger || !panel) return;
      panel.style.maxHeight = "0px";
      trigger.addEventListener("click", function () {
        var isOpen = item.getAttribute("data-open") === "true";
        items.forEach(function (other) {
          other.setAttribute("data-open", "false");
          var p = other.querySelector("[data-accordion-panel]");
          if (p) p.style.maxHeight = "0px";
          var icon = other.querySelector("[data-accordion-icon]");
          if (icon) icon.style.transform = "rotate(0deg)";
        });
        if (!isOpen) {
          item.setAttribute("data-open", "true");
          panel.style.maxHeight = panel.scrollHeight + "px";
          var icon = item.querySelector("[data-accordion-icon]");
          if (icon) icon.style.transform = "rotate(45deg)";
        }
      });
    });
  });

  /* ---------------------------------------------------------------------
     8. Onglets (page Services)
  --------------------------------------------------------------------- */
  document.querySelectorAll("[data-tabs]").forEach(function (group) {
    var buttons = group.querySelectorAll("[data-tab-btn]");
    var panels = group.querySelectorAll("[data-tab-panel]");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-tab-btn");
        buttons.forEach(function (b) {
          var active = b === btn;
          b.classList.toggle("is-active", active);
        });
        panels.forEach(function (p) {
          p.classList.toggle("hidden", p.getAttribute("data-tab-panel") !== target);
        });
      });
    });
  });

  /* ---------------------------------------------------------------------
     9. Retour en haut
  --------------------------------------------------------------------- */
  var toTop = document.querySelector("[data-to-top]");
  if (toTop) {
    function toggleToTop() {
      toTop.classList.toggle("opacity-0", window.scrollY < 480);
      toTop.classList.toggle("pointer-events-none", window.scrollY < 480);
      toTop.classList.toggle("translate-y-3", window.scrollY < 480);
    }
    toggleToTop();
    window.addEventListener("scroll", toggleToTop, { passive: true });
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });
  }

  /* ---------------------------------------------------------------------
     10. Formulaire de contact (validation front + envoi via mailto de secours)
  --------------------------------------------------------------------- */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    try {
      var presetService = new URLSearchParams(window.location.search).get("service");
      var serviceSelect = form.querySelector("#f-service");
      if (presetService && serviceSelect) {
        var optionExists = Array.prototype.some.call(serviceSelect.options, function (o) {
          return o.value === presetService;
        });
        if (optionExists) serviceSelect.value = presetService;
      }
    } catch (err) {
      /* URLSearchParams indisponible : on ignore silencieusement */
    }
    var feedback = form.querySelector("[data-form-feedback]");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var required = form.querySelectorAll("[required]");
      var valid = true;
      required.forEach(function (field) {
        var group = field.closest("[data-field]") || field;
        var errorHint = group.querySelector ? group.querySelector("[data-field-error]") : null;
        if (!field.value || (field.type === "email" && !/^\S+@\S+\.\S+$/.test(field.value))) {
          valid = false;
          field.classList.add("ring-brick-400", "border-brick-400");
          if (errorHint) errorHint.classList.remove("hidden");
        } else {
          field.classList.remove("ring-brick-400", "border-brick-400");
          if (errorHint) errorHint.classList.add("hidden");
        }
      });

      if (!valid) {
        if (feedback) {
          feedback.textContent = "Merci de compléter les champs obligatoires avant d'envoyer votre demande.";
          feedback.classList.remove("hidden", "text-navy-700");
          feedback.classList.add("text-brick-600");
        }
        return;
      }

      var data = new FormData(form);
      var lines = [];
      lines.push("Nom : " + (data.get("name") || ""));
      lines.push("Entreprise : " + (data.get("company") || "—"));
      lines.push("Téléphone : " + (data.get("phone") || "—"));
      lines.push("Email : " + (data.get("email") || ""));
      lines.push("Service recherché : " + (data.get("service") || "—"));
      lines.push("");
      lines.push(data.get("message") || "");

      var subject = encodeURIComponent("Demande de devis — " + (data.get("name") || "Site web"));
      var body = encodeURIComponent(lines.join("\n"));
      var mailto = "mailto:info@firstcom-group.net?subject=" + subject + "&body=" + body;

      if (feedback) {
        feedback.textContent = "Votre client de messagerie va s'ouvrir avec votre demande pré-remplie. Vous pouvez aussi nous écrire directement à info@firstcom-group.net.";
        feedback.classList.remove("hidden", "text-brick-600");
        feedback.classList.add("text-navy-700");
      }
      window.location.href = mailto;
    });
  }

  /* ---------------------------------------------------------------------
     11. Marquee logos — duplique le contenu pour boucle infinie fluide
  --------------------------------------------------------------------- */
  document.querySelectorAll("[data-marquee]").forEach(function (track) {
    if (track.dataset.cloned) return;
    var clone = track.innerHTML;
    track.insertAdjacentHTML("beforeend", clone);
    track.dataset.cloned = "true";
  });
})();
