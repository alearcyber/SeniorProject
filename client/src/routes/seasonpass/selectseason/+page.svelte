<style>

  button {
    background-color: #f0f0f0;
    border: none;
    border-radius: 4px;
    color: #333;
    cursor: pointer;
    font-size: 16px;
    margin: 8px;
    padding: 12px 24px;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #e0e0e0;
  }

  button.selected {
    background-color: #007bff;
    color: #fff;
  }

  button.selected:hover {
    background-color: #0069d9;
  }

  .container {
    display: flex;
    justify-content: center;
  }
</style>


<script>
  import Button from './Button.svelte';

  let seasons = [];
  let selectedSeason = null;

  async function fetchSeasons() {
    const response = await fetch('http://127.0.0.1:5000/get_upcoming_seasons');
    const data = await response.json();
    seasons = data.seasons;
  }


  function selectSeason(season) {
    selectedSeason = season;
  }

  fetchSeasons();


</script>
<div class="container">
  <h1>Select a Season</h1>

  <ul>
    {#each seasons as season}
      <li>
        <button on:click={() => selectSeason(season)}>{season.title} - {season.location} - {season.month}</button>
      </li>
    {/each}
  </ul>

  {#if selectedSeason}
    <p>You selected: {selectedSeason.title}</p>
    <Button to='/seasonpass/chooseperformances?season={selectedSeason.title}' text='click here to continue' />
  {/if}


</div>



