$.circleProgress={defaults:{value:0,size:100,startAngle:-Math.PI,thickness:'auto',fill:{gradient:['#3aeabb','#fdd250']},emptyFill:'rgba(0, 0, 0, .1)',animation:{duration:1200,easing:'circleProgressEasing'}}};$.easing.circleProgressEasing=function(x,t,b,c,d){if((t/=d/2)<1)
return c/2*t*t*t+b;return c/2*((t-=2)*t*t+2)+b;};$.fn.circleProgress=function(options){if(options=='widget')
return this.data('circle-progress');options=$.extend({},$.circleProgress.defaults,options);return this.each(function(){var el=$(this),size=options.size,radius=size/2,thickness=size/14,value=options.value,startAngle=options.startAngle,emptyArcFill=options.emptyFill,arcFill;if($.isNumeric(options.thickness))
thickness=options.thickness;var canvas=el.data('circle-progress');if(!canvas){canvas=$('<canvas>').prependTo(el)[0];el.data('circle-progress',canvas);}
canvas.width=size;canvas.height=size;var ctx=canvas.getContext('2d');if(!options.fill)
throw Error("The fill is not specified!");if(options.fill.color)
arcFill=options.fill.color;if(options.fill.gradient){var gr=options.fill.gradient;if(gr.length==1){arcFill=gr[0];}else if(gr.length>1){var lg=ctx.createLinearGradient(0,0,size,0);for(var i=0;i<gr.length;i++)
lg.addColorStop(i/(gr.length-1),gr[i]);arcFill=lg;}}
if(options.fill.image){var img=new Image();img.src=options.fill.image;img.onload=function(){var bg=$('<canvas>')[0];bg.width=size;bg.height=size;bg.getContext('2d').drawImage(img,0,0,size,size);arcFill=ctx.createPattern(bg,'no-repeat');if(!options.animation)
draw(value);}}
if(options.animation)
drawAnimated(value);else
draw(value);function draw(v){ctx.clearRect(0,0,size,size);drawArc(v);drawEmptyArc(v);}
function drawArc(v){ctx.save();ctx.beginPath();ctx.arc(radius,radius,radius-thickness/2,startAngle,startAngle+Math.PI*2*v);ctx.lineWidth=thickness;ctx.strokeStyle=arcFill;ctx.stroke();ctx.restore();}
function drawEmptyArc(v){ctx.save();if(v<1){ctx.beginPath();if(v<=0)
ctx.arc(radius,radius,radius-thickness/2,0,Math.PI*2);else
ctx.arc(radius,radius,radius-thickness/2,startAngle+Math.PI*2*v,startAngle);ctx.lineWidth=thickness;ctx.strokeStyle=emptyArcFill;ctx.stroke();}
ctx.restore();}
function drawAnimated(v){el.trigger('circle-animation-start');$(canvas).css({progress:0}).animate({progress:v},$.extend({},options.animation,{step:function(p){draw(p);el.trigger('circle-animation-progress',[p/v,p]);},complete:function(){el.trigger('circle-animation-end');}}));}});};