<template>
  <div>
    <section
      class="confirmation-section"
      style="text-align: center; padding: 5rem 2rem"
    >
      <div class="container small-container">
        <i
          class="fas fa-check-circle"
          style="font-size: 5rem; color: #28a745; margin-bottom: 2rem"
        ></i>
        <h1 class="section-title">Merci pour votre confiance !</h1>
        <p>
          Votre commande a été traitée avec succès. Un e-mail de confirmation
          contenant les détails de votre abonnement vous a été envoyé.
        </p>
        <p>Bienvenue dans la communauté SELYN !</p>
        <a
          href="index.html"
          class="btn btn-secondary"
          style="margin-top: 2rem"
          >Retour à l'accueil</a
        >
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ConfirmationView',
};
</script>
