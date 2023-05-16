<script setup lang="ts">
import useDataFetch from '@/composables/useDataFetch'
import DataLoader from '@/components/DataLoader.vue'
import DataTable from '@/components/DataTable.vue'
import { type TableData } from '@/components/DataTable.vue'

type StatsData = {
  [symbol: string]: {
    [stat: string]: number
  }
}

const { data, isLoading, error } = useDataFetch<StatsData>('/stocks/statistics')
const errorMessage = 'Error! Could not retrieve statistics data.'
</script>

<template>
  <DataLoader v-bind="{ isLoading, error, errorMessage }"
    ><DataTable v-if="data" :data="(data as TableData)"
  /></DataLoader>
</template>
