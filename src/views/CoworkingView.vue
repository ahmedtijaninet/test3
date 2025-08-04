<template>
  <div>
    <!-- ================== -->
    <!--   Coworking Hero   -->
    <!-- ================== -->
    <section
      class="hero-section page-hero"
      style="
        background-image: linear-gradient(
            rgba(0, 51, 102, 0.7),
            rgba(0, 51, 102, 0.7)
          ),
          url('https://images.unsplash.com/photo-1594122230689-45899d9e6f69?auto=format&fit=crop&w=1770&q=80');
      "
    >
      <div class="hero-content">
        <h1>Plus qu'un bureau, une communauté.</h1>
        <p class="subtitle">
          Découvrez un espace de travail inspirant, flexible et connecté, conçu
          pour les entrepreneurs et les innovateurs.
        </p>
        <a href="#tarifs" class="btn btn-secondary">Découvrir nos offres</a>
      </div>
    </section>

    <!-- ===================== -->
    <!--   Services Section    -->
    <!-- ===================== -->
    <section class="services-section poles-section">
      <div class="container">
        <h2 class="section-title">Des services tout inclus</h2>
        <div class="poles-grid poles-grid-4-cols">
          <div class="pole-card" v-fade-in>
            <i class="fas fa-wifi card-icon"></i>
            <h3>Fibre Optique</h3>
            <p>Connexion très haut débit pour une productivité maximale.</p>
          </div>
          <div class="pole-card" v-fade-in>
            <i class="fas fa-coffee card-icon"></i>
            <h3>Café à volonté</h3>
            <p>Pour faire le plein d'énergie tout au long de la journée.</p>
          </div>
          <div class="pole-card" v-fade-in>
            <i class="fas fa-phone-alt card-icon"></i>
            <h3>Cabines de visio</h3>
            <p>
              Des espaces insonorisés pour vos appels et réunions en ligne.
            </p>
          </div>
          <div class="pole-card" v-fade-in>
            <i class="fas fa-users card-icon"></i>
            <h3>Communauté</h3>
            <p>
              Accès à un réseau dynamique d'entrepreneurs et de créatifs.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== -->
    <!--    Tarifs Section     -->
    <!-- ===================== -->
    <section id="tarifs" class="pricing-section">
      <div class="container">
        <h2 class="section-title">Nos Formules</h2>
        <div class="pricing-grid">
          <div class="pricing-card" v-fade-in>
            <h3>Poste Nomade</h3>
            <div class="price">200 <span>DH / Jour</span></div>
            <p class="period">Flexibilité maximale</p>
            <ul class="features">
              <li><i class="fas fa-check"></i> Accès aux espaces partagés</li>
              <li><i class="fas fa-check"></i> Wifi Fibre & Café</li>
              <li><i class="fas fa-check"></i> Idéal pour freelances</li>
            </ul>
            <a href="#" class.btn.btn-outline>Réserver</a>
          </div>
          <div class="pricing-card popular" v-fade-in>
            <div class="popular-badge">Populaire</div>
            <h3>Abonnement Mensuel</h3>
            <div class="price">2 500 <span>DH / Mois</span></div>
            <p class="period">Votre bureau attitré</p>
            <ul class="features">
              <li><i class="fas fa-check"></i> Poste fixe dédié</li>
              <li><i class="fas fa-check"></i> Accès 24/7</li>
              <li><i class="fas fa-check"></i> Crédits salle de réunion</li>
            </ul>
            <a href="#" class.btn.btn-secondary>S'abonner</a>
          </div>
          <div class="pricing-card" v-fade-in>
            <h3>Bureau Privatif</h3>
            <div class="price">Sur Devis</div>
            <p class="period">Pour votre équipe</p>
            <ul class="features">
              <li><i class="fas fa-check"></i> Espace fermé et sécurisé</li>
              <li><i class="fas fa-check"></i> Pour 2 à 6 personnes</li>
              <li><i class="fas fa-check"></i> Tous services inclus</li>
            </ul>
            <a href="#" class.btn.btn-outline>Nous Contacter</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== -->
    <!--   Gallery Section     -->
    <!-- ===================== -->
    <section class="gallery-section">
      <div class="container">
        <h2 class="section-title">Ambiance & Culture</h2>
        <div class="gallery-grid">
          <img
            src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=870&q=80"
            alt="Galerie 1"
            v-fade-in
          />
          <img
            src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=871&q=80"
            alt="Galerie 2"
            v-fade-in
          />
          <img
            src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=870&q=80"
            alt="Galerie 3"
            v-fade-in
          />
          <img
            src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=870&q=80"
            alt="Galerie 4"
            v-fade-in
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'CoworkingView',
};
</script>
