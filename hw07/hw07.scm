(define (square n) (* n n))

(define (pow base exp)
  (cond ((= exp 0) 1)
        ((= exp 1) base)
        (else
          (let ((half-power (pow base (quotient exp 2))))
            (if (even? exp)
                (square half-power)
                (* base (square half-power)))))))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))
