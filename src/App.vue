<template>
  <div>
    <div id="preloader" v-if="showPreloader" :class="{ 'preloader-fade-out': !isPreloaderVisible }">
      <img src="/SELYN.svg" alt="SELYN Logo" class="preloader-logo" />
      <div class="preloader-dots">
        <div class="dot dot-1"></div>
        <div class="dot dot-2"></div>
        <div class="dot dot-3"></div>
      </div>
    </div>
    <div id="app-container" :class="{ 'preloader-hidden': showPreloader }">
      <SidebarNav @toggle-layout="handleLayoutToggle" />
      <main class="main-content">
        <RouterView />
      </main>
      <SiteFooter />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import SidebarNav from './components/SidebarNav.vue';
import SiteFooter from './components/SiteFooter.vue';
import { RouterView } from 'vue-router';

export default {
  name: 'App',
  components: {
    SidebarNav,
    SiteFooter,
    RouterView,
  },
  setup() {
    const showPreloader = ref(false);
    const isPreloaderVisible = ref(true);

    const applyLayoutPreference = () => {
      const preferredLayout = localStorage.getItem('layout-preference');
      if (preferredLayout === 'horizontal') {
        document.body.classList.add('horizontal-layout');
      } else {
        document.body.classList.remove('horizontal-layout');
      }
    };

    const handleLayoutToggle = () => {
      const isHorizontal = document.body.classList.toggle('horizontal-layout');
      if (isHorizontal) {
        localStorage.setItem('layout-preference', 'horizontal');
      } else {
        localStorage.setItem('layout-preference', 'vertical');
      }
    };

    onMounted(() => {
      if (!sessionStorage.getItem('selyn-preloader-shown')) {
        showPreloader.value = true;
        setTimeout(() => {
          isPreloaderVisible.value = false;
          setTimeout(() => {
            showPreloader.value = false;
            sessionStorage.setItem('selyn-preloader-shown', 'true');
          }, 500); // fade-out duration
        }, 5000); // preloader display duration
      }
      applyLayoutPreference();
    });

    return {
      showPreloader,
      isPreloaderVisible,
      handleLayoutToggle,
    };
  },
};
</script>

<style>
/* Global styles can go here if needed, but most are in main.css and style.css */
.main-content {
  /* Basic layout styling to position the content next to the sidebar */
  /* This will likely need adjustment based on the final sidebar styles */
  margin-left: 250px; /* Example value, adjust as needed */
  padding: 1rem;
}

.preloader-hidden {
  display: none;
}
</style>
