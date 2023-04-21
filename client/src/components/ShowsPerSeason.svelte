<script lang="ts">

    export let season: string; // Mutating this will cause function below to re-run
  
    $: showPromise = (async function getShowsBySeason(season: string) {
        // Assuming API has a route for ‘/seasons/{season}’
        // and ‘season’ is a url path param
        const res = await fetch(‘/seasons/‘ + season);
        const value = await res.json();

        return value;
    // Note IIFE call with id variable after closing the function below
    // This makes the promise reactive based on 'id'
    })(season)  
      
  </script>
    
  {#await showPromise }
      <p>...waiting</p>
  {:then shows}
      <p>{shows.length} Show</p>
  {:catch error}
      <p style="color: red">{error.message}</p>
  {/await}