<!-- 
    Navigation Bar Component 
    This component has the logo, navigation bar links, and the login.
-->
<script>
	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		Button,
		Input,
		Modal,
		Label,
		Checkbox
	} from 'flowbite-svelte';
	import { page } from '$app/stores';
	import { writable } from 'svelte/store';
	import { onMount } from 'svelte';

	let email = '';
	var org_id = '';

  // Triggered when page is loaded
	onMount(async () => {
		console.log('This is onMount');
		let val = sessionStorage.getItem('user');
		if (val === null) {
			console.log('User is not logged in');
			is_logged_in = false;
		} else {
			console.log('User is logged in');
			is_logged_in = true;
			email = val;
		}
	});

	// Returns the id of the organization the user is a part of if they are a volunteer.
	// If they're a normal user, returns <empty string>
	async function is_volunteer() {
		let vol_response = await fetch('http://127.0.0.1:5000/is_volunteer', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ email: email })
		});

		const out = await vol_response.json();
		console.log(out['org_id']);
	}

	// Data struct to hold login info
	let login_info = {
		email: '',
		password: ''
	};

	// --------------
	// LOGIN ACTIONS
	// --------------
	async function login_request() {
		// Make a POST request to the server with the login info
		let response = await fetch('http://127.0.0.1:5000/login', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(login_info)
		});
		const out = await response.json();

		// The server returns either the user's first name or "fail".
		// If a name came through, set the session variable and first name and
		// close the window.
		// In either case, set the variables that will be used to control the
		// window's items.
		if (out != 'fail') {
			valid_email_passw = true;
			is_logged_in = true;
			is_logging_in = false;
			sessionStorage.setItem('user', login_info.email);
			email = login_info.email;

			// Check if the user is a volunteer
			let vol_response = await fetch('http://127.0.0.1:5000/is_volunteer', {
				method: 'POST',
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ email: email })
			});

      // Get the organization id
			const vol_out = await vol_response.json();
      console.log("vol_out.org_id: ", vol_out['org_id']);
      sessionStorage.setItem("org_id", vol_out['org_id']);

      // Reload the page
			window.location.href = '/';

			console.log(`${out[0]} logged in`);
		} else {
			valid_email_passw = false;
			is_logged_in = false;
			is_logging_in = true;
		}
	}

	// Data struct to hold signup info
	let signup_info = {
		fname: '',
		lname: '',
		email: '',
		password: '',
		venue_id: '',
		level: 0
	};

	// -----------------------
	// CREATE ACCOUNT ACTIONS
	// -----------------------
	async function signup_request() {
		// Check to see if passwords match.
		// If not, alert user and prevent account creation.
		if (password === confirm_password) {
			signup_info.password = password;
		} else {
			alert('Passwords do not match');
			return -1;
		}

		// If there's nothing in the venue field, the user is a normal user (level 1).
		// If the user did type a venue ID, they're a volunteer (level 2).
		// This can likely be moved serverside.
		if (signup_info.venue_id == '') {
			signup_info.level = 1;
		} else {
			signup_info.level = 2;
		}

		// Make a request to the server with the signup info
		let response = await fetch('http://127.0.0.1:5000/signup', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(signup_info)
		});

		// Wait for the response from the server
		const out = await response.json();

		// If the account already exists, alert the user. The server has already
		// prevented the account from being created.
		// Otherwise, set a session variable to the user's email so they remain
		// logged in throughout their session.
		if (out === 'account_exists') {
			does_email_exist = true;
			return out;
		} else if (out === 'invalid_email') {
			is_valid_email = false;
			return out;
		} else {
			does_email_exist = false;
			is_valid_email = true;
			sessionStorage.setItem('user', signup_info.email);
			is_creating_acct = false; // Closes the modal window
			is_logged_in = true;
			first_name = signup_info.fname;
		}

		return out;
	}

	// When user logs out, unset the appropriate variables
	function logout() {
		is_logged_in = false;
		sessionStorage.removeItem('user');
		sessionStorage.removeItem('org_id');
		first_name = '';
		window.location.href = '/';
	}

	let is_logging_in = false;
	let is_creating_acct = false;
	let does_email_exist = false;
	let is_valid_email = true;
	let valid_email_passw = true;
	let is_logged_in = false;

	let password = '';
	let confirm_password = '';

	let first_name = '';
</script>

