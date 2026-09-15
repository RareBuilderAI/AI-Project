'use strict';
const VaultCrypto=(()=>{
 const iterations=600000,enc=new TextEncoder(),dec=new TextDecoder();
 const b64=a=>{let s='';for(const n of new Uint8Array(a))s+=String.fromCharCode(n);return btoa(s);};
 const bytes=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
 function validate(v){if(!v||v.version!==1||v.iterations!==iterations||typeof v.salt!=='string'||typeof v.iv!=='string'||typeof v.data!=='string'||v.data.length>2000000||bytes(v.salt).length!==16||bytes(v.iv).length!==12||bytes(v.data).length<16)throw Error('Unsupported or damaged backup.');return v;}
 async function key(password,salt){const material=await crypto.subtle.importKey('raw',enc.encode(password),'PBKDF2',false,['deriveKey']);return crypto.subtle.deriveKey({name:'PBKDF2',hash:'SHA-256',salt:bytes(salt),iterations},material,{name:'AES-GCM',length:256},false,['encrypt','decrypt']);}
 function salt(){return b64(crypto.getRandomValues(new Uint8Array(16)));}
 async function seal(entries,k,s){const iv=crypto.getRandomValues(new Uint8Array(12));const data=await crypto.subtle.encrypt({name:'AES-GCM',iv,additionalData:enc.encode('raremotion-vault-v1')},k,enc.encode(JSON.stringify(entries)));return {version:1,iterations,salt:s,iv:b64(iv),data:b64(data)};}
 async function open(v,k){validate(v);const raw=await crypto.subtle.decrypt({name:'AES-GCM',iv:bytes(v.iv),additionalData:enc.encode('raremotion-vault-v1')},k,bytes(v.data));const entries=JSON.parse(dec.decode(raw));if(!Array.isArray(entries)||entries.length>200||entries.some(e=>!e||typeof e.id!=='string'||e.id.length>100||!['title','username','password'].every(f=>typeof e[f]==='string'&&e[f].length<=2000))||new Set(entries.map(e=>e.id)).size!==entries.length)throw Error('Invalid vault contents.');return entries;}
 return {key,salt,seal,open,validate};
})();
if(typeof module!=='undefined')module.exports=VaultCrypto;
