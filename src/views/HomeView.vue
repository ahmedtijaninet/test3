<template>
  <div>
    <HeroSection />
    <PricingSection />
    <CommunitySection />
  </div>
</template>

<script>
import HeroSection from '@/components/HeroSection.vue';
import PricingSection from '@/components/PricingSection.vue';
import CommunitySection from '@/components/CommunitySection.vue';

export default {
  name: 'HomeView',
  components: {
    HeroSection,
    PricingSection,
    CommunitySection,
  },
};
</script>
