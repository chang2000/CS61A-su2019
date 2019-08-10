(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ 3 x)) multiples-of-three))
)

(define (rle s)
  'YOUR-CODE-HERE
    (define (helper head s n)
        (cond ((null? s) (cons-stream (list head n) nil))
        ((= head (car s)) (helper head (cdr-stream s) (+ n 1)))
        (else (cons-stream (list head n) (helper(car s) (cdr-stream s) 1)))
        ))
    (if (null? s) nil
        (helper (car s) (cdr-stream s) 1)))
