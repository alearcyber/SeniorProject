<!-- 
    Navigation Bar Component 
    This component has the logo, navigation bar links, and the login.
-->

<script>
    import { Navbar, NavBrand, NavLi, NavUl, Button, Input, Modal, Label, Checkbox } from 'flowbite-svelte'
    import { page } from '$app/stores'

    let is_login = false 
    let is_creating_acct = false;

    let password = "";
    let confirm_password = "";
</script>

<Navbar let:hidden let:toggle>
    <!-- Logo -->
    <NavBrand href="/">
      <img
        src="../logo.jpeg"
        class="mr-3 h-24 sm:h-24"
        alt="Huntsville Civic Center Logo"
      />
    </NavBrand>

    <!-- Login Button and Form -->
    <div class="flex md:order-2"> 
      <Button on:click={() => is_login = true}>Login</Button>  <!-- Clicking on Login Button opens form -->
      <Modal bind:open={is_login} size="xs" autoclose={false} class="w-full">
        <form class="flex flex-col space-y-6" action="#">
          <!-- Title -->
          <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Sign in</h3>

          <!-- Email field -->
          <Label class="space-y-2">
            <span>Email</span>
            <Input type="email" name="email" placeholder="name@company.com" required />
          </Label>

          <!-- Password field -->
          <Label class="space-y-2">
            <span>Your password</span>
            <Input type="password" name="password" placeholder="••••••••••" required />
          </Label>

          <!-- Login button -->
          <Button type="submit" class="w-full1">Login to your account</Button>

          <!-- Create an account link -->
          <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
            Not registered? <a href="/" on:click={() => {is_login = false; is_creating_acct = true}} class="text-blue-700 hover:underline dark:text-blue-500">Create account</a>
          </div>
        </form>
      </Modal>

      <!-- Create Account form -->
      <Modal bind:open={is_creating_acct} size="xs" autoclose={false} class="w-full">
        <form class="flex flex-col space-y-6" action='#'>
          <!-- Title -->
          <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Create an Account</h3>

          <!-- First Name Field -->
          <Label class="space-y-2">
            <span>First Name</span>
            <Input type="text" name="create_firstname" placeholder="Michael" required />
          </Label>

          <!-- Last Name Field -->
          <Label class="space-y-2">
            <span>Last Name</span>
            <Input type="text" name="create_lastname" placeholder="Scott" required />
          </Label>

          <!-- Email Field -->
          <Label class="space-y-2">
            <span>Email</span>
            <Input type="email" name="create_email" placeholder="name@company.com" required />
          </Label>

          <!-- Password field -->
          <Label class="space-y-2">
            <span>Password</span>
            <Input type="password" name="create_password" placeholder="••••••••••" bind:value={password} required />
          </Label>

          <!-- Confirm password field -->
          <Label class="space-y-2">
            <span>Confirm Password</span>
            <Input type="password" name="confirm_password" placeholder="••••••••••" bind:value={confirm_password} required />
          </Label>

          <!-- Let the  user know whether or not the passwords match-->
          <Label class="foo space-y-2">
            {#if password === confirm_password}
            <span style="color: green">Passwords match</span>
            {:else}
            <span style="color: red">Passwords do not match</span>
            {/if}
          </Label>

          <!-- Venue ID Field -->
          <Label class="space-y-2">
            <span>Venue ID (optional)</span>
            <Input type="text" name="venue_id" />
          </Label>

          <!-- Create Account button -->
          <Button type="submit" class="w-full1">Create Account</Button>
        </form>
      </Modal>
    </div>

    <!-- Navigation Bar -->
    <NavUl {hidden} class="order-1">
      <NavLi href="/" active={$page.url.pathname === "/"}>HOME</NavLi>
      <NavLi href="/shows" active={$page.url.pathname === "/shows" }>SHOWS</NavLi>
      <NavLi href="/tickets" active={$page.url.pathname === "/tickets"}>BUY TICKETS</NavLi>
      <NavLi href="/help" active={$page.url.pathname === "/contact"}>HELP</NavLi>
    </NavUl>
  </Navbar>