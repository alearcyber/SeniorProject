<script>
    import {onMount} from "svelte";
    import { page } from '$app/stores';

    //maps the section to what word should be displayed
    var section_name_map = {"main_orch": "Main Orchestra",
      "left_orch": "Left Orchestra",
      "right_orch": "Right Orchestra",
      "balc": "Balcony",
      "right_box": "Right Box",
      "left_box": "Left Box",
      "left_loge": "Left Loge",
      "right_loge": "Right Loge"}




    //get url params
    const url = $page.url;  //url
    const performance_id = url.searchParams.get('id')
    const performance_title = url.searchParams.get('title')



    let email = '';
    onMount(async () => {
        //grab the user's email
		email = sessionStorage.getItem('user');
		if (email === null) {
          alert('You need to be logged in first, please log in');
          window.location.href = '/';
        }
	});

    //FORM STUFF
    //option = section
    let options = ["main_orch", "left_orch", "right_orch", "balc", "right_box", "left_box", "left_loge", "right_loge"];
    let selectedOption = options[0];
    let number = '';
    let row = '';

    function handleSubmit() {
        //alert(`${number}, ${row}, ${selectedOption}`); //for testing, shows what user selected
        //TODO - Check that the seat actually exists. Only do this if it's needed


        //send the info as url parameters to the /frontdesk/seatinfo page
        var new_url = `/frontdesk/seatinfo?title=${performance_title}&id=${performance_id}&number=${number}&row=${row}&section=${selectedOption}`;
        window.location.href = new_url;

    }




</script>
<h1>Managing The Front Desk For {performance_title}</h1>

<h1>Insert information here</h1>

<form on:submit|preventDefault={handleSubmit}>
  <label>
    Section:
    <select bind:value={selectedOption}>
      {#each options as option}
        <option value={option}>{section_name_map[option]}</option>
      {/each}
    </select>
  </label>

  <label>
    Seat Number:
    <input type="text" bind:value={number}>
  </label>

  <label>
    Row:
    <input type="text" bind:value={row}>
  </label>

  <button type="submit">Submit</button>
</form>