import logging
import os
from concurrent import futures

from typing import Text

import calculator_pb2
import calculator_pb2_grpc

import grpc

_PORT = os.environ["PORT"]

class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def Calculate(self,
                  request: calculator_pb2.BinaryOperation,
                  context: grpc.ServicerContext) -> None:
        logging.info("Received request: %s", request)
        if request.operation == calculator_pb2.ADD:
            result = request.first_operand + request.second_operand
        else:
            result = request.first_operand - request.second_operand
        return calculator_pb2.CalculationResult(result=result)

    def CalculateComplex(self,
                  request: calculator_pb2.ComplexOperation,
                  context: grpc.ServicerContext) -> None:
        logging.info("Received complex request: %s", request)
        if request.operation == calculator_pb2.ADD:
            rr = request.first_operand.real + request.second_operand.real
            ri = request.first_operand.imaginary + request.second_operand.imaginary
        else:
            rr = request.first_operand.real - request.second_operand.real
            ri = request.first_operand.imaginary - request.second_operand.imaginary
        result = calculator_pb2.ComplexNumber(real= rr, imaginary=ri)
        return calculator_pb2.ComplexResult(result=result)
        ### alternative
        # complexResult = calculator_pb2.ComplexResult()
        # complexResult.result.copy(result)
        ### another alternative 
        # complexResult = calculator_pb2.ComplexResult()
        # complexResult.result.real = result.real
        # complexResult.result.imaginary = result.imaginary


def _serve(port: Text):
    bind_address = f"[::]:{port}"
    server = grpc.server(futures.ThreadPoolExecutor())
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port(bind_address)
    server.start()
    logging.info("Listening on %s.", bind_address)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _serve(_PORT)
