<!-- 
    Help Page
    This page is where the customer will go to find helpful soultions to their problems and know how to operate the software. 
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList } from 'flowbite-svelte'
    
    let commentarea = { //comment area for the comment field
        id: 'message',
        name: 'message',
        label: 'Your message',
        rows: 4,
        placeholder: 'Describe the issue... ',
    }
    
  </script>
  
  <div class="space-y-10">
    <div class="text-center">
        <Heading tag="h1" class="mb-16" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">How can we help you?</Heading> 


        
        <div class="mb-10 flex justify-center">
            <Card class="flex flex-col space-y-10" style="width: 500px" >
                <div class="mb-5 flex justify-center">
                    <img src="../started_logo.jpg" class="mr-3 h-24 sm:h-24" alt="logo" style="width: 150px" />
                    <Heading tag="h2" class="mb-5 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Getting Started</Heading> 
                </div>
                <a href="/help/account_help" class="text-blue-700 hover:underline dark:text-blue-500">Sign up for an account</a>
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Sign up for season tickets</a>
            </Card> 
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <div class="mb-5 flex justify-center">
                    <img src="../ticket_logo.png" class="mr-3 h-24 sm:h-24" alt="logo" style="width: 150px" />
                    <Heading tag="h2" class="mb-1 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Tickets</Heading> 
                </div>
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Purchasing Tickets</a>
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Choosing a venue</a>    
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Choosing a performance</a>   
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Selecting Seats for performance</a>     
            </Card> 
            <Card class="flex flex-col space-y-5" style="width: 500px">
                <div class="mb-5 flex justify-center">
                    <img src="../volunteer_logo.jpg" class="mr-3 h-24 sm:h-24" alt="logo" style="width: 150px" />
                    <Heading tag="h2" class="mb-1 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Volunteer Help</Heading> 
                </div>
                <a href="/help/volunteer_help" class="text-blue-700 hover:underline dark:text-blue-500">Create or login to organiztion</a>
                <a href="/help/volunteer_help" class="text-blue-700 hover:underline dark:text-blue-500">Creating a Season</a>    
                <a href="/help/volunteer_help" class="text-blue-700 hover:underline dark:text-blue-500">Creating a new production</a>   
                <a href="/help/volunteer_help" class="text-blue-700 hover:underline dark:text-blue-500">Login as admin</a>   
                <a href="/help/volunteer_help" class="text-blue-700 hover:underline dark:text-blue-500">Manage front desk</a>     
            </Card> 
            <Card class="flex flex-col space-y-5"  style="width: 500px">
                <div class="mb-5 flex justify-center">
                    <img src="../account.png" class="mr-3 h-24 sm:h-24" alt="logo" style="width: 150px" />
                    <Heading tag="h2" class="mb-1 text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Account</Heading> 
                </div>
                <a href="/help/account_help" class="text-blue-700 hover:underline dark:text-blue-500">Login to account</a>
                <a href="/help/account_help" class="text-blue-700 hover:underline dark:text-blue-500">Forgot Password</a>    
                <a href="/help/ticket_help" class="text-blue-700 hover:underline dark:text-blue-500">Access season tickets</a>   
                <a href="/help/account_help" class="text-blue-700 hover:underline dark:text-blue-500">Update Season ticket info</a>     
            </Card> 
        </div>
        
        <div class="mb-10 flex justify-center" >
            <form class="flex flex-col space-y-6" style="width:800px" action="/">
                <!-- Title -->
                <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Need more help?</h3>
                
                <!-- First name field -->
                <Label class="space-y-2">
                    <span class="flex justify-left" >First Name</span>
                    <Input type="text" name="first-name" placeholder="First Name" required />
                </Label>
                
                <!-- Last name field -->
                <Label class="space-y-2">
                    <span class="flex justify-left" >Last Name</span>
                    <Input type="text" name="last-name" placeholder="Last Name" required />
                </Label>
                
                <!-- Email field -->
                <Label class="space-y-2">
                    <span class="flex justify-left" >Email</span>
                    <Input type="email" name="email" placeholder="name@company.com" required />
                </Label>

                <!-- Comment field -->
                <Label class="space-y-2">
                    <span class="flex justify-left">Issue</span>
                    <Textarea {...commentarea} required />
                </Label>
               
                
                <!-- Submit button -->
                <Button type="submit" class="w-full" on:click>Submit</Button>
            </form>

        </div>


    </div>     
  </div>
  
 



