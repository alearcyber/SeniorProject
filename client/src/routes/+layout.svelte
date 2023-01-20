<script>
	import '../app.postcss'
	import CustomFooter from '../components/CustomFooter.svelte'
	import CustomNavBar from '../components/CustomNavBar.svelte'
</script>

<div class="relative w-full">
	<CustomNavBar />
	<slot />
	<CustomFooter />
</div>
