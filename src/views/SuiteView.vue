<template>
  <div>
    <!-- ================== -->
    <!--     Suite Hero       -->
    <!-- ================== -->
    <section class="hero-section page-hero">
      <div class="hero-content">
        <h1>Selyn Suite: La Super App qui unifie toute votre entreprise.</h1>
        <p class="subtitle">
          Finance, RH, CRM, Projets. Pilotez tout depuis une seule plateforme
          intelligente et évolutive.
        </p>
        <div class="cta-buttons">
          <a href="#offres" class="btn btn-secondary">Voir les tarifs</a>
          <a href="#" class="btn btn-outline">Demander une démo</a>
        </div>
      </div>
    </section>

    <!-- ===================== -->
    <!--   Video/Workflow      -->
    <!-- ===================== -->
    <section class="video-section">
      <div class="container">
        <h2 class="section-title">Découvrez la puissance de la Suite</h2>
        <div class="video-placeholder">
          <i class="far fa-play-circle"></i>
          <p>Vidéo de présentation à venir</p>
        </div>
      </div>
    </section>

    <!-- ===================== -->
    <!--   Modules Section     -->
    <!-- ===================== -->
    <section class="modules-section poles-section">
      <div class="container">
        <h2 class="section-title">
          Des modules conçus pour votre croissance
        </h2>
        <div class="poles-grid">
          <!-- Fictional screenshot could be a background of the card or an img tag -->
          <div class="pole-card fade-in-element">
            <i class="fas fa-wallet card-icon"></i>
            <h3>Finance & ERP</h3>
            <p>
              Comptabilité, facturation, trésorerie et budgets centralisés.
            </p>
          </div>
          <div class="pole-card fade-in-element">
            <i class="fas fa-users-cog card-icon"></i>
            <h3>RH & Paie</h3>
            <p>
              Gérez vos employés, les contrats, les congés et la paie en
              quelques clics.
            </p>
          </div>
          <div class="pole-card fade-in-element">
            <i class="fas fa-bullseye card-icon"></i>
            <h3>CRM & Ventes</h3>
            <p>
              Suivez vos prospects, gérez votre pipeline de vente et fidélisez
              vos clients.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== -->
    <!-- Comparison Table      -->
    <!-- ===================== -->
    <section class="comparison-section">
      <div class="container">
        <h2 class="section-title">Comparez nos formules</h2>
        <div class="table-responsive-wrapper">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>Fonctionnalités</th>
                <th>Essentiel</th>
                <th>Pro</th>
                <th>Entreprise</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Gestion des contacts (CRM)</td>
                <td><i class="fas fa-check"></i></td>
                <td><i class="fas fa-check"></i></td>
                <td><i class="fas fa-check"></i></td>
              </tr>
              <tr>
                <td>Facturation</td>
                <td><i class="fas fa-check"></i></td>
                <td><i class="fas fa-check"></i></td>
                <td><i class="fas fa-check"></i></td>
              </tr>
              <tr>
                <td>Gestion de trésorerie</td>
                <td><i class="fas fa-times"></i></td>
                <td><i class="fas fa-check"></i></td>
                <td><i class="fas fa-check"></i></td>
              </tr>
              <tr>
                <td>Module RH</td>
                <td><i class="fas fa-times"></i></td>
                <td><i class="fas fa-times"></i></td>
                <td><i class="fas fa-check"></i></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SuiteView',
};
</script>
