<script setup lang="ts">
import { RouterLink } from 'vue-router'
defineProps({
  title: String,
  items: Array<{ name: string; path: string }>,
  getStarted: { type: String, required: true }
})
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <label tabindex="0" class="btn btn-ghost lg:hidden">
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
          <li v-for="item in items" :key="item.name">
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
      <RouterLink :to="getStarted" class="btn">Get started</RouterLink>
    </div>
  </div>
</template>
