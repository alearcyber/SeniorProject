<!-- 
    Import/Export Page
    This page is where the volunteers go to import or export data to/from the database.
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList, Listgroup } from 'flowbite-svelte'
	let files;
</script>
  
<div class="mb-10 flex justify-center">
    <form class=" ml-1flex flex-col space-y-2" style="width:500px" action='/'>
        
        <!-- Import Data Header -->
        <h3 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Import Data from Database</h3>

        <!-- Import button: Go to payment page with guests reserved tickets from database -->
        <Button type="submit" class="mr-3 h-18 sm:h-18 justify-center" style="width:150px" action='/'>Import Data*</Button>
        <input accept=".csv, .json, .xlsx, .db" bind:files type="file"/>

        <!-- Import Data Descriptor -->
        <h3 class="text-l font-medium text-gray-900 dark:text-white p-0">*Importing the database will open up a file browser and will automatically save a backup of the current database.</h3>

    </form>

    <form class=" ml-1flex flex-col space-y-2" style="width:500px" action='/'>
        
        <!-- Export Data Header -->
        <h3 class="text-3xl font-medium text-gray-900 dark:text-white p-0">Export Data from Database</h3>

        <!-- Export button: Go to payment page with guests reserved tickets from database -->
        <Button class="mr-3 h-18 sm:h-18 justify-center" style="width:150px" action='/'>Export Data*</Button>
        <input type="file" accept=".csv, .json, .xlsx, .pdf, .html, .db" bind:files>

        <!-- Export Data Descriptor -->
        <h3 class="text-l font-medium text-gray-900 dark:text-white p-0">*Exporting the database will open up a file browser to browse the save destination.</h3>

    </form>
</div>