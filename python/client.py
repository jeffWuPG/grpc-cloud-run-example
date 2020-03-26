import argparse
import functools

from typing import Text

import grpc

import calculator_pb2
import calculator_pb2_grpc


_OPERATIONS = {
    "add": calculator_pb2.ADD,
    "subtract": calculator_pb2.SUBTRACT,
}


def _calculate(server_address: Text,
               operation: calculator_pb2.Operation,
               a: float,
               b: float,
               plaintext: bool) -> float:
    if plaintext:
        channel = grpc.insecure_channel(server_address)
    else:
        channel = grpc.secure_channel(server_address, grpc.ssl_channel_credentials())
    try:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        request = calculator_pb2.BinaryOperation(first_operand=a,
                                                 second_operand=b,
                                                 operation=operation)
        return stub.Calculate(request).result
    finally:
        channel.close()

def _calculateComplex(server_address: Text,
               operation: calculator_pb2.Operation,
               a: calculator_pb2.ComplexNumber,
               b: calculator_pb2.ComplexNumber,
               plaintext: bool) -> calculator_pb2.ComplexNumber:
    if plaintext:
        channel = grpc.insecure_channel(server_address)
    else:
        channel = grpc.secure_channel(server_address, grpc.ssl_channel_credentials())
    try:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        request = calculator_pb2.ComplexOperation(first_operand=a,
                                                 second_operand=b,
                                                 operation=operation)
        return stub.CalculateComplex(request)
    finally:
        channel.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server",
                        help="The address of the calculator server.")
    parser.add_argument("operation",
                        choices=_OPERATIONS.keys(),
                        help="The operation to perform")
    parser.add_argument("ar", type=float, help="The first operand real part.")
    parser.add_argument("ai", type=float, help="The first operand imaginary part.")
    parser.add_argument("br", type=float, help="The second operand real part.")
    parser.add_argument("bi", type=float, help="The second operand imaginary part.")
    parser.add_argument("-k", "--plaintext",
                        action="store_true",
                        help="When set, establishes a plaintext connection. " +
                             "Useful for debugging locally.")
    args = parser.parse_args()
    a = calculator_pb2.ComplexNumber(real= args.ar, imaginary=args.ai)
    b = calculator_pb2.ComplexNumber(real= args.br, imaginary=args.bi)
    complextResult = _calculateComplex(args.server,
                     _OPERATIONS[args.operation],
                     a, b, args.plaintext)
    
    result = complextResult.result
    print('real: ' + str(result.real) + ' imaginary: ' + str(result.imaginary))
