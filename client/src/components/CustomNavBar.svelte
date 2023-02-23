<script>
    import { Navbar, NavBrand, NavLi, NavUl, Button, Input, Modal, Label, Checkbox } from 'flowbite-svelte'
    import { page } from '$app/stores'

    let formModal = false 
</script>

<Navbar let:hidden let:toggle>
    <NavBrand href="/">
      <img
        src="../logo.jpeg"
        class="mr-3 h-24 sm:h-24"
        alt="Huntsville Civic Center Logo"
      />
    </NavBrand>
    <div class="flex md:order-2">
      <Button on:click={() => formModal = true}>Login</Button>
      <Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
        <form class="flex flex-col space-y-6" action="#">
          <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Sign in</h3>
          <Label class="space-y-2">
            <span>Email</span>
            <Input type="email" name="email" placeholder="name@company.com" required />
          </Label>
          <Label class="space-y-2">
            <span>Your password</span>
            <Input type="password" name="password" placeholder="••••••••••" required />
          </Label>
          <div class="flex items-start">
              <Checkbox>Remember me</Checkbox>
              <a href="/" class="ml-auto text-sm text-blue-700 hover:underline dark:text-blue-500">Lost password?</a>
          </div>
          <Button type="submit" class="w-full1">Login to your account</Button>
            <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
              Not registered? <a href="/" class="text-blue-700 hover:underline dark:text-blue-500">Create account</a>
            </div>
        </form>
      </Modal>
    </div>
    <NavUl {hidden} class="order-1">
      <NavLi href="/" active={$page.url.pathname === "/"}>HOME</NavLi>
      <NavLi href="/shows" active={$page.url.pathname === "/shows" }>SHOWS</NavLi>
      <NavLi href="/tickets" active={$page.url.pathname === "/tickets"}>BUY TICKETS</NavLi>
      <NavLi href="/contact" active={$page.url.pathname === "/contact"}>CONTACT US</NavLi>
    </NavUl>
</Navbar>


