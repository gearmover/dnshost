# DNS Host
A **very** simple Python script to add a REST interface to dnsmasq.  It has no authentication, no error checking, and just one route:

  /add/[hostname]/[ipaddress]

That will add the hostname and IP address to a custom hosts file at /etc/dns.conf, presumably so dnsmasq can pick it up using

  addn-hosts=/etc/dns.conf

And poof, now you have an easy-to-update interface to your local DNS server!  This was a quick script, writing this readme's probably taken longer, so expect bugs and  I hope you
take the idea more than line-for-line copy the code, however, it's MIT licensed so use it how you like.

Thanks for stopping by!
