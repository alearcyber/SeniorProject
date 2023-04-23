export async function load({ url }) {
    const pid = '26';
    const response = await fetch('http://127.0.0.1:5000/get_seating_chart', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ 'performance_id': pid })
		});

    const data = await response.json();
    return { data };
}