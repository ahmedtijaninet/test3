<template>
  <section id="accueil" class="hero-section">
    <div class="hero-content">
      <h1>
        Une transformation globale, portée par l’intelligence, l’expertise et
        l’espace.
      </h1>

      <!-- Poles Slider -->
      <div id="poles-slider" class="poles-slider">
        <div class="slider-container" :style="{ transform: `translateX(${sliderTransform}px)` }">
          <!-- Slide 1: Consulting -->
          <RouterLink to="/consulting" class="pole-slide-link pole-conseil">
            <div class="pole-slide">
              <div class="pole-card">
                <i class="fas fa-briefcase card-icon"></i>
                <h3>Selyn Conseil</h3>
                <p>
                  Un accompagnement stratégique complet pour transformer vos
                  ambitions en succès.
                </p>
              </div>
            </div>
          </RouterLink>
          <!-- Slide 2: SELYN Suite -->
          <RouterLink to="/suite" class="pole-slide-link pole-suite">
            <div class="pole-slide">
              <div class="pole-card">
                <i class="fas fa-rocket card-icon"></i>
                <h3>Selyn Suite</h3>
                <p>
                  Pilotez toute votre entreprise depuis une seule plateforme
                  évolutive et intelligente.
                </p>
              </div>
            </div>
          </RouterLink>
          <!-- Slide 3: Coworking -->
          <RouterLink to="/coworking" class="pole-slide-link pole-space">
            <div class="pole-slide">
              <div class="pole-card">
                <i class="fas fa-users card-icon"></i>
                <h3>Selyn Space</h3>
                <p>
                  Un environnement de travail moderne et connecté pour inspirer
                  l'innovation.
                </p>
              </div>
            </div>
          </RouterLink>
        </div>
        <button class="slider-btn prev" @click="prevSlide" :disabled="currentIndex === 0">
          <i class="fas fa-chevron-left"></i>
        </button>
        <button class="slider-btn next" @click="nextSlide" :disabled="currentIndex >= totalSlides - visibleSlides">
          <i class="fas fa-chevron-right"></i>
        </button>
      </div>

      <p class="subtitle">
        Découvrez un écosystème connecté où vos idées prennent vie.
      </p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import { RouterLink } from 'vue-router';

const currentIndex = ref(0);
const totalSlides = 3;
const sliderTransform = ref(0);
const visibleSlides = ref(3);

const getVisibleSlides = () => {
  return window.innerWidth <= 768 ? 1 : 3;
};

const updateSliderPosition = () => {
  const slideWidth = document.querySelector('.pole-slide-link')?.getBoundingClientRect().width || 0;

  if (window.innerWidth <= 768) {
    sliderTransform.value = -currentIndex.value * slideWidth;
  } else {
    sliderTransform.value = 0;
  }

  visibleSlides.value = getVisibleSlides();
};

const nextSlide = () => {
  if (currentIndex.value < totalSlides - visibleSlides.value) {
    currentIndex.value++;
    updateSliderPosition();
  }
};

const prevSlide = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
    updateSliderPosition();
  }
};

const handleResize = () => {
  currentIndex.value = 0;
  updateSliderPosition();
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
  updateSliderPosition();
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
/* Scoped styles for the hero section can go here */
.slider-container {
  transition: transform 0.3s ease-in-out;
}
</style>