<Navbar let:hidden let:toggle>
	<!-- Logo -->
	<NavBrand href="/">
		<img src="../logo.jpeg" class="mr-3 h-24 sm:h-24" alt="Huntsville Civic Center Logo" />
	</NavBrand>

	<!-- Login Button and Form -->
	<div class="flex flex-row md:order-2 items-center">
		<Label class="text-lg pr-4"
			>{#if email != ''}Hey, {email}!{:else}{email}{/if}</Label
		>
		{#if !is_logged_in}
			<Button on:click={() => (is_logging_in = true)}>Log In</Button>
		{:else}
			<Button on:click={logout}>Sign out</Button>
		{/if}
		<Modal bind:open={is_logging_in} size="xs" autoclose={false} class="w-full">
			<form class="flex flex-col space-y-6" method="POST" on:submit|preventDefault={login_request}>
				<!-- Title -->
				<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Sign in</h3>

				<!-- Email field -->
				<Label class="space-y-2">
					<span>Email</span>
					<Input
						type="email"
						name="email"
						placeholder="name@company.com"
						bind:value={login_info.email}
						required
					/>
				</Label>

				<!-- Password field -->
				<Label class="space-y-2">
					<span>Your password</span>
					<Input
						type="password"
						name="password"
						placeholder="••••••••••"
						bind:value={login_info.password}
						required
					/>
				</Label>

				<Label class="foo space-y-2">
					{#if !valid_email_passw}
						<span style="color: red"
							>This email/password combination does not exist in our records</span
						>
					{/if}
				</Label>

				<!-- Login button -->
				<Button type="submit" class="w-full1" on:click={login_request}>Login to your account</Button
				>

				<!-- Create an account link -->
				<div class="text-sm font-medium text-gray-500 dark:text-gray-300">
					Not registered? <a
						href="/"
						on:click={() => {
							is_logging_in = false;
							is_creating_acct = true;
						}}
						class="text-blue-700 hover:underline dark:text-blue-500">Create account</a
					>
				</div>
			</form>
		</Modal>

		<!-- Create Account form -->
		<Modal bind:open={is_creating_acct} size="xs" autoclose={false} class="w-full">
			<form class="flex flex-col space-y-6" action="#">
				<!-- Title -->
				<h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create an Account</h3>

				<!-- First Name Field -->
				<Label class="space-y-2">
					<span>First Name</span>
					<Input
						type="text"
						name="create_firstname"
						placeholder="Michael"
						bind:value={signup_info.fname}
						required
					/>
				</Label>

				<!-- Last Name Field -->
				<Label class="space-y-2">
					<span>Last Name</span>
					<Input
						type="text"
						name="create_lastname"
						placeholder="Scott"
						bind:value={signup_info.lname}
						required
					/>
				</Label>

				<!-- Email Field -->
				<Label class="space-y-2">
					<span>Email</span>
					<Input
						type="email"
						name="create_email"
						placeholder="name@company.com"
						bind:value={signup_info.email}
						required
					/>
				</Label>
				<!-- Let the user know if that email already exists in the database -->
				<Label class="foo space-y-2">
					{#if does_email_exist}
						<span style="color: red">A user account with that email already exists</span>
					{/if}
				</Label>
				<Label class="foo space-y-2">
					{#if !is_valid_email}
						<span style="color: red">Please enter a valid email</span>
					{/if}
				</Label>

				<!-- Password field -->
				<Label class="space-y-2">
					<span>Password</span>
					<Input
						type="password"
						name="create_password"
						placeholder="••••••••••"
						bind:value={password}
						required
					/>
				</Label>

				<!-- Confirm password field -->
				<Label class="space-y-2">
					<span>Confirm Password</span>
					<Input
						type="password"
						name="confirm_password"
						placeholder="••••••••••"
						bind:value={confirm_password}
						required
					/>
				</Label>
				<!-- Let the user know whether or not the passwords match-->
				<Label class="foo space-y-2">
					{#if password.length > 0}
						{#if password === confirm_password}
							<span style="color: green">Passwords match</span>
						{:else}
							<span style="color: red">Passwords do not match</span>
						{/if}
					{/if}
				</Label>

				<!-- Venue ID Field -->
				<Label class="space-y-2">
					<span>Venue ID (optional)</span>
					<Input type="text" name="venue_id" bind:value={signup_info.venue_id} />
				</Label>

				<!-- Create Account button -->
				<Button type="submit" class="w-full1" on:click={signup_request}>Create Account</Button>
			</form>
		</Modal>
	</div>

	<!-- Navigation Bar -->
	<NavUl {hidden} class="order-1">
		<NavLi href="/" active={$page.url.pathname === '/'}>HOME</NavLi>
		<NavLi href="/shows" active={$page.url.pathname === '/shows'}>SHOWS</NavLi>
		<NavLi href="/tickets" active={$page.url.pathname === '/tickets'}>BUY TICKETS</NavLi>
		<NavLi href="/help" active={$page.url.pathname === '/contact'}>HELP</NavLi>
		<NavLi href="/volunteers" active={$page.url.pathname === '/contact'}>VOLUNTEERS</NavLi>
	</NavUl>
</Navbar>
