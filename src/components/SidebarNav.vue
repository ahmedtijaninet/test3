<template>
  <div>
    <button
      class="mobile-nav-toggle"
      @click="toggleMobileNav"
      :aria-expanded="isMobileNavVisible.toString()"
      aria-controls="sidebar-nav"
    >
      <i class="fas" :class="isMobileNavVisible ? 'fa-times' : 'fa-bars'" aria-hidden="true"></i>
      <span class="sr-only">Menu</span>
    </button>
    <nav class="sidebar-nav" :class="{ 'is-visible': isMobileNavVisible }" id="sidebar-nav">
      <div class="logo">
        <RouterLink to="/">
          <img src="/SELYN.svg" alt="SELYN Logo" class="logo-svg" />
        </RouterLink>
      </div>
      <button
        class="horizontal-nav-toggle"
        @click="toggleHorizontalNav"
        :aria-expanded="isHorizontalNavVisible.toString()"
        aria-controls="nav-menu"
      >
        <i class="fas fa-bars" aria-hidden="true"></i>
        <span class="sr-only">Menu</span>
      </button>
      <ul id="nav-menu" :class="{ 'is-visible': isHorizontalNavVisible }">
        <li @click="closeNav"><RouterLink to="/"><i class="fas fa-home"></i> Accueil</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/consulting"><i class="fas fa-briefcase"></i> Selyn Conseil</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/suite"><i class="fas fa-rocket"></i> Selyn Suite</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/coworking"><i class="fas fa-building"></i> Selyn Space</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/offres"><i class="fas fa-tags"></i> Offres & Tarifs</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/communaute"><i class="fas fa-users"></i> Communauté</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/a-propos"><i class="fas fa-info-circle"></i> À propos</RouterLink></li>
        <li @click="closeNav"><RouterLink to="/contact"><i class="fas fa-envelope"></i> Contact</RouterLink></li>
      </ul>

      <button id="layout-toggle" title="Changer la mise en page" @click="toggleLayout">
        <i class="fas fa-exchange-alt"></i>
        <span class="layout-toggle-text">Changer la vue</span>
      </button>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const isMobileNavVisible = ref(false);
const isHorizontalNavVisible = ref(false);

const toggleMobileNav = () => {
  isMobileNavVisible.value = !isMobileNavVisible.value;
};

const toggleHorizontalNav = () => {
  isHorizontalNavVisible.value = !isHorizontalNavVisible.value;
};

const closeNav = () => {
  isMobileNavVisible.value = false;
  isHorizontalNavVisible.value = false;
};

const emit = defineEmits(['toggle-layout']);
const toggleLayout = () => {
  emit('toggle-layout');
};
</script>

<style scoped>
/* Scoped styles for the sidebar can go here if needed */
</style>
