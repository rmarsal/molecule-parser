<template>
  <div class="App">
    <Header :title="'Molecule Parser'" />
    <div id="app">
        <img src="./assets/molecule.png">
    </div>
    <Search :search="state.search" @search="handleSearch" />
    <p class="App-intro">The atom composition of the molecule is the following:</p>
    <div class="molecules">
      <h2>{{state.molecules}}</h2>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  import VueCompositionApi from '@vue/composition-api';

  Vue.use(VueCompositionApi);
  import { reactive, watch } from '@vue/composition-api';
  import Header from './components/Header.vue';
  import Search from './components/Search.vue';

  export default {
    name: 'app',
    components: {
      Header, Search
    },
    setup() {
      const state = reactive({
        search: 'H2O',
        loading: true,
        molecules: {},
        errorMessage: null
      });

      watch(() => {
        const MOVIE_API_URL = `http://localhost:5000/parse/${state.search}`;

        fetch(MOVIE_API_URL)
          .then(response => response.json())
          .then(jsonResponse => {
            state.molecules = jsonResponse.Composition;
            state.loading = false;
          });
      });

      return {
        state,
        handleSearch(searchTerm) {
          state.loading = true;
          state.search = searchTerm;
        }
      };
    }
  }
</script>