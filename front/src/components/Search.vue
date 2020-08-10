<template>
  <form class="search">
    <input
       type="text"
       :value="moleculeFormula"
       @keyup="handleChange"
    />
    <input @click="handleSubmit" type="submit" value="SEARCH" />
  </form>
</template>

<script>
  import { ref } from '@vue/composition-api';

  export default {
    name: 'Search',
    props: ['search'],
    setup({ search }, { emit }) {
      const moleculeFormula = ref(search);

      return {
        moleculeFormula,
        handleSubmit(event) {
          event.preventDefault();
          emit('search', moleculeFormula.value);
        },
        handleChange(event) {
          moleculeFormula.value = event.target.value
        }
      }
    }
  };
</script>