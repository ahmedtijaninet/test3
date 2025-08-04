<template>
  <section id="communaute" class="community-section">
    <div class="container">
      <h2 class="section-title">Communauté</h2>

      <!-- Testimonials -->
      <div class="testimonials-grid">
        <blockquote class="testimonial-card" v-fade-in>
          <img src="https://i.pravatar.cc/80?img=1" alt="Client 1" />
          <p>
            "L'accompagnement de SELYN a été un véritable accélérateur pour
            notre croissance. Une expertise rare."
          </p>
          <footer>— Jean Dupont, CEO de TechCorp</footer>
        </blockquote>
        <blockquote class="testimonial-card" v-fade-in>
          <img src="https://i.pravatar.cc/80?img=2" alt="Client 2" />
          <p>
            "La flexibilité de l'espace de coworking et la puissance de SELYN
            Suite nous ont permis de nous structurer rapidement."
          </p>
          <footer>— Fatima El Fassi, Fondatrice de Creative Minds</footer>
        </blockquote>
      </div>

      <!-- Mission & Vision -->
      <div class="mission-vision">
        <div>
          <h3>Notre Mission</h3>
          <p>
            Fournir un écosystème intégré qui simplifie l'entrepreneuriat et
            accélère la croissance des entreprises grâce à des solutions
            intelligentes et un environnement collaboratif.
          </p>
        </div>
        <div>
          <h3>Notre Vision</h3>
          <p>
            Devenir le partenaire stratégique de référence pour les entreprises
            en quête de transformation digitale, d'excellence opérationnelle et
            d'innovation durable.
          </p>
        </div>
      </div>

      <!-- Newsletter -->
      <div class="newsletter-signup">
        <h3>Rejoignez notre communauté</h3>
        <p>
          Recevez nos analyses, actualités et invitations exclusives en
          avant-première.
        </p>
        <form class="newsletter-form">
          <input type="email" placeholder="Votre adresse e-mail" required />
          <button type="submit" class="btn btn-secondary">S'inscrire</button>
        </form>
      </div>

      <!-- Team -->
      <div class="team-section">
        <h3 class="subsection-title">Notre Équipe</h3>
        <div class="team-grid">
          <div class="team-member">
            <img src="https://i.pravatar.cc/150?img=3" alt="Membre équipe 1" />
            <h4>Alice Martin</h4>
            <p>CEO & Fondatrice</p>
          </div>
          <div class="team-member">
            <img src="https://i.pravatar.cc/150?img=4" alt="Membre équipe 2" />
            <h4>Karim Bennani</h4>
            <p>Directeur Technique (CTO)</p>
          </div>
          <div class="team-member">
            <img src="https://i.pravatar.cc/150?img=5" alt="Membre équipe 3" />
            <h4>Sofia Chen</h4>
            <p>Responsable Coworking</p>
          </div>
        </div>
      </div>

      <!-- Partners -->
      <div class="partners-section">
        <h3 class="subsection-title">Nos Partenaires Stratégiques</h3>
        <div class="partners-logos">
          <img
            src="https://via.placeholder.com/150x60/CCCCCC/FFFFFF?text=Partner+1"
            alt="Partner 1 Logo"
          />
          <img
            src="https://via.placeholder.com/150x60/CCCCCC/FFFFFF?text=Partner+2"
            alt="Partner 2 Logo"
          />
          <img
            src="https://via.placeholder.com/150x60/CCCCCC/FFFFFF?text=Partner+3"
            alt="Partner 3 Logo"
          />
          <img
            src="https://via.placeholder.com/150x60/CCCCCC/FFFFFF?text=Partner+4"
            alt="Partner 4 Logo"
          />
          <img
            src="https://via.placeholder.com/150x60/CCCCCC/FFFFFF?text=Partner+5"
            alt="Partner 5 Logo"
          />
        </div>
      </div>

      <!-- Upcoming Events -->
      <div class="events-section">
        <h3 class="subsection-title">Événements à venir</h3>
        <ul class="events-list">
          <li class="event-item">
            <div class="event-date"><span>25</span>AOÛ</div>
            <div class="event-details">
              <h4>Masterclass : Financer son projet innovant</h4>
              <p>18:00 - Espace Conférence SELYN</p>
            </div>
            <a href="#" class="btn btn-outline">S'inscrire</a>
          </li>
          <li class="event-item">
            <div class="event-date"><span>12</span>SEP</div>
            <div class="event-details">
              <h4>Networking : La rencontre des entrepreneurs</h4>
              <p>19:00 - Rooftop SELYN</p>
            </div>
            <a href="#" class="btn btn-outline">Détails</a>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "CommunitySection",
};
</script>

<style scoped>
/* Scoped styles for the community section can go here */
</style>
