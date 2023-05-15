<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
import { capitalize } from 'vue'
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
    <Transition
      enter-from-class="opacity-0"
      leave-to-class="opacity-0"
      enter-active-class="transition duration-300"
      leave-active-class="transition duration-300"
    >
      <component :is="Component" />
    </Transition>
  </RouterView>
</template>
