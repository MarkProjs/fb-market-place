"use strict";

/**
 * @author Jeremy Tang
 * Changes class names to change the layout
 * from list to grid, and vice-versa.
 */

// document.addEventListener('DOMContentLoaded', setup)

const checkbox = document.getElementById('myCheckbox')

const col = document.getElementsByClassName('col-md-8')
const articles = document.getElementsByClassName('articles')
const contentSection = document.getElementsByClassName('content-section')
const content = document.getElementsByClassName('content')
const contentImage = document.getElementsByClassName('content-image')

var oldCol = ''
var oldArticles = ''
var oldContentSection = ''
var oldContent = ''
var oldContentImage = ''

checkbox.addEventListener('change', (event) => {
  if (event.currentTarget.checked) {
    addAll()
  } else {
    resetAll()
  }
})

function addClass(classList, newClass){
  var oldClass = classList[0].className;
  for(let i = 0; i < classList.length; i++) {
    classList[i].className += ' ' + newClass;
  }
  return oldClass
}

function addAll(){
  oldCol = addClass(col, 'col-md-8-grid')
  oldArticles = addClass(articles, 'articles-grid')
  oldContentSection = addClass(contentSection, 'content-section-grid')
  oldContent = addClass(content, 'content-grid')
  oldContentImage = addClass(contentImage, 'content-image-grid')
  console.log('added')
}

function resetClass(classList, oldClass){
  for(let i = 0; i < classList.length; i++) {
    classList[i].className = oldClass;
  }
}

function resetAll(){
  resetClass(col, oldCol)
  resetClass(articles, oldArticles)
  resetClass(contentSection, oldContentSection)
  resetClass(content, oldContent)
  resetClass(contentImage, oldContentImage)
}

// function setup(){

// }