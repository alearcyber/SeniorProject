<!-- 
    Playhouse Component 
    This component is the SVG image of the Playhouse.
-->

<script>
    import Seat from "../components/Seat.svelte"
    import { clear } from '../stores/SeatStore.js'
    import { onMount } from 'svelte'

    /**
	* @type {{ left_orch: any; main_orch: any; right_orch: any; balc: any; left_loge: any; right_loge: any; left_box: any; right_box: any; }}
	*/
    export let seats

    /**
	* @type {{ [x: string]: any; }}
	*/
    export let tickets

    //clear the seat store when page is left
    onMount(() => {
		clear()
	})
</script>


<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 10240 7680" x="0px" y="0px" width="1024px" height="768px">
    <defs>
    </defs>
    <g>
        <path 
        d="M9158.98,1009.54L3866.6800000000003,595.28L669.95,1824.47L669.95,5994.67L3896.6800000000003,7249L9158.98,6834.73C9158.98,6834.73 9581.460000000001,5920.119999999999 9581.460000000001,3919.22C9581.46,1918.33 9158.98,1009.54 9158.98,1009.54z" 
        id="VENUE POCHE" 
        fill="#F6F6F6" 
        stroke-width="10" 
        stroke="#D4D4D4"
        />
        <path 
        d="M869.95,5872.780000000001L869.95,1972.26L1640.05,1706.0900000000001L1640.05,6128.57z" 
        id="STAGE BASE" 
        fill="#262626" 
        stroke-width="10"
        />
        <text 
        font-family="arialebold" 
        font-size="360" 
        transform="rotate(-90, 1057.3040443072314, 4486.561268606538)" 
        x="1064.4999070434974" 
        y="4819.570144152938" 
        width="1253.9" 
        height="416.35" 
        fill="#ffffff" 
        stroke-width="10"
        >STAGE
        </text>
        <path 
        d="M3009.4700000000003,6357.77L2752.96,6297.79L1834.9299999999998,5956.130000000001L1709.65,5642.290000000001L1712.62,5637.900000000001C1889.3700000000001,5376.660000000001 2024.0800000000002,5091.990000000001 2113.0099999999998,4791.820000000001L2121.7599999999998,4762.290000000001L1883.73,4698.500000000001L1886.67,4688.650000000001C1961.11,4439.1 1998.86,4179.410000000001 1998.86,3916.8000000000006C1998.86,3641.750000000001 1957.49,3370.2200000000003 1875.8899999999999,3109.7800000000007L1872.77,3099.830000000001L2111.27,3035.9200000000005L2102.0499999999997,3006.1400000000003C2011.3999999999999,2713.3100000000004 1877.1,2435.8200000000006 1702.8899999999999,2181.3900000000003L1699.9599999999998,2177.1000000000004L1844.3599999999997,1791.1000000000004L2743.2200000000003,1465.7500000000005L2990.1,1468.3400000000004L3306.92,1238.2400000000002L6321.65,1455.0900000000001L6377.089999999999,1770.0700000000002C6484.53,2476.27 6539.0599999999995,3198.7400000000002 6539.0599999999995,3916.7200000000003C6539.0599999999995,4632.990000000001 6484.969999999999,5352.860000000001 6378.28,6056.35L6321.619999999999,6371.5L3375.8699999999994,6580.969999999999L3009.4700000000003,6357.77z" 
        id="ORCH BASE" 
        fill="#ffffff" 
        stroke-width="10"
        />
        <path 
        d="M3515.09,6757.110000000001L6682.290000000001,6500.42L6688.570000000001,6481.639999999999C6964.41,5657.429999999999 7104.270000000001,4795.3099999999995 7104.270000000001,3919.22C7104.270000000001,3044.7299999999996 6965.210000000002,2184.64 6690.940000000001,1362.8499999999997L6684.660000000002,1344.0499999999997L3515.090000000001,1087.1599999999999L3924.470000000001,830.5099999999999L8983.190000000002,1226.4899999999998L9075.210000000003,1538.45C9258.510000000002,2314.43 9351.460000000003,3115.46 9351.460000000003,3919.23C9351.460000000003,4705.65 9262.350000000002,5490.1 9086.610000000002,6250.789999999999L9077.340000000002,6290.92L9079.7,6290.72L8983.190000000002,6617.79L3924.4700000000016,7013.780000000001L3515.09,6757.110000000001z" 
        id="DROPSHADOW BALCONY BASE" 
        fill="#ffffff" 
        stroke-width="10"
        />
        <path 
        d="M3138.17,6377.63L6319.77,6099.27L6279.290000000001,6324.390000000001L3388.250000000001,6529.99L3138.17,6377.63zM3103.47,1447.81L3321.5499999999997,1289.43L6279.1799999999985,1502.1800000000003L6318.829999999999,1727.46L3103.47,1447.81z" 
        id="OLOGE" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
        <path 
        d="M3676.7000000000003,6796.59L6696.220000000001,6551.860000000001L9007.68,6349.62L8943.140000000001,6568.360000000001L3937.650000000001,6960.17L3676.7000000000003,6796.59zM6696.4800000000005,1292.44L3676.7000000000003,1047.68L3937.6400000000003,884.0899999999999L8943.13,1275.9099999999999L9007.67,1494.65L6696.4800000000005,1292.44z" 
        id="BLOGE" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
        <path 
        d="M6749.47,6464.48C7019.6900000000005,5645.129999999999 7156.67,4789.16 7156.67,3919.22C7156.67,3050.92 7020.48,2196.97 6751.82,1379.9899999999998L9031.01,1579.3899999999996C9208.880000000001,2342.43 9299.07,3129.49 9299.07,3919.209999999999C9299.07,4710.91 9208.4,5499.939999999999 9029.51,6265L6749.47,6464.48z" 
        id="BALC" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
        <path 
        d="M1953,4642.29C2016.6200000000001,4406.7 2048.86,4162.799999999999 2048.86,3916.7999999999993C2048.86,3658.2999999999993 2013.2900000000004,3402.4199999999996 1943.1200000000001,3155.7599999999998L3557.6800000000003,2730.4299999999994L6444.120000000001,2788.5199999999995C6473.95,3163.95 6489.070000000001,3543.3799999999997 6489.070000000001,3916.73C6489.070000000001,4279.06 6474.8099999999995,4647.57 6446.700000000001,5012.4400000000005L3557.7400000000007,5070.57L1953,4642.29z" 
        id="ORCH" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
        <path 
        d="M6436.849999999999,2698.96C6411.3,2400.56 6376.5199999999995,2103.39 6332.399999999999,1808.94L2991.379999999999,1518.3700000000001L2751.7599999999993,1515.8600000000001L1883.1199999999992,1830.2700000000002L1755.8799999999994,2170.38C1931.6799999999994,2430.79 2066.2599999999993,2714.2599999999998 2156.459999999999,3013.47L2158.0499999999993,3013.05L3546.7199999999993,2640.2L6436.849999999999,2698.96z" 
        id="ORCHR" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
        <path 
        d="M3016.1900000000005,6308L6333.530000000001,6017.7699999999995C6378.750000000001,5714.96 6414.1900000000005,5409.169999999999 6439.760000000001,5101.99L3546.590000000001,5160.82L2167.96,4785L2167.04,4784.76C2078.7,5090.969999999999 1943.9099999999999,5381.32 1765.8899999999996,5648.289999999999L1873.1599999999999,5917.02L2767.4399999999996,6249.84L3016.1900000000005,6308z" 
        id="ORCHL" 
        stroke="gray" 
        stroke-width="20"
        fill="gainsboro"
        class="hover:opacity-60"
        />
    </g>
    <!-- Add seats to the different sections -->
    <g class="seats">
        <g data-component="svg_block" data-section-name="ORCHL" data-section-id="s_1" class="section" >
            {#each seats.left_orch as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="ORCH" data-section-id="s_2" class="section" >
            {#each seats.main_orch as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="ORCHR" data-section-id="s_3" class="section" >
            {#each seats.right_orch as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="BALC" data-section-id="s_4" class="section" >
            {#each seats.balc as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LLOGE" data-section-id="s_5" class="section" >
            {#each seats.left_loge as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="RLOGE" data-section-id="s_6" class="section" >
            {#each seats.right_loge as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="BOXL" data-section-id="s_7" class="section" >
            {#each seats.left_box as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
        <g data-component="svg_block" data-section-name="BOXR" data-section-id="s_8" class="section" >
            {#each seats.right_box as seat}
                <Seat bind:seat={seat} ticket={tickets[seat?.id] ?? {}} />
            {/each}
        </g>
    </g>
</svg>