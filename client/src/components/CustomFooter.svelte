<!-- 
    Footer Component 
    This component has the footer copyright and the footer navigation links.
-->

<script>
    import { Footer, FooterCopyright, FooterLink, FooterLinkGroup } from "flowbite-svelte"

    // get current year
    const date = new Date()
    const year = date.getFullYear() 
</script>

<Footer>
    <FooterCopyright href="/" by="Huntsville Civic Center™" year={year} /> 
    <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
        <FooterLink href="/">About</FooterLink>
        <FooterLink href="/">Privacy Policy</FooterLink>
        <FooterLink href="/">Licensing</FooterLink>
        <FooterLink href="/contact">Contact</FooterLink>
    </FooterLinkGroup>
</Footer>