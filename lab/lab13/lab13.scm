; Lab 13: Final Review

; Q3
(define (compose-all funcs)
 	(define (helper funcs x)
 		(if (null? funcs) x
 			(helper (cdr funcs) ((car funcs) x))
 		)


 	)
 	(lambda (x) (helper funcs x))
)