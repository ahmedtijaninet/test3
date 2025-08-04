<template>
  <div>
    <section class="checkout-section">
      <div class="container">
        <h1 class="section-title">Finaliser votre commande</h1>
        <div class="checkout-layout">
          <div class="checkout-form">
            <h3>Informations de facturation</h3>
            <form id="payment-form" @submit.prevent="submitPayment">
              <label for="fullname" class="sr-only">Nom complet</label>
              <input
                type="text"
                id="fullname"
                placeholder="Nom complet"
                required
              />
              <label for="email" class="sr-only">Adresse e-mail</label>
              <input
                type="email"
                id="email"
                placeholder="Adresse e-mail"
                required
              />
              <label for="company" class="sr-only">Nom de l'entreprise</label>
              <input
                type="text"
                id="company"
                placeholder="Nom de l'entreprise (facultatif)"
              />

              <h3 style="margin-top: 2rem">Informations de paiement</h3>
              <div id="card-element">
                <!-- Placeholder for credit card details -->
                <label for="card-number" class="sr-only"
                  >Numéro de carte</label
                >
                <input
                  type="text"
                  id="card-number"
                  placeholder="Numéro de carte"
                />
                <div class="card-details">
                  <label for="expiry-date" class="sr-only"
                    >Date d'expiration</label
                  >
                  <input
                    type="text"
                    id="expiry-date"
                    placeholder="MM/AA"
                  />
                  <label for="cvc" class="sr-only">CVC</label>
                  <input type="text" id="cvc" placeholder="CVC" />
                </div>
              </div>

              <button
                type="submit"
                class="btn btn-secondary"
                style="width: 100%; margin-top: 2rem"
              >
                Confirmer et Payer
              </button>
            </form>
          </div>
          <div class="order-summary">
            <h3>Résumé de la commande</h3>
            <div class="summary-item">
              <span>Offre</span>
              <span id="offer-name">{{ offerName }}</span>
            </div>
            <div class="summary-item">
              <span>Prix</span>
              <span id="offer-price">{{ offerPrice }} DH/mois</span>
            </div>
            <hr />
            <div class="summary-item total">
              <span>Total</span>
              <span id="total-price">{{ offerPrice }} DH</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const offerName = ref('Non sélectionnée');
const offerPrice = ref('N/A');

onMounted(() => {
  offerName.value = route.query.offer || 'Non sélectionnée';
  offerPrice.value = route.query.price || 'N/A';
});

const submitPayment = () => {
  // In a real app, you would process the payment here
  router.push('/confirmation');
};
</script>
