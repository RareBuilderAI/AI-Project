'use strict';
const FileOrganizer = (() => {
  const types = {
    Images: 'jpg jpeg png gif webp svg heic heif avif bmp tiff tif ico raw',
    Documents: 'pdf doc docx odt txt rtf md pages epub',
    Spreadsheets: 'xls xlsx csv tsv ods numbers',
    Presentations: 'ppt pptx odp key',
    Music: 'mp3 wav flac aac ogg m4a aiff opus',
    Videos: 'mp4 mov avi mkv webm m4v wmv mpg mpeg',
    Archives: 'zip rar 7z tar gz bz2 xz',
    Code: 'js ts jsx tsx py html css json xml yaml yml sql sh java c cpp h rs go rb php'
  };
  function category(name) {
    const dot = name.lastIndexOf('.'), ext = dot > 0 ? name.slice(dot+1).toLowerCase() : '';
    return Object.keys(types).find(k => types[k].split(' ').includes(ext)) || 'Other';
  }
  function plan(files) {
    if (files.length > 500 || files.reduce((sum,f)=>sum+f.size,0) > 100*1024*1024) throw Error('Choose at most 500 files totaling 100 MB.');
    const used = new Set();
    return files.map(file => {
      let name = file.name.replace(/[\\/:*?"<>|\x00-\x1f\x7f]/g,'_').replace(/[. ]+$/g,'');
      if (!name || name === '.' || name === '..') name='unnamed';
      if (/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\.|$)/i.test(name)) name='_'+name;
      const folder=category(file.name), dot=name.lastIndexOf('.');
      const stem=dot>0?name.slice(0,dot):name, ext=dot>0?name.slice(dot):'';
      let candidate=name, suffix=2;
      while(used.has((folder+'/'+candidate).normalize('NFC').toLowerCase())) candidate=stem+' ('+(suffix++)+')'+ext;
      used.add((folder+'/'+candidate).normalize('NFC').toLowerCase());
      return {file,folder,path:folder+'/'+candidate};
    });
  }
  const table=Uint32Array.from({length:256},(_,n)=>{for(let k=0;k<8;k++)n=(n&1)?0xedb88320^(n>>>1):n>>>1;return n>>>0;});
  function crc32(bytes){let c=0xffffffff;for(const b of bytes)c=table[(c^b)&255]^(c>>>8);return (c^0xffffffff)>>>0;}
  async function zip(entries, progress=()=>{}) {
    const parts=[], directory=[];let offset=0,centralSize=0;
    for(let i=0;i<entries.length;i++) {
      const {file,path}=entries[i], data=new Uint8Array(await file.arrayBuffer()), name=new TextEncoder().encode(path);
      if(name.length>65535)throw Error('A filename is too long. Rename it and try again.');
      const crc=crc32(data), local=new Uint8Array(30), h=new DataView(local.buffer);
      h.setUint32(0,0x04034b50,true);h.setUint16(4,20,true);h.setUint16(6,0x800,true);h.setUint16(12,33,true);h.setUint32(14,crc,true);h.setUint32(18,data.length,true);h.setUint32(22,data.length,true);h.setUint16(26,name.length,true);
      parts.push(local,name,data);
      const center=new Uint8Array(46),d=new DataView(center.buffer);
      d.setUint32(0,0x02014b50,true);d.setUint16(4,20,true);d.setUint16(6,20,true);d.setUint16(8,0x800,true);d.setUint16(14,33,true);d.setUint32(16,crc,true);d.setUint32(20,data.length,true);d.setUint32(24,data.length,true);d.setUint16(28,name.length,true);d.setUint32(42,offset,true);
      directory.push(center,name);offset+=local.length+name.length+data.length;centralSize+=center.length+name.length;
      progress(i+1,entries.length);
      await new Promise(resolve=>setTimeout(resolve,0));
    }
    const end=new Uint8Array(22),e=new DataView(end.buffer);e.setUint32(0,0x06054b50,true);e.setUint16(8,entries.length,true);e.setUint16(10,entries.length,true);e.setUint32(12,centralSize,true);e.setUint32(16,offset,true);
    return new Blob([...parts,...directory,end],{type:'application/zip'});
  }
  return {plan,zip,category};
})();
if(typeof module !== 'undefined') module.exports=FileOrganizer;
if(typeof document !== 'undefined') (()=>{
  const $=id=>document.getElementById(id);let entries=[],busy=false;
  const size=n=>n<1024?n+' B':n<1048576?(n/1024).toFixed(1)+' KB':(n/1048576).toFixed(1)+' MB';
  function render(){
    $('preview').replaceChildren();$('empty').hidden=entries.length>0;$('download').disabled=!entries.length||busy;$('clear').disabled=!entries.length||busy;
    $('count').textContent=entries.length?entries.length+' files · '+size(entries.reduce((n,e)=>n+e.file.size,0)):'No files selected';
    const folders=[...new Set(entries.map(e=>e.folder))].sort();
    for(const folder of folders){const group=entries.filter(e=>e.folder===folder),title=document.createElement('h3');title.className='group';title.textContent=folder+' / '+group.length;const list=document.createElement('ul');for(const entry of group){const row=document.createElement('li');row.className='file';const name=document.createElement('span');name.textContent=entry.path.slice(folder.length+1);const bytes=document.createElement('small');bytes.textContent=size(entry.file.size);row.append(name,bytes);list.append(row);}$('preview').append(title,list);}
  }
  $('files').addEventListener('change',()=>{try{entries=FileOrganizer.plan(Array.from($('files').files));$('notice').textContent=entries.length?'Preview ready. Your original files are unchanged.':'';}catch(error){entries=[];$('files').value='';$('notice').textContent=error.message;}render();});
  $('clear').onclick=()=>{if(busy)return;entries=[];$('files').value='';$('notice').textContent='Selection cleared. Your original files are unchanged.';render();};
  $('download').onclick=async()=>{if(busy||!entries.length)return;busy=true;$('files').disabled=true;render();try{const blob=await FileOrganizer.zip(entries,(n,total)=>{$('notice').textContent='Preparing file '+n+' of '+total+'…';});const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='raremotion-organized-files.zip';a.click();setTimeout(()=>URL.revokeObjectURL(url),60000);$('notice').textContent='ZIP ready. Check your downloads and extract it to see the folders.';}catch(error){$('notice').textContent='Could not prepare the ZIP. Try fewer files or select them again.';}finally{busy=false;$('files').disabled=false;render();}};
  render();
})();
