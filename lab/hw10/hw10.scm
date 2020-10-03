(define (accumulate combiner start n term)
	(if (= n 0) start
      	(combiner (term n) (accumulate combiner start (- n 1) term))
   	)
)


(define (accumulate-tail combiner start n term)
	(if (= n 0) start
      	(accumulate-tail combiner (combiner (term n) start) (- n 1) term)
   	)
)



(define (partial-sums stream)
  (define (helper start stream)
  	(if (null? stream) nil
  		(cons-stream (+ (car stream) start)
  					(helper (+ (car stream) start) (cdr-stream stream))
  		)
  	
  	)	
  )

  (helper 0 stream)
)






(define (rle s)
	(define (helper prev cnt s)
		(if (null? s) (cons-stream (cons prev (cons cnt nil)) nil)
			(if (= (car s) prev)
				(helper prev (+ cnt 1) (cdr-stream s))
				(cons-stream (cons prev (cons cnt nil))
							(helper (car s) 1 (cdr-stream s))
				)
			)
		)
	)
	(if (null? s) nil
		(helper (car s) 1 (cdr-stream s)) 
	) 
)






















