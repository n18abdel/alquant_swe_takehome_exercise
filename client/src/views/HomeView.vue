<script setup lang="ts">
import CenteredHero from '../components/CenteredHero.vue'
const props = defineProps({
  getStarted: { type: String, required: true }
})

const hero = {
  title: 'Invest with Confidence',
  content: 'Explore and compare the performance and statistics of popular stocks here.',
  getStarted: props.getStarted
}
</script>

<template>
  <CenteredHero v-bind="hero" />
</template>
