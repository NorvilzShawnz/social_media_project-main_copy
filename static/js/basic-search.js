function basicSearchSetup(searchBarID, searchBtnID, displayedResultsList, searchResultContainerIdPrefix) {
    document.getElementById(searchBarID)
    .addEventListener("keyup", () => {
        basicSearch(searchBarID, displayedResultsList, searchResultContainerIdPrefix)
    })

    document.getElementById(searchBtnID)
    .addEventListener("click", () => {
        basicSearch(searchBarID, displayedResultsList, searchResultContainerIdPrefix)
    })
}

function basicSearch(searchBarID, displayedResultsList, searchResultContainerIdPrefix) {
    const searchKeyWords = document.getElementById(searchBarID).value.toUpperCase().split(" ")

    makeAPostBox = document.getElementById("make-a-post-box")
    if(makeAPostBox) {
        if (searchKeyWords.length > 1 || searchKeyWords[0] != "") {
            makeAPostBox.style.display = "none"
        } else {
            makeAPostBox.style.display = ""
        }
    }

    displayedResultsList.forEach((displayedResult) => {
        let postDisplayContainer = document.getElementById(searchResultContainerIdPrefix + displayedResult.id)
        
        let keywordsAllIncluded = true
        searchKeyWords.forEach((searchKeyWord) => {
            if (!displayedResult.strToMatchWithKeywords.toUpperCase().includes(searchKeyWord)) {
                keywordsAllIncluded = false
            }
        })
        
        if(!keywordsAllIncluded) {
            postDisplayContainer.style.display = "none"
        } else {
            postDisplayContainer.style.display = ""
        }
    })
}