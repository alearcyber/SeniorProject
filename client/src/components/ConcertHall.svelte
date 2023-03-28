<!-- 
    Concert Hall Component 
    This component is the SVG image of the Concert Hall.
-->

<script>
    import Seat from "../components/Seat.svelte"

    /**
	 * @type {{ left_pit: any; center_pit: any; right_pit: any; orch1: any; orch2: any; orch3: any; loge1: any; loge2: any; lower_balc1: any; lower_balc2: any; lower_balc3: any; lower_balc4: any; upper_balc1: any; upper_balc2: any; upper_balc3: any; upper_balc4: any; upper_balc5: any; }}
	 */
     export let seats
</script>

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 10240 7680" x="0px" y="0px" width="1024px" height="768px">
    <defs>
    </defs>
    <g>
      <g id="background">
        <path 
            d="M5484.814,1388.95L1956.425,1821.949L1139.5045,2360.0138L750.0540000000001,2359.985L750.0540000000001,2360.1500000000005L50.158,2360.1500000000005L50.1,5310.15L1020.104,5310.15L1020.104,5309.198900000001L1136.5233999999998,5309.114300000002L1902.531,5853.55L5484.8640000000005,6294.95L10200.072,6294.572L10200.072,5656.429999999999L10200.072,4628.646L10200.072,3449.763L10200.072,2423.379999999999L10200.072,1389.033z" 
            id="POCHE" 
            fill="#f6f6f6" 
            stroke="#d4d4d4" 
            stroke-width="10"
        />
        <path 
            d="M250.19968618380642,2560.2L820.1499006276324,2560.2L820.1499006276324,5110.199921572169L250.15,5110.199921572169z" 
            id="stage" 
            transform="rotate(-5.684341886080804e-14, 250.15, 2560.2)" 
            fill="#262626" 
            stroke-width="10"
        />
        <text 
            font-family="arialebold"
            font-size="480" 
            transform="rotate(-90, 265.40561199806484, 4679.514826910516)" 
            x="275" 
            y="5123.5" 
            width="1671.85" 
            height="555.1" 
            fill="#ffffff" 
            stroke-width="10">
            <tspan 
                text-anchor="start" 
                x="275">STAGE
            </tspan>
        </text>
      </g>
      <g id="orch">
        <path 
            d="M2016.416497962199,2022L1200.25,2559.5683588317106L1200.2683588317107,3202.768358831711L5810.294923504869,3202.7183588317107L5810.544923504869,2022.0683588317104z" 
            id="SEC3" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M1200.25,3203.018358831711L1200.2683588317107,4468.168358831711L5610.494923504869,4468.15L5610.494923504869,3203z" 
            id="SEC2" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M1200.25,4468.068358831711L1200.2683588317107,5109.068358831711L1966.411507746371,5653.599913720696L5810.544923504869,5653.6L5810.294923504869,4468.05z" 
            id="SEC1" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M950.1698275862069,4508.6L950.1,5109.220689655173L1200.07,5109.040689655173L1200.0698275862069,4508.6z" 
            id="PITL" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M950.1,3163.4L950.109482758621,4507.519827586208L1199.909482758621,4507.519827586208L1200,3163.4z" 
            id="PITC" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M950.1,2560.05L950.1698275862069,3162.369827586207L1200.0698275862069,3162.369827586207L1200.07,2560.07z" 
            id="PITR" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
      </g>
      <g id="BALCONY DETAILS">
        <polyline 
            points="5748.35,1589 5881.544,2066.05 7865.8051,2066.05 7971.4707,2451.1207 7971.4707,2524.5207 7971.55,2524.5207 7971.75,3720.8052 7971.75,5164.1 7971.5207,5164.1 7971.6678,5232.4971000000005 7868.572900000001,5617.8778999999995 7868.55,5617.85 7868.3579,5618.0033 7868.3678,5617.9678 5881.594,5617.95 5748.4,6095 10000.1184,6094.6184 10000.1184,1589.0684 5748.35,1589 " 
            id="UPPER LEVEL DROP SHADOW" 
            fill="#dfdfdf" 
            stroke="#dfdfdf" 
            stroke-width="16"
        />
        <g>
          <polyline 
            points="5879.613004172462,1524.6130041724618 5879.613004172462,1311.2630041724617 1830.05,1311.25 1830.05,1906.5 " 
            id="OH ARROW" 
            fill="none" 
            stroke="#727272" 
            stroke-width="5"
          />
          <path 
            d="M1782.05,1906.57L1830.104,1989.682L1878.05,1906.5z" 
            fill="#727272"
          />
        </g>
        <g>
          <polyline 
            points="5879.613004172462,6155.663004172462 5879.613004172462,6368.763004172462 1830.05,6368.55 1830.05,5773.3 " 
            id="OH ARROW" 
            fill="none" 
            stroke="#727272" 
            stroke-width="5"
          />
          <path 
            d="M1878.05,5773.2300000000005L1829.9959999999999,5690.118L1782.05,5773.3z" 
            fill="#727272"
          />
        </g>
        <text 
            font-family="arialebold" 
            font-size="200" 
            x="2954" 
            y="1265.4" 
            width="1785.1" 
            height="231.3" 
            fill="#727272" 
            stroke-width="10"
        >
            <tspan 
                text-anchor="start" 
                x="2954">LOGE OVERHANG
            </tspan>
        </text>
        <text 
            font-family="arialebold" 
            font-size="200" 
            x="2954" 
            y="6560" 
            width="1785.1" 
            height="231.3" 
            fill="#727272" 
            stroke-width="10"
        >
          <tspan 
            text-anchor="start" 
            x="2954">LOGE OVERHANG
          </tspan>
        </text>
      </g>
      <g id="balc">
        <path 
            d="M5881.593999999999,5617.95L5748.4,6095L7735.165,6095L7868.367802503477,5617.967802503477L7868.367802503477,5617.967802503477z" 
            id="LOGE1" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M5748.35,1589L5881.544,2066.05L7868.2771,2066.05L7734.936,1589Z" 
            id="LOGE4" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M7971.520653685674,5164.1L7971.667802503477,5232.4971488178035L7868.567802503477,5617.897148817803L7735.15,6094.96154381085L8331.051,6094.96154381085L8571.964,5232.11154381085L8571.820653685674,5164.120653685675z" 
            id="LOWERBALCONY1" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M7971.75,3844.65L7971.75,5164.070653685674L8571.820653685674,5164.070653685674L8571.8,3844.6706536856746z" 
            id="LOWERBALCONY2" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M7971.55,2524.4L7971.770653685675,3844.6206536856744L8571.820653685674,3844.6206536856744L8571.820653685674,2524.4206536856746z" 
            id="LOWERBALCONY3" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M7734.9,1589L7971.470653685674,2451.1206536856744L7971.470653685674,2524.5206536856745L8571.920653685675,2524.5206536856745L8571.935,2451.914L8331.004,1589z" 
            id="SEC4" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M9050.4,5456.7L9050.4,6094.6L10000.11835883171,6094.618358831711L10000.11835883171,5456.71835883171z" 
            id="UPPERBALCONY1" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M8800.4,4428.85L8800.4,5456.75L10000.11835883171,5456.518358831711L10000.11835883171,4428.868358831711z" 
            id="UPPERBALCONY2" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M8800.4,3249.85L8800.4,4428.85L10000.11835883171,4428.718358831711L10000.11835883171,3249.9183588317105z" 
            id="UPPERBALCONY3" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M8800.4,2224L8800.4,3249.8500000000004L10000.11835883171,3249.8183588317106L10000.11835883171,2224.0683588317106z" 
            id="UPPERBALCONY4" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M9050.4,1589L9050.4,2223.6500000000005L10000.11835883171,2223.4683588317107L10000.11835883171,1589.0683588317106z" 
            id="SEC5" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M5748.35,1589L5881.544,2066.05L7865.8051,2066.05L7971.4707,2451.1207L7971.4707,2524.5207L8571.9207,2524.5207L8571.935,2451.914L8331.004,1589Z" 
            id="LOGE 4 STROKE" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
        <path 
            d="M7971.5207,5164.1L7971.6678,5232.4971L7868.5678,5617.8971L7868.5358,5618.0117C7868.5118,5617.9709 7868.4998,5617.9503 7868.5,5617.95L7868.348,5618.0386L7868.3678,5617.9678L5881.594,5617.95L5748.4,6095L7735.165,6095L7735.1757,6094.9615L8331.051,6094.9615L8571.964,5232.1115L8571.8207,5164.1207L7971.5207,5164.1Z" 
            id="LOGE 1 STROKE" 
            fill="#ffffff" 
            stroke="#dddddd" 
            stroke-width="16"
        />
      </g>
    </g>
    <g class="seats">
        <g data-component="svg_block" data-section-name="PITL" data-section-id="s_1" class="section" >
            {#each seats.left_pit as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="PITC" data-section-id="s_2" class="section" >
            {#each seats.center_pit as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="PITR" data-section-id="s_3" class="section" >
            {#each seats.right_pit as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="ORCH1" data-section-id="s_4" class="section" >
            {#each seats.orch1 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="ORCH2" data-section-id="s_5" class="section" >
            {#each seats.orch2 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="ORCH3" data-section-id="s_6" class="section" >
            {#each seats.orch3 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LOGE1" data-section-id="s_7" class="section" >
            {#each seats.loge1 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LOGE2" data-section-id="s_8" class="section" >
            {#each seats.loge2 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LBALC1" data-section-id="s_9" class="section" >
            {#each seats.lower_balc1 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LBALC2" data-section-id="s_10" class="section" >
            {#each seats.lower_balc2 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LBALC3" data-section-id="s_11" class="section" >
            {#each seats.lower_balc3 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="LBALC4" data-section-id="s_12" class="section" >
            {#each seats.lower_balc4 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="UBALC1" data-section-id="s_13" class="section" >
            {#each seats.upper_balc1 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="UBALC2" data-section-id="s_14" class="section" >
            {#each seats.upper_balc2 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="UBALC3" data-section-id="s_15" class="section" >
            {#each seats.upper_balc3 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="UBALC4" data-section-id="s_16" class="section" >
            {#each seats.upper_balc4 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
        <g data-component="svg_block" data-section-name="UBALC5" data-section-id="s_17" class="section" >
            {#each seats.upper_balc5 as seat}
                    <Seat seat={seat} />
	            {/each}
        </g>
    </g>
  </svg>