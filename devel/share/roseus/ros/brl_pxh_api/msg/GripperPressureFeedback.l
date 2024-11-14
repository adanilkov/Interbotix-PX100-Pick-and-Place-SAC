;; Auto-generated. Do not edit!


(when (boundp 'brl_pxh_api::GripperPressureFeedback)
  (if (not (find-package "BRL_PXH_API"))
    (make-package "BRL_PXH_API"))
  (shadow 'GripperPressureFeedback (find-package "BRL_PXH_API")))
(unless (find-package "BRL_PXH_API::GRIPPERPRESSUREFEEDBACK")
  (make-package "BRL_PXH_API::GRIPPERPRESSUREFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude GripperPressureFeedback.msg.html


(defclass brl_pxh_api::GripperPressureFeedback
  :super ros::object
  :slots (_log ))

(defmethod brl_pxh_api::GripperPressureFeedback
  (:init
   (&key
    ((:log __log) "")
    )
   (send-super :init)
   (setq _log (string __log))
   self)
  (:log
   (&optional __log)
   (if __log (setq _log __log)) _log)
  (:serialization-length
   ()
   (+
    ;; string _log
    4 (length _log)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _log
       (write-long (length _log) s) (princ _log s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _log
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _log (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get brl_pxh_api::GripperPressureFeedback :md5sum-) "c3e2a6f3c8b4a69b39bb08b44fadcdca")
(setf (get brl_pxh_api::GripperPressureFeedback :datatype-) "brl_pxh_api/GripperPressureFeedback")
(setf (get brl_pxh_api::GripperPressureFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback
string log


")



(provide :brl_pxh_api/GripperPressureFeedback "c3e2a6f3c8b4a69b39bb08b44fadcdca")

