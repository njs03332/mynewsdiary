// for event modal
$('#eventModal').on('show.bs.modal', function (event) {
    var eventLabel = $(event.relatedTarget) // Button that triggered the modal
    var eventTitle = eventLabel.data('title')
    var eventIssue = eventLabel.data('issue')
    var eventCategory = eventLabel.data('category')
    var eventConcept = eventLabel.data('concept')
    var eventBackground = eventLabel.data('background')
    var eventImportance = eventLabel.data('importance')
    var eventArticle = eventLabel.data('article')
     // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    console.log(eventTitle)
    var modal = $(this)
    if (eventCategory === '정치') {
        modal.find('.modal-event-title').removeClass('bg-danger')
        modal.find('.modal-event-title').removeClass('bg-warning')
        modal.find('.modal-event-title').removeClass('bg-violet')
        modal.find('.modal-event-title').addClass('bg-danger')
    } else if (eventCategory === '사회') {
        modal.find('.modal-event-title').removeClass('bg-danger')
        modal.find('.modal-event-title').removeClass('bg-success')
        modal.find('.modal-event-title').removeClass('bg-violet')
        modal.find('.modal-event-title').addClass('bg-warning')
    } else if (eventCategory === '경제'){
        modal.find('.modal-event-title').removeClass('bg-danger')
        modal.find('.modal-event-title').removeClass('bg-warning')
        modal.find('.modal-event-title').removeClass('bg-violet')
        modal.find('.modal-event-title').addClass('bg-success')
    } else if (eventCategory === '세계'){
        modal.find('.modal-event-title').removeClass('bg-danger')
        modal.find('.modal-event-title').removeClass('bg-warning')
        modal.find('.modal-event-title').removeClass('bg-success')
        modal.find('.modal-event-title').addClass('bg-violet')

    }
    modal.find('.modal-event-title').text(eventTitle)
    modal.find('.modal-event-issue').text(eventIssue)
    modal.find('.modal-event-concept').text(eventConcept)
    modal.find('.modal-event-background').text(eventBackground)
    modal.find('.modal-event-importance').text(eventImportance)
    modal.find('.modal-event-article').text(eventArticle)
})
