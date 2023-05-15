<script setup lang="ts">
import { RouterLink } from 'vue-router'
defineProps({
  title: String,
  content: String,
  getStarted: { type: String, required: true }
})
</script>

<template>
  <div class="hero min-h-screen bg-base-200">
    <div class="hero-content text-center">
      <div class="max-w-md md:max-w-none">
        <h1 class="text-5xl font-bold">{{ title }}</h1>
        <p class="py-6">
          {{ content }}
        </p>
        <RouterLink :to="getStarted" class="btn btn-primary">Get started</RouterLink>
      </div>
    </div>
  </div>
</template>
