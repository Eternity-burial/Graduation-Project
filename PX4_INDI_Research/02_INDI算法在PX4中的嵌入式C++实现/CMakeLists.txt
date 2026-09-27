px4_add_module(
	MODULE modules__rate_control_indi
	MAIN rate_control_indi
	STACK_MAIN 2048
	SRCS
		RateControlINDI.cpp
	DEPENDS
		matrix
		px4_work_queue
	)
