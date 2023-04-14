<!-- 
    Create Production Page
    This page is where the volunteers go to create a new production.
-->
<script>
	// @ts-nocheck

	import {
		Label,
		Input,
		Textarea,
		Button,
		Card,
		Heading,
		List,
		DescriptionList
	} from 'flowbite-svelte';

    let production_info = {
        title: "",
        venue_id: "",
        org_id: "",
        image: "",
        description: "",
        duration: "",
        times: [],
    }

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
	let venue_input;

	let input;
	let container;
	let image;
	let placeholder;
	let showImage = false;

	function onChange() {
		const file = input.files[0];

		if (file) {
			showImage = true;

			const reader = new FileReader();
			reader.addEventListener('load', function () {
				image.setAttribute('src', reader.result);
			});
			reader.readAsDataURL(file);

			return;
		}
		showImage = false;
	}

	async function create_production() {
		let response = await fetch('http://127.0.0.1/create_production', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			}
		});
	}
</script>

<div class="mb-10 flex justify-center">
	<form class="flex flex-col space-y-6" style="width:800px" action="/">
		<!-- Title -->
		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create New Production</h3>

		<!-- Production Title Field -->
		<Label class="space-y-2">
			<span>Production Title</span>
			<Input type="text" name="production_name" placeholder="" required />
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
			<Input
				type="text"
				name="venue"
				bind:value={venue_input}
				placeholder="Civic Center Playhouse"
				required
			/>
		</Label>

		<!-- Start Date Field -->
		<Label class="space-y-2">
			<span>Starting Date</span>
			<Input type="text" name="start_date" placeholder="MM/DD/YYYY" required />
		</Label>

		<!-- End Date Field -->
		<Label class="space-y-2">
			<span>Ending Date</span>
			<Input type="text" name="end_date" placeholder="MM/DD/YYYY" required />
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
					{#if venue_input == 'Civic Center Playhouse'}
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
					{:else if venue_input == 'Civic Center Concert Hall'}
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
		<Button type="submit" class="w-full1">Create Production</Button>
	</form>
</div>
