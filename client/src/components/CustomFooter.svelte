<script>
    import { Footer, FooterCopyright, FooterLink, FooterLinkGroup } from "flowbite-svelte"
</script>

<Footer>
    <FooterCopyright href="/" by="Huntsville Civic Center™" year={2022} />
    <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
        <FooterLink href="/">About</FooterLink>
        <FooterLink href="/">Privacy Policy</FooterLink>
        <FooterLink href="/">Licensing</FooterLink>
        <FooterLink href="/">Contact</FooterLink>
    </FooterLinkGroup>
</Footer>