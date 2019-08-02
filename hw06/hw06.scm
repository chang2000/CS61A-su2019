;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons (car s) (filter (lambda (x) (not (eq? x (car s)))) (unique (cdr s))))
  )
)

(define (cons-all first rests)
  (map (lambda (x) (append (list first) x)) rests))

; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  'YOUR-CODE-HERE
  (cond
    ((null? denoms) nil)
    ((< total 0) nil)
    ((= total 0) (cons (cons (car denoms) nil) nil))
    ((> (car denoms) total) (list-change total (cdr denoms)))
    ((= (car denoms) total) (append (list-change (- total (car denoms)) denoms) (list-change total (cdr denoms))))
    (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
  ))

; Tail recursion

(define (replicate x n)
  'YOUR-CODE-HERE
  (define (replicate-tail n lst-so-far)
    (if (= n 0) lst-so-far
      (replicate-tail (- n 1) (append lst-so-far (list x)))
      ))
  (replicate-tail n (list)))

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0) start
    (combiner (term n) (accumulate combiner start (- n 1) term))))

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (define (accumulate-tail curr total)
    (if (= curr (+ 1 n)) total
      (accumulate-tail (+ curr 1) (combiner total (term curr)))
  ))
  (accumulate-tail 1 start))


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
    `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)
