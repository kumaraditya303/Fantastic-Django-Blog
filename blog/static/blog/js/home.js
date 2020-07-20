$(document).ready(() => {
	$('.author').hover(
		(event) => {
			$.getJSON(`/author/${event.target.id}`).then((response) => {
				res = JSON.parse(response);
				console.log(res);
				$(event.target)
					.popover({
						html: true,
						content: `<div class="media">
  						<img src="${$(`#${event.target.id}.media > img`).attr(
								'src'
							)}" class="rounded-circle mr-3" width="75"
					    height="75" >
					  <div class="media-body">
					    <h5>${event.target.text}</h5>
					    <p>${res[0]['fields']['description']}</p>
					  </div>
						</div>`,
					})
					.popover('show');
			});
		},
		(event) => {
			$(event.target).popover('hide');
		}
	);
});
