<script setup lang="ts">
import { computed, ref } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
defineProps({
  title: String,
  items: Array<{ name: string; path: string }>,
  getStarted: { type: String, required: true }
})
const displayGetStarted = computed(() => useRoute().path === '/')
const dropdownOpen = ref(false)

const blurActiveElement = () => {
  if (document.activeElement) (document.activeElement as HTMLElement).blur()
}

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
  blurActiveElement()
}

const closeDropdown = () => {
  dropdownOpen.value = false
  blurActiveElement()
}
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown" :class="{ 'dropdown-open': dropdownOpen }">
        <label tabindex="0" class="btn btn-ghost lg:hidden" @click="toggleDropdown">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>
        </label>
        <ul
          tabindex="0"
          class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
        >
          <li v-for="item in items" :key="item.name" @click="closeDropdown">
            <RouterLink :to="item.path">{{ item.name }}</RouterLink>
          </li>
        </ul>
      </div>
      <RouterLink to="/" class="btn btn-ghost normal-case text-xl">{{ title }}</RouterLink>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li v-for="item in items" :key="item.name">
          <RouterLink :to="item.path">{{ item.name }}</RouterLink>
        </li>
      </ul>
    </div>
    <div class="navbar-end">
      <RouterLink v-show="displayGetStarted" :to="getStarted" class="btn">Get started</RouterLink>
    </div>
  </div>
</template>
