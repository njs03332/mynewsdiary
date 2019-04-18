// for event modal
$('#eventModal').on('show.bs.modal', function (event) {
    var eventLabel = $(event.relatedTarget) // Button that triggered the modal
    var eventTitle = eventLabel.data('title')
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
    modal.find('.modal-event-title').text(eventTitle)
    modal.find('.modal-event-category').text(eventCategory)
    modal.find('.modal-event-concept').text(eventConcept)
    modal.find('.modal-event-background').text(eventBackground)
    modal.find('.modal-event-importance').text(eventImportance)
    modal.find('.modal-event-article').text(eventArticle)
})
