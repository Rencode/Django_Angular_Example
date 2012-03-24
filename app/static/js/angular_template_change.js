angular.markup('(())', function(text, textNode, parentElement){
  if (parentElement[0].nodeName.toLowerCase() == 'script') return;
  text = text.replace(/\(\(/g,'{{').replace(/\)\)/g, '}}');
  textNode.text(text);
  return angular.markup('{{}}').call(this, text, textNode, parentElement);
});