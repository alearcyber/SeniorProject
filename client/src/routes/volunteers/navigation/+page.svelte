<!-- 
    Volunteer Navigation Page
    This page is where the volunteers go to create a season, production, and manage front desk.
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList } from 'flowbite-svelte'
</script>
  
<!-- Volunteer Navigaion -->
  <div class="space-y-10">
    <div class="text-center">
        <Heading tag="h1" class="mb-16" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">Volunteer Navigation</Heading> 
 
        <div class="mb-10 flex justify-center">

            <!-- Create New Season -->
            <Card class="flex flex-col space-y-10" style="width: 500px" >
                <img src="../masks.png" class="mr-3 h-24 sm:h-24" alt="logo" style=" height:250px" />
                <a href="/volunteers/season" class="text-4xl text-blue-700 hover:underline dark:text-blue-500">Create New Season</a>
            </Card> 

            <!-- Create New Production -->
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <img src="../camera.png" class="mr-3 h-24 sm:h-24" alt="logo" style=" height:250px" />
                <a href="/volunteers/production" class="text-4xl text-blue-700 hover:underline dark:text-blue-500">Create New Production</a>   
            </Card> 

            <!-- Front Desk -->
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <img src="../frontdesk.jpg" class="mr-3 h-24 sm:h-24" alt="logo" style=" height:250px" />
                <a href="/frontdesk" class="text-4xl text-blue-700 hover:underline dark:text-blue-500">Manage Front Desk</a>
            </Card> 

            <!-- Import/Export -->
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <img src="../started_logo.jpg" class="mr-3 h-24 sm:h-24" alt="logo" style=" height:250px" />
                <a href="/volunteers/importexport" class="text-4xl text-blue-700 hover:underline dark:text-blue-500">Import/Export Database</a>
            </Card> 

            <!-- Past Season Pass Info -->
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <img src="../seasonpass.jpg" class="mr-3 h-24 sm:h-24" alt="logo" style=" height:250px" />
                <a href="/pastseason" class="text-4xl text-blue-700 hover:underline dark:text-blue-500">Past Season Pass Info</a>
            </Card> 
        </div>
    </div>  
    
  </div>
  
 



