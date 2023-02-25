<!-- 
	Main Layout
    This layout is the main layout for the site. It makes all pages have 
	the navigation bar and the footer unless otherwise specified. 
-->

<script>
	import '../app.postcss'
	import CustomFooter from '../components/CustomFooter.svelte' //import footer component
	import CustomNavBar from '../components/CustomNavBar.svelte' //import navbar component
</script>

<!-- place navbar and footer around all pages unless otherwise specified -->
<div class="relative w-full">
	<CustomNavBar />
	<slot />
	<CustomFooter />
</div>
