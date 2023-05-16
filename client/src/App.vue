<script setup lang="ts">
import { capitalize } from 'vue'
import { RouterView, useRouter } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import FadeIn from '@/components/FadeIn.vue'

const getStarted = '/performance'
const navbar = {
  title: 'Alquant SWE',
  items: useRouter()
    .getRoutes()
    .filter((e) => e.path != '/')
    .map(({ path, name }) => ({ path, name: capitalize(name! as string) })),
  getStarted
}
</script>

<template>
  <NavBar v-bind="navbar" />
  <RouterView v-slot="{ Component }" :get-started="getStarted">
    <FadeIn> <component :is="Component" /></FadeIn>
  </RouterView>
</template>
