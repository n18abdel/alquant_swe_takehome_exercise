<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import router from './router'
import { capitalize } from 'vue'
const getStarted = '/performance'
const navbar = {
  title: 'Alquant SWE',
  items: router
    .getRoutes()
    .filter((e) => e.path != '/')
    .map(({ path, name }) => ({ path, name: capitalize(name! as string) })),
  getStarted
}
</script>

<template>
  <NavBar v-bind="navbar" />
  <RouterView :get-started="getStarted" />
</template>
