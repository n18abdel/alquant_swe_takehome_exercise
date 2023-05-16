import { ref, watch } from 'vue'

export default function useStartDate(
  initialDate: string,
  fetchData: (
    params: string | Record<string, string> | URLSearchParams | string[][] | undefined
  ) => void
) {
  const startDate = ref(initialDate)

  watch(startDate, (newValue) => {
    fetchData({ start: newValue })
  })

  return startDate
}
