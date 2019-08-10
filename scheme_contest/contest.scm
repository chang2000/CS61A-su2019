;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (draw)
  ; YOUR CODE HERE
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
 (hideturtle)
  (penup)
  (goto 10 10)
  (pendown)
  (backward 100)
  (left 60)
  (backward 30)
  (penup)
  (goto 10 -90)
  (pendown)
  (left 60)
  (backward 30)
  (penup)
  (goto 10 95)
  (pendown)
  (circle 50)
  (penup)
  (goto 50 60)
  (pendown)
  (circle 10)
  (penup)
  (goto 50 30)
  (pendown)
  (right 100)
  (backward 25)
  (penup)
  (goto 10 -30)
  (pendown)
  (left 60)
  (backward 30)
  (penup)
  (goto 10 -30)
  (pendown)
  (forward 30)
  (left 80)
  (exitonclick))
(draw)
