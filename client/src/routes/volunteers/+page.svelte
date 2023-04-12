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
      {#if sessionStorage.getItem("org_id") != null && sessionStorage.getItem("org_id") != ""}
      <script>
        window.location.href = "/volunteers/navigation"
      </script>
      {:else}
      <h1 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Hmm, it doesn't look like you're a volunteer.</h1>
      {/if}
    </div>

  
 



