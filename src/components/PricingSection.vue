<template>
  <section id="offres" class="pricing-section">
    <div class="container">
      <h2 class="section-title">Offres & Tarifs</h2>
      <div class="pricing-grid">
        <!-- Pricing Card 0: Gratuit -->
        <div class="pricing-card" v-fade-in>
          <h3>Panier 0 (Gratuit)</h3>
          <div class="price">0.00 <span>DH</span></div>
          <p class="period">Découverte</p>
          <ul class="features">
            <li><i class="fas fa-check"></i> 1ère consultation gratuite</li>
            <li><i class="fas fa-check"></i> 1 module SELYN Suite (1 mois)</li>
            <li><i class="fas fa-check"></i> 1h/semaine de coworking</li>
            <li><i class="fas fa-check"></i> Profil publié 15 jours</li>
            <li><i class="fas fa-check"></i> Participation aux événements</li>
          </ul>
          <a href="#" class="btn btn-outline">Commencer</a>
        </div>
        <!-- Pricing Card 1: Populaire -->
        <div class="pricing-card popular" v-fade-in>
          <div class="popular-badge">Populaire</div>
          <h3>Panier 1</h3>
          <div class="price">3 000 <span>DH HT / Mois</span></div>
          <p class="period">Accompagnement Continu</p>
          <ul class="features">
            <li>
              <i class="fas fa-check"></i> Gestion de projet, RH,
              pré-comptabilité
            </li>
            <li>
              <i class="fas fa-check"></i> Modules SELYN Suite (compta, tréso)
            </li>
            <li><i class="fas fa-check"></i> Coworking quotidien</li>
            <li><i class="fas fa-check"></i> Salle de réunion 1h/semaine</li>
            <li><i class="fas fa-check"></i> Services de secrétariat</li>
          </ul>
          <a href="#" class="btn btn-secondary">Choisir cette offre</a>
        </div>
        <!-- Pricing Card 2: Personnalisé -->
        <div class="pricing-card" v-fade-in>
          <h3>Panier 2 (Personnalisé)</h3>
          <div class="price">10 000 <span>DH HT / Trimestre</span></div>
          <p class="period">Solution Complète</p>
          <ul class="features">
            <li><i class="fas fa-check"></i> Étude et suivi de projets</li>
            <li>
              <i class="fas fa-check"></i> RH, optimisation, modules avancés
            </li>
            <li><i class="fas fa-check"></i> Accès coworking 2 pers.</li>
            <li><i class="fas fa-check"></i> Salle de réunion 3h/semaine</li>
            <li><i class="fas fa-check"></i> Secrétariat inclus</li>
          </ul>
          <a href="#" class="btn btn-outline">Nous Contacter</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "PricingSection",
};
</script>

<style scoped>
/* Scoped styles for the pricing section can go here */
</style>
