<!-- 
    Create Season Page
    This page is where the volunteers go to create a new season.
-->
<script>
    import { Label, Input, Button, Listgroup, Checkbox, Textarea } from 'flowbite-svelte'
    import { onMount } from 'svelte';

    onMount(async () => {
		console.log('This is onMount for the Create Season page');
		console.log(get_production_list());
	});

	let list = [{}]
    let production_names = [{ name: "Placeholder production" }]
	let production_ids = [0];

    let org_name = "";

	// This info will be passed into the database
    let season_info = {
        org_id: '',
        title: '',
        description: '',
        productions: [],
    }
    let selected = [0];

    async function get_production_list() {
		// Get session vars about user
        let email = sessionStorage.getItem("user");
        let org_id = sessionStorage.getItem("org_id");
        console.log(email, org_id);

		// Get production list from server
        let response = await fetch(`http://127.0.0.1:5000/get_productions/${email}:${org_id}`);
        const out = await response.json();
        console.log(out);
		
		// Make local vars with the production data so they're easier to access
		production_names = [];
		production_ids = [];
		list = out['production_list'];
		for (let i in list) {
			production_names.push(out['production_list'][i][1]);
			production_ids.push(out['production_list'][i][0]);
		}

        org_name = out['org_name'];

        return out
    }
    
    async function create_season() {

        let org_id = sessionStorage.getItem("org_id");
		if (org_id != null) season_info.org_id = org_id;

		let response = await fetch('http://127.0.0.1:5000/create_season', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(season_info)
		});
		const out = await response.json();
		console.log(out);
		alert(`${season_info.title} season created.`);
		location.reload();
    }

    
</script>

<div class="mb-10 flex justify-center">
	<form class="flex flex-col space-y-6" style="width:800px" action="/">
		<!-- Title -->
		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create New Season</h3>

		<!-- Season Name Field -->
		<Label class="space-y-2">
			<span>Season Name</span>
			<Input type="text" name="season_name" bind:value={season_info.title} placeholder="" required />
		</Label>

        <!-- Description Field -->
		<Label class="space-y-2">
			<span>Description</span>
			<Textarea
				name="prod_desc"
				placeholder="A description of the types of shows in this season"
				bind:value={season_info.description}
				required
			/>
		</Label>

		<!-- Organization Field -->
		<Label class="space-y-2">
			<span>Organization: {org_name}</span>
		</Label>

		<!-- Production List -->
		<Label class="space-y-2">
			<span> Production List</span>
			{#each production_names as item, p}
				<div class="d-flex justify-space-around">
					<input type="checkbox" value={production_ids[p]} bind:group={season_info.productions} />
					{item}<br />
				</div>
			{/each}
		</Label>

		<!-- Create Season button -->
		<Button class="w-full1" on:click={create_season}>Create Season</Button>
	</form>
</div>
