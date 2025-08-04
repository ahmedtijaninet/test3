<template>
  <div>
    <!-- ================== -->
    <!--   Consulting Hero    -->
    <!-- ================== -->
    <section class="hero-section page-hero">
      <div class="hero-content">
        <h1>Selyn Conseil</h1>
        <p class="subtitle">
          Transformer vos défis en opportunités, et vos ambitions en succès
          durables.
        </p>
      </div>
    </section>

    <!-- ======================= -->
    <!--   Expertise Section     -->
    <!-- ======================= -->
    <section class="expertise-section poles-section">
      <div class="container">
        <h2 class="section-title">Nos Domaines d'Intervention</h2>
        <div class="poles-grid">
          <div class="pole-card" v-fade-in>
            <i class="fas fa-lightbulb card-icon"></i>
            <h3>Étude & Montage de Projets</h3>
            <p>
              De l'idée à la réalisation, nous structurons votre projet pour
              maximiser ses chances de succès.
            </p>
          </div>
          <div class="pole-card" v-fade-in>
            <i class="fas fa-chart-line card-icon"></i>
            <h3>Optimisation & Financement</h3>
            <p>
              Nous analysons votre performance et nous vous aidons à trouver les
              leviers de croissance et les financements adaptés.
            </p>
          </div>
          <div class="pole-card" v-fade-in>
            <i class="fas fa-cogs card-icon"></i>
            <h3>Transformation Digitale</h3>
            <p>
              Intégrez les meilleures technologies pour optimiser vos opérations
              et créer de la valeur ajoutée.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ======================== -->
    <!--   Why Choose Us Section  -->
    <!-- ======================== -->
    <section class="why-choose-us-section">
      <div class="container">
        <h2 class="section-title">Pourquoi Nous Choisir ?</h2>
        <div class="why-choose-us-content">
          <div class="why-choose-us-text">
            <h3>Une Approche Partenaire, des Résultats Mesurables.</h3>
            <p>
              Chez SELYN, nous ne sommes pas de simples consultants. Nous sommes
              vos partenaires de croissance. Notre approche est basée sur
              l'écoute, la co-construction et un engagement total à vos côtés
              pour atteindre vos objectifs.
            </p>
            <p>
              Nous combinons une expertise stratégique de haut niveau avec une
              connaissance approfondie du terrain pour vous offrir des solutions
              pragmatiques et efficaces.
            </p>
          </div>
          <div class="why-choose-us-stats">
            <div class="stat-item">
              <span class="stat-number">95%</span>
              <span class="stat-label">Satisfaction Client</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">50+</span>
              <span class="stat-label">Projets Financés</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">+30%</span>
              <span class="stat-label">Croissance Moyenne</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ConsultingView',
};
</script>
