<script setup lang="ts">
import useDataFetch from '@/composables/useDataFetch'
import useStartDate from '@/composables/useStartDate'
import DatePickerWrapper from '@/components/DatePickerWrapper.vue'
import DataLoader from '@/components/DataLoader.vue'
import DataTable from '@/components/DataTable.vue'
import { type TableData } from '@/components/DataTable.vue'

type StatsData = {
  [symbol: string]: {
    [stat: string]: number
  }
}

const initialDate = new Date(new Date().getFullYear() - 1, 0, 1).toLocaleDateString('fr-ca')
const { data, fetchData, isLoading, error } = useDataFetch<StatsData>('/stocks/statistics', {
  start: initialDate
})
const errorMessage = 'Error! Could not retrieve statistics data.'
const startDate = useStartDate(initialDate, fetchData)
</script>

<template>
  <DatePickerWrapper v-model="startDate">
    <DataLoader v-bind="{ isLoading, error, errorMessage }">
      <DataTable v-if="data" :data="(data as TableData)" />
    </DataLoader>
  </DatePickerWrapper>
</template>
