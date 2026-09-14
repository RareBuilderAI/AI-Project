'use strict';
(() => {
 const $ = id => document.getElementById(id);
 const key = 'raremotion.support.business.v1';
 const lab = {name:'Raremotion Labs',email:'founder@raremotionlabs.com',description:'Help with our everyday tools, projects, and getting in touch.',faqs:[
 {question:'How do I contact Raremotion Labs?',answer:'Email founder@raremotionlabs.com to discuss a project or ask for help. Use the Email support link to open your email app.'},
 {question:'Where can I find the projects?',answer:'Use All projects at the top of this page to explore Task Studio, the Crypto Dashboard, Contact Book, Password Generator, and File Organizer.'},
 {question:'Does File Organizer upload or move my files?',answer:'No. It creates an organized ZIP of copies on your device. Your originals are not moved, renamed, or deleted. Select up to 500 files, totaling 100 MB.'},
 {question:'Are generated passwords saved?',answer:'The Password Generator uses your browser’s cryptographic random generator. It does not save or send passwords. Copying a password places it on your clipboard.'},
 {question:'Where are my contacts stored?',answer:'Contact Book stores contacts in this browser. They do not automatically sync to other devices. Export a backup before clearing browser data.'},
 {question:'Can I set up support for my own business?',answer:'Yes. Select Your business, add your public business details and FAQs, then save the setup in this browser. This preview does not publish a customer support site. AI chat is still awaiting connection.'},
 {question:'Is this an AI chat assistant yet?',answer:'Not yet. These are written FAQs. The AI service must be connected before this page can generate replies.'}
 ]};
 let mode='lab', saved=null;
 const valid = value => value && typeof value.name==='string' && value.name.length>0 && value.name.length<=80 && typeof value.description==='string' && value.description.length<=600 && typeof value.email==='string' && /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(value.email) && value.email.length<=254 && Array.isArray(value.faqs) && value.faqs.length<=20 && value.faqs.every(f=>f && typeof f.question==='string' && f.question.length>0 && f.question.length<=200 && typeof f.answer==='string' && f.answer.length>0 && f.answer.length<=2000);
 try { const value=JSON.parse(localStorage.getItem(key)); if(valid(value)) saved=value; } catch { $('notice').textContent='Browser storage is unavailable. You can still prepare and export a setup in this session.'; }
 function render(){
  const profile=mode==='lab'?lab:saved;
  $('space-name').textContent=profile?.name || 'Your business';
  $('space-description').textContent=profile?.description || 'Add your details below to preview your own help centre.';
  $('contact').hidden=!profile;
  $('contact-note').hidden=!profile;
  if(profile) $('contact').href='mailto:'+encodeURIComponent(profile.email);
  $('storage-note').textContent=mode==='lab'?'Choose a question or search the help topics. For anything else, contact the team.':'Your saved business preview is available only in this browser. AI chat is not connected.';
  const terms=$('search').value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const faqs=(profile?.faqs||[]).filter(f=>terms.every(t=>(f.question+' '+f.answer).toLocaleLowerCase().includes(t)));
  $('answers').replaceChildren();
  faqs.forEach(f=>{const d=document.createElement('details'),s=document.createElement('summary'),p=document.createElement('p');s.textContent=f.question;p.textContent=f.answer;d.append(s,p);$('answers').append(d);});
  $('result-count').textContent=faqs.length+(faqs.length===1?' answer':' answers');
  $('empty').hidden=faqs.length>0;
  $('empty').textContent=profile?'No matching answers. Try another word or contact support.':'Save your business details and FAQs below to see your help centre.';
  $('export').disabled=!saved;
 }
 function addFAQ(f={question:'',answer:''}){
  if($('faq-editor').children.length>=20)return;
  const row=document.createElement('div');row.className='faq-row';
  const qlabel=document.createElement('label'),alabel=document.createElement('label'),q=document.createElement('input'),a=document.createElement('textarea'),remove=document.createElement('button');
  qlabel.textContent='Question';alabel.textContent='Answer';q.required=a.required=true;q.maxLength=200;a.maxLength=2000;a.rows=3;q.value=f.question;a.value=f.answer;q.className='question';a.className='answer';
  remove.type='button';remove.className='secondary';remove.textContent='Remove question';remove.onclick=()=>{row.remove();$('add-faq').disabled=false;$('add-faq').focus();};
  qlabel.append(q);alabel.append(a);row.append(qlabel,alabel,remove);$('faq-editor').append(row);$('add-faq').disabled=$('faq-editor').children.length>=20;
 }
 function changeMode(value){mode=value;$('lab-mode').setAttribute('aria-pressed',String(value==='lab'));$('business-mode').setAttribute('aria-pressed',String(value==='business'));$('business-setup').hidden=value!=='business';$('search').value='';$('search').placeholder=value==='lab'?'Try files, passwords, or contact':'Search your saved answers';render();}
 $('lab-mode').onclick=()=>changeMode('lab');$('business-mode').onclick=()=>changeMode('business');$('search').oninput=render;
 $('business-name').value=saved?.name||'';$('business-email').value=saved?.email||'';$('business-description').value=saved?.description||'';
 (saved?.faqs.length?saved.faqs:[{question:'',answer:''}]).forEach(addFAQ);
 $('add-faq').onclick=()=>{addFAQ();$('faq-editor').lastElementChild.querySelector('input').focus();};
 $('setup-form').onsubmit=e=>{e.preventDefault();const value={name:$('business-name').value.trim(),email:$('business-email').value.trim(),description:$('business-description').value.trim(),faqs:[...$('faq-editor').children].map(row=>({question:row.querySelector('.question').value.trim(),answer:row.querySelector('.answer').value.trim()}))};
 if(!valid(value)||!value.description||!value.faqs.length){$('notice').textContent='Add a business name, valid email, description, and at least one complete question and answer.';return;}
 saved=value;try{localStorage.setItem(key,JSON.stringify(saved));$('notice').textContent='Business setup saved in this browser. Your preview above is updated.';}catch{$('notice').textContent='Updated for this session only. Browser storage is unavailable; export a backup.';}render();};
 $('export').onclick=()=>{if(!saved)return;const blob=new Blob([JSON.stringify(saved,null,2)],{type:'application/json'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='business-support-setup.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);$('notice').textContent='Backup download requested. This contains your last saved setup.';};
 render();
})();
