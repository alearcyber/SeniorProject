<!-- 
    Help Page
    This page is where the customer will go to find helpful soultions to their problems and know how to operate the software. 
-->

<script>
    import { Label, Input, Textarea, Button, Card, Heading, List, DescriptionList, P, Layout } from 'flowbite-svelte'
    
    
  </script>
  
  <div class="space-y-2">
    <div class="text-center">
        <Heading tag="h1" class="mb-10 pl-16 text-left" customSize="text-4xl font-extrabold  md:text-4xl lg:text-4xl">Volunteer Help</Heading> 
        <Layout class= "mb-3" gap={1}>
          <P class= "mb-3 pl-16 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Create an Organiztion</h3>
              1. .....
          </P>
          <P class= "mb-3 pl-5 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Login to Organization</h3>
              1. Select <strong class="font-semibold text-blue-900 dark:text-white">"Login"</strong> in the right hand corner.
              2. If you already created an account with organization code, just login.
              3. Then select <strong class="font-semibold text-blue-900 dark:text-white">"Login to your account"</strong>.
              4. If not, select <strong class="font-semibold text-blue-900 dark:text-white">"Create account"</strong> and fill in information and organization code.
              5. Then select <strong class="font-semibold text-blue-900 dark:text-white">"Create account"</strong>.
          </P>
        </Layout>
        <Layout gap={1}>
          <P class= " mt-10 mb-3 pl-16 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mt-10 mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Create a Season</h3>
              1. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Volunteers"</strong> in the navigation bar.
              2. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Create New Season"</strong>.
              3. Fill in information for the season, then select <strong class="font-semibold text-blue-900 dark:text-white">"Create Season"</strong>.
          </P>
          <P class= "mt-10 mb-3 pl-5 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mt-10 mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Create new Production</h3>
            1. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Volunteers"</strong> in the navigation bar.
            2. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Create New Production"</strong>
            3. Fill in information for the production.
            4. Fill in information for each performace for the production.
            5. Then select <strong class="font-semibold text-blue-900 dark:text-white">"Create Production"</strong>.
          </P>
        </Layout>
        <Layout gap={1}>
          <P class= " mt-10 mb-3 pl-16 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mt-10 mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Login as Admin</h3>
              1. Follow the standard login procedure.
              Logging in as an admin is automatic as the database will
              check if the user email/password match an admin account
              already in the system.
          </P>
          <P class= "mt-10 mb-3 pl-5 text-left" weight="bold" color="text-gray-500 dark:text-gray-400"  whitespace="preline" size="xl">
            <h3 class="mt-10 mb-1 pl-5 text-left text-xl font-medium text-blue-900 dark:text-white p-0">Operate Front Desk Help</h3>
            1. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Volunteers"</strong> in the navigation bar.
            2. Click on <strong class="font-semibold text-blue-900 dark:text-white">"Manage Front Desk"</strong>.
            3. To purchase seats for guets, enter venue name.
            4. Upcoming performance will be displayed, select <strong class="font-semibold text-blue-900 dark:text-white">"Buy Tickets"</strong> on guests desired performance.
            5. Select seats in seating chart, then click <strong class="font-semibold text-blue-900 dark:text-white">"Purchase Tickets"</strong>.
            6. On payment page, enter payment information.
            7. To pay existing reservation, enter in guests' name, and select <strong class="font-semibold text-blue-900 dark:text-white">"Continue"</strong>.
            8. ....

          </P>
        </Layout>

    </div>     
  </div>
  
 



