"use strict";
(() => {
  const key = "raremotion.tasks.v1";
  let tasks = [], filter = "all", removed = null;
  const $ = id => document.getElementById(id);
  const say = text => { $("notice").textContent = text; };
  let storageReadable = true;
  try {
    const saved = JSON.parse(localStorage.getItem(key) || "[]");
    if (!Array.isArray(saved) || !saved.every(t => t && typeof t.id === "string" && typeof t.text === "string" && typeof t.done === "boolean")) throw new Error("Invalid saved tasks");
    tasks = saved;
  } catch (_) { storageReadable = false; say("Saved tasks could not be read. You can work here temporarily and download a backup; existing saved data will not be overwritten."); }
  function save() {
    if (!storageReadable) { say("Temporary session: download a backup to keep your tasks."); return; }
    try { localStorage.setItem(key, JSON.stringify(tasks)); }
    catch (_) { say("Browser storage is unavailable or full. Download a backup before leaving this page."); }
  }
  function render() {
    const done = tasks.filter(t => t.done).length;
    $("summary").textContent = `${done} of ${tasks.length} tasks complete`;
    $("progress").value = tasks.length ? done / tasks.length * 100 : 0;
    const visible = tasks.filter(t => filter === "all" || (filter === "done" ? t.done : !t.done));
    $("count").textContent = `${visible.length} ${visible.length === 1 ? "task" : "tasks"}`;
    $("tasks").replaceChildren();
    visible.forEach(t => {
      const row = document.createElement("li"); row.classList.toggle("done", t.done);
      const label = document.createElement("label");
      const check = document.createElement("input"); check.type = "checkbox"; check.checked = t.done;
      check.setAttribute("aria-label", `${t.done ? "Reopen" : "Complete"} ${t.text}`);
      const title = document.createElement("span"); title.textContent = t.text;
      check.addEventListener("change", () => { t.done = check.checked; save(); render(); });
      label.append(check, title);
      const del = document.createElement("button"); del.textContent = "Delete"; del.setAttribute("aria-label", `Delete ${t.text}`);
      del.addEventListener("click", () => {
        removed = {task:t, index:tasks.indexOf(t)}; tasks = tasks.filter(x => x.id !== t.id);
        say("Task deleted. You can undo this below."); $("undo").hidden = false; save(); render(); $("undo").focus();
      });
      row.append(label,del); $("tasks").append(row);
    });
    $("empty").hidden = visible.length > 0;
    $("empty").querySelector("h3").textContent = tasks.length ? "Nothing in this view yet." : "A clear space. A fresh start.";
    $("empty").querySelector("p").textContent = tasks.length ? "Switch filters to see your other tasks." : "Add your first task above and turn an idea into progress.";
  }
  $("add-form").addEventListener("submit", event => {
    event.preventDefault(); const text = $("task").value.trim(); if (!text) { $("task").focus(); return; }
    tasks.push({id:crypto.randomUUID(),text,done:false}); $("task").value = "";
    filter = "all"; updateFilters(); say("Task added."); save(); render(); $("task").focus();
  });
  function updateFilters() { document.querySelectorAll("[data-filter]").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.filter === filter))); }
  document.querySelectorAll("[data-filter]").forEach(b => b.addEventListener("click", () => {filter=b.dataset.filter;updateFilters();render();}));
  $("undo").addEventListener("click", () => { if (!removed) return; tasks.splice(removed.index,0,removed.task); removed=null; $("undo").hidden=true; say("Task restored."); save();render();$("task").focus(); });
  $("export").addEventListener("click", () => {
    const url=URL.createObjectURL(new Blob([JSON.stringify(tasks,null,2)],{type:"application/json"}));
    const a=document.createElement("a");a.href=url;a.download="raremotion-tasks.json";a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);say("Task backup downloaded.");
  });
  render();
})();