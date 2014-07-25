
var gene_height = 10;
var gene_width = 20;
var arrow_width = gene_width*0.5;
var arrow_height = gene_height*0.5

function path_line(x,y) {
  return 'l '+x+' '+y+' ';
}
var gene_f = path_line(0,gene_height*-1) + path_line(gene_width,0)
            + path_line(arrow_width,arrow_height) 
            + path_line(arrow_width*-1,arrow_height) + 'z';
var gene_r = path_line(0,gene_height) + path_line(gene_width*-1,0)
            + path_line(arrow_width*-1,arrow_height*-1) 
            + path_line(arrow_width,arrow_height*-1) + 'z';

window.onload = function() {
  var paper = new Raphael( document.getElementById('canvas_container'), 500, 500 );

  var genes = [ {'name':'abc', 'pos':256, 'strand':'+'}, 
                {'name':'bcd', 'pos':456, 'strand':'-'} ]
  var arrows = []
  for(i=0; i<genes.length; i++) {
    if( genes[i].strand == '+' ) {
      arrows[i]= paper.path('M '+genes[i].pos+' 250 '+gene_f);
      arrows[i].attr({'fill':'#9cf', 'stroke':'#ddd', 'stroke-width':3});
      arrows[i].text = paper.text(genes[i].pos+gene_width*0.5,250-gene_height*1.8,genes[i].name);

      arrows[i].text.hide()
      arrows[i].mouseover( function() { this.text.show(); } )
      arrows[i].mouseout( function() { this.text.hide(); } )

    } else {
      arrows[i]= paper.path('M '+genes[i].pos+' 250 '+gene_r);
      arrows[i].attr({'fill':'#fc9', 'stroke':'#ddd', 'stroke-width':3});
      arrows[i].text = paper.text(genes[i].pos-gene_width*0.5,250+gene_height*1.8,genes[i].name);
      
      arrows[i].text.hide()
      arrows[i].mouseover( function() { this.text.show(); } )
      arrows[i].mouseout( function() { this.text.hide(); } )
    }
  }
}
