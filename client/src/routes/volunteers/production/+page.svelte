<!-- 
    Create Production Page
    This page is where the volunteers go to create a new production.
-->
<script>
	// @ts-nocheck

	import {
		Label,
		Input,
		Button,
		Radio,
		Textarea,
	} from 'flowbite-svelte';

	let production_info = {
		title: '',
		venue_id: '',
		org_id: '',
		image: '',
		description: '',
		duration: '',
		times: []
	};

	let values = [
		{
			title: '',
			date: '',
			time: '',
			seats: ''
		}
	];

	const addField = () => {
		values = [...values, { title: '', date: '', time: '', seats: '', sections: '' }];
	};

	const removeField = () => {
		values = values.slice(0, values.length - 1);
	};

	const venue_options = [
		{
			value: '1',
			text: 'Civic Center Concert Hall'
		},
		{
			value: '2',
			text: 'Civic Center Playhouse'
		}
	];

	let input;
	let container;
	let image;
	let showImage = false;

	let start_date_str, end_date;

	function onChange() {
		const file = input.files[0];
		production_info.image = file.name;

		if (file) {
			showImage = true;

			const reader = new FileReader();
			reader.addEventListener('load', function () {
				image.setAttribute('src', reader.result);
			});
			reader.readAsDataURL(file);
			console.log(file);

			return;
		}
		showImage = false;
	}

	async function create_production() {
        console.log("Creating production...")
		// Get org id from sessionStorage
		let org_id = sessionStorage.getItem('org_id');
		if (org_id != undefined) {
			production_info.org_id = parseInt(org_id);
		} else {
			console.error('Invalid organization ID');
		}

        console.log();
		// let response = await fetch('http://127.0.0.1/create_production', {
		// 	method: 'POST',
		// 	headers: {
		// 		Accept: 'application/json',
		// 		'Content-Type': 'application/json'
		// 	}
		// });
	}
</script>

<div class="mb-10 flex justify-center">
	<form class="flex flex-col space-y-6" style="width:800px" action="/">
		<!-- Title -->
		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create New Production</h3>

		<!-- Production Title Field -->
		<Label class="space-y-2">
			<span>Production Title</span>
			<Input
				type="text"
				name="production_name"
				placeholder=""
				bind:value={production_info.title}
				required
			/>
		</Label>

		<!-- Production Image Field -->
		<Label class="space-y-2">
			<h1>Production Image</h1>
			<input bind:this={input} on:change={onChange} type="file" />
			<div bind:this={container}>
				{#if showImage}
					<img style=" height:100px" bind:this={image} src="" alt="Preview" />
				{/if}
			</div>
		</Label>

		<!-- Venue Field -->
        <Label class="space-y-2">
            <span>Venue</span>
        </Label>
        <Radio name="venue" on:click={() => {production_info.venue_id = 1}}>Civic Center Concert Hall</Radio>
        <Radio name="venue" on:click={() => {production_info.venue_id = 2}}>Civic Center Playhouse</Radio>

		 <!-- Start Date Field -->
		<Label class="space-y-2">
			<span>Starting Date</span>
			<Input type="date" name="start_date" bind:value={start_date_str} required />
		</Label>

		<!-- End Date Field -->
		<Label class="space-y-2">
			<span>Ending Date</span>
			<Input type="date" name="end_date" bind:value={end_date} required />
		</Label>

        <!-- Description Field -->
        <Label class="space-y-2">
			<span>Description</span>
			<Textarea name="prod_desc" placeholder="A description of the types of shows in this production" required />
		</Label>

		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Performance</h3>

		<!-- Performance Field -->
		{#each values as v, i}
			<div>
				<Label class="space-y-2">
					<span>Date</span>
					<Input
						type="text"
						name="performance_date"
						bind:value={values[i].date}
						placeholder="MM/DD/YYYY"
						required
					/>
					<span>Time</span>
					<Input
						type="text"
						name="performance_time"
						bind:value={values[i].time}
						placeholder="X:XX p.m."
						required
					/>
					<span>Default Seat Price</span>
					<Input
						type="text"
						name="seat_price"
						bind:value={values[i].seats}
						placeholder="$"
						required
					/>

					<!-- Section Prices' Field -->
					<h3 class=" text-xl font-medium text-gray-900 dark:text-white p-0">Sections</h3>
					{#if production_info.venue_id == 1}
						<span>Orchestra Price</span>
						<Input
							type="text"
							name="orch_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Balcony Price</span>
						<Input
							type="text"
							name="balcony_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Loge Price</span>
						<Input
							type="text"
							name="loge_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Box Price</span>
						<Input
							type="text"
							name="box_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Handicap Price</span>
						<Input
							type="text"
							name="handicap_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
					{:else if production_info.venue_id == 2}
						<span>Orchestra Price</span>
						<Input
							type="text"
							name="orch_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Pit Price</span>
						<Input
							type="text"
							name="pit_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Lower Balcony Price</span>
						<Input
							type="text"
							name="lower_balcony_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Upper Balcony Price</span>
						<Input
							type="text"
							name="upper_balcony_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Loge Price</span>
						<Input
							type="text"
							name="loge_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
						<span>Handicap Price</span>
						<Input
							type="text"
							name="handicap_price"
							bind:value={values[i].sections}
							placeholder="$"
							required
						/>
					{/if}
				</Label>
			</div>
		{/each}
		{#if values.length >= 2}
			<Button style="width: 200px" color="light" on:click={removeField}>Remove Performance -</Button
			>
		{/if}
		<Button style="width: 200px" color="dark" on:click={addField}>Add Performance +</Button>

		<!-- Create Production button -->
		<Button class="w-full1" on:click={create_production}>Create Production</Button>
	</form>
</div>
