<!-- 
    Volunteer Navigation Page
    This page is where the volunteers go to create a season, production, and manage front desk.
-->

<script>
    import { Navbar, NavBrand, NavLi, NavUl, Button, Input, Modal, Label, Checkbox } from 'flowbite-svelte'
    import { page } from '$app/stores'

    let is_adding_volunteer = false;

    
</script>
  
    <!-- Volunteer Login Form -->
    <div class="mb-10 flex justify-center"> 
          <form class="flex flex-col space-y-6" style="width:500px" action="#">
            <!-- Title -->
            <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Volunteer Login</h3>
  
            <!-- Email field -->
            <Label class="space-y-2">
              <span>Email</span>
              <Input type="email" name="email" placeholder="name@company.com" required />
            </Label>
  
            <!-- Organization Code field -->
            <Label class="space-y-2">
              <span>Organization Code</span>
              <Input type="text" name="org_code" placeholder="••••••••••" required />
            </Label>
  
            <!-- Login button -->
            <Button type="submit" href="/volunteers/navigation" class="w-full1">Login as volunteer</Button>
  
            <!-- Add volunteer link -->
            <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
              Not registered as volunteer? <a href= "" on:click={() => {is_adding_volunteer = true}} class="text-blue-700 hover:underline dark:text-blue-500">Register Here</a>
            </div>
          </form>


        <!-- Add volunteer form -->
      <Modal bind:open={is_adding_volunteer} size="xs" autoclose={false} class="w-full">
        <form class="flex flex-col space-y-6" action='#'>
          <!-- Title -->
          <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Register As Volunteer</h3>

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

           <!-- Organization Code field -->
           <Label class="space-y-2">
            <span>Organization Code</span>
            <Input type="text" name="org_code" placeholder="••••••••••" required />
          </Label>

          <!-- Add volunteer button -->
          <Button href= "/volunteers/navigation" type="submit" class="w-full1">Register as Volunteer</Button>
        </form>
      </Modal>
    </div>

  
 



