<!-- 
    Footer Component 
    This component has the footer copyright and the footer navigation links.
-->

<script>
    import { Footer, FooterCopyright } from "flowbite-svelte"

    //get current year
    const date = new Date()
    const year = date.getFullYear() 
</script>

<Footer>
    <FooterCopyright href="/" by="Huntsville Civic Center™" year={year} /> 
</Footer>