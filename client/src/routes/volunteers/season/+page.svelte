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

    //hard coded event data that will eventually be received from database
    let list = [{ name: "Placeholder production" }]

    let org_name = "";

    let season_info = {
        org_id: '',
        season_name: '',
        description: '',
        productions: [],
    }
    let selected = [""];

    async function get_production_list() {
        let email = sessionStorage.getItem("user");
        let org_id = sessionStorage.getItem("org_id");
        console.log(email, org_id);

        let response = await fetch(`http://127.0.0.1:5000/get_productions/${email}:${org_id}`);
        const out = await response.json();
        console.log(out['production_list']);
        list = out['production_list'];
        org_name = out['org_name'];
        return out
    }
    
    async function create_season() {
        console.log(selected);
    }

    
</script>

<div class="mb-10 flex justify-center">
	<form class="flex flex-col space-y-6" style="width:800px" action="/">
		<!-- Title -->
		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create New Season</h3>

		<!-- Season Name Field -->
		<Label class="space-y-2">
			<span>Season Name</span>
			<Input type="text" name="season_name" bind:value={season_info.season_name} placeholder="" required />
		</Label>

		<!-- Organization Field -->
		<Label class="space-y-2">
			<span>Organization: {org_name}</span>
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


		<!-- Production List -->
		<Label class="space-y-2">
			<span> Production List</span>
			{#each list as item, i}
				<div class="d-flex justify-space-around">
					<Checkbox group={selected} value={item.name} />
					{item}<br />
				</div>
			{/each}
		</Label>

		<!-- Create Season button -->
		<Button class="w-full1" on:click={create_season}>Create Season</Button>
	</form>
</div>
