<!-- 
    Create Production Page
    This page is where the volunteers go to create a new production.
-->
<script>
	// @ts-nocheck

	import { Label, Input, Button, Radio, Textarea } from 'flowbite-svelte';

	let production_info = {
		title: '',
		venue_id: 2,
		org_id: '',
		image: '',
		description: '',
		duration: 0,
		times: [],
		performances: []
	};

	let performances = [
		{
			title: '',
			date: '',
			time: '',
			seats: '',
			default_price: '',
			section_prices: {
				orchestra: '',
				balcony: '',
				loge: '',
				box: '',
				handicap: '',
				pit: '',
				lower_balcony: '',
				upper_balcony: ''
			}
		}
	];

	const addField = () => {
		performances = [
			...performances,
			{
				title: '',
				date: '',
				time: '',
				default_price: '',
				section_prices: {
					orchestra: '',
					balcony: '',
					loge: '',
					box: '',
					handicap: '',
					pit: '',
					lower_balcony: '',
					upper_balcony: ''
				}
			}
		];
	};

	const removeField = () => {
		performances = performances.slice(0, performances.length - 1);
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
	let image_file;
	let showImage = false;

	let start_date_str, end_date_str;

	function onChange() {
		// Set image filename
		const file = input.files[0];
		image_file = file;
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
		console.log('Creating production...');

		// Get org id from sessionStorage
		let org_id = sessionStorage.getItem('org_id');
		if (org_id != undefined) {
			production_info.org_id = parseInt(org_id);
		} else {
			console.error('Invalid organization ID');
		}

		// Calculate days between the dates
		let start_date = Date.parse(start_date_str);
		let end_date = Date.parse(end_date_str);
		production_info.duration = (end_date - start_date) / 8.64e7;

		// Record each performance
		for (let i in performances) {
			let performance_date = new Date(performances[i].date + ' ' + performances[i].time);
			production_info.times.push(performance_date.toISOString());
		}

		production_info.performances = performances;

		console.log(production_info);

		let response = await fetch('http://127.0.0.1:5000/create_production', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(production_info)
		});

		const out = await response.json();
		console.log(out);
		return out;
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
		<Radio
			name="venue"
			selected="false"
			on:click={() => {
				production_info.venue_id = 1;
			}}>Civic Center Concert Hall</Radio
		>
		<Radio
			name="venue"
			selected="false"
			on:click={() => {
				production_info.venue_id = 2;
			}}>Civic Center Playhouse</Radio
		>

		<!-- Start Date Field -->
		<Label class="space-y-2">
			<span>Starting Date</span>
			<Input type="date" name="start_date" bind:value={start_date_str} required />
		</Label>

		<!-- End Date Field -->
		<Label class="space-y-2">
			<span>Ending Date</span>
			<Input type="date" name="end_date" bind:value={end_date_str} required />
		</Label>

		<!-- Description Field -->
		<Label class="space-y-2">
			<span>Description</span>
			<Textarea
				name="prod_desc"
				placeholder="A description of the types of shows in this production"
				bind:value={production_info.description}
				required
			/>
		</Label>

		<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Performance</h3>

		<!-- Performance Field -->
		{#each performances as v, i}
			<div>
				<Label class="space-y-2">
					<span>Date</span>
					<Input
						type="date"
						name="performance_date"
						bind:value={performances[i].date}
						placeholder="MM/DD/YYYY"
						required
					/>
					<span>Time</span>
					<Input
						type="time"
						name="performance_time"
						bind:value={performances[i].time}
						placeholder="X:XX p.m."
						required
					/>
					<span>Default Seat Price</span>
					<Input
						type="number"
						name="seat_price"
						bind:value={performances[i].default_price}
						placeholder="$"
						required
					/>

					<!-- Section Prices' Field -->
					<h3 class=" text-xl font-medium text-gray-900 dark:text-white p-0">Sections</h3>
					{#if production_info.venue_id == 1}
						<span>Orchestra Price</span>
						<Input
							type="number"
							name="orch_price"
							bind:value={performances[i].section_prices.orchestra}
							placeholder="$"
							required
						/>
						<span>Balcony Price</span>
						<Input
							type="text"
							name="balcony_price"
							bind:value={performances[i].section_prices.balcony}
							placeholder="$"
							required
						/>
						<span>Loge Price</span>
						<Input
							type="text"
							name="loge_price"
							bind:value={performances[i].section_prices.loge}
							placeholder="$"
							required
						/>
						<span>Box Price</span>
						<Input
							type="text"
							name="box_price"
							bind:value={performances[i].section_prices.box}
							placeholder="$"
							required
						/>
						<span>Handicap Price</span>
						<Input
							type="text"
							name="handicap_price"
							bind:value={performances[i].section_prices.handicap}
							placeholder="$"
							required
						/>
					{:else if production_info.venue_id == 2}
						<span>Orchestra Price</span>
						<Input
							type="text"
							name="orch_price"
							bind:value={performances[i].section_prices.orchestra}
							placeholder="$"
							required
						/>
						<span>Pit Price</span>
						<Input
							type="text"
							name="pit_price"
							bind:value={performances[i].section_prices.pit}
							placeholder="$"
							required
						/>
						<span>Lower Balcony Price</span>
						<Input
							type="text"
							name="lower_balcony_price"
							bind:value={performances[i].section_prices.lower_balcony}
							placeholder="$"
							required
						/>
						<span>Upper Balcony Price</span>
						<Input
							type="text"
							name="upper_balcony_price"
							bind:value={performances[i].section_prices.upper_balcony}
							placeholder="$"
							required
						/>
						<span>Loge Price</span>
						<Input
							type="text"
							name="loge_price"
							bind:value={performances[i].section_prices.loge}
							placeholder="$"
							required
						/>
						<span>Handicap Price</span>
						<Input
							type="text"
							name="handicap_price"
							bind:value={performances[i].section_prices.handicap}
							placeholder="$"
							required
						/>
					{/if}
				</Label>
			</div>
		{/each}
		{#if performances.length >= 2}
			<Button style="width: 200px" color="light" on:click={removeField}>Remove Performance -</Button
			>
		{/if}
		<Button style="width: 200px" color="dark" on:click={addField}>Add Performance +</Button>

		<!-- Create Production button -->
		<Button class="w-full1" on:click={create_production}>Create Production</Button>
	</form>
</div>
