'use strict';
class LabCalculator {
 constructor(){this.clear();this.history=[];}
 clear(){this.display='0';this.left=null;this.operator=null;this.fresh=true;this.error=false;}
 format(n){if(!Number.isFinite(n))throw Error('Result is too large');return String(Number(n.toPrecision(12)));}
 digit(d){if(this.error)this.clear();if(this.display.includes('e'))this.fresh=true;if(this.fresh){this.display=d==='.'?'0.':d;this.fresh=false;}else if(d==='.'&&!this.display.includes('.')&&!this.display.includes('e'))this.display+='.';else if(d!=='.'&&this.display.replace(/[-.]/g,'').length<15)this.display=this.display==='0'?d:this.display+d;}
 sign(){if(!this.error&&Number(this.display)!==0){this.display=this.display.startsWith('-')?this.display.slice(1):'-'+this.display;this.fresh=false;}}
 percent(){if(this.error)return;this.display=this.format(Number(this.display)/100);this.fresh=false;}
 back(){if(this.error){this.clear();return;}if(this.fresh)return;if(this.display.includes('e')){this.display='0';return;}this.display=this.display.slice(0,-1);if(!this.display||this.display==='-')this.display='0';}
 calculate(){if(this.left===null||!this.operator||this.fresh)return;const a=this.left,b=Number(this.display);if(this.operator==='÷'&&b===0)throw Error('Cannot divide by zero');const n=this.operator==='+'?a+b:this.operator==='−'?a-b:this.operator==='×'?a*b:a/b;const result=this.format(n);this.history.unshift({expression:a+' '+this.operator+' '+b,result});this.history=this.history.slice(0,10);this.display=result;this.left=null;this.operator=null;this.fresh=true;}
 op(value){if(this.error)return;if(this.operator&&!this.fresh)this.calculate();this.left=Number(this.display);this.operator=value;this.fresh=true;}
 act(value){try{if(/^\d$/.test(value)||value==='.')this.digit(value);else if(value==='AC')this.clear();else if(value==='±')this.sign();else if(value==='%')this.percent();else if(value==='⌫')this.back();else if(value==='=')this.calculate();else if(['+','−','×','÷'].includes(value))this.op(value);}catch(e){this.display=e.message;this.error=true;this.left=null;this.operator=null;this.fresh=true;}}
}
if(typeof module!=='undefined')module.exports=LabCalculator;
