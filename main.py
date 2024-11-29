import math
import time

def normal(sigmax, ux, t): 
    y = ( 1 / ( ((2*math.pi)**0.5)*(sigmax) ) ) * ((math.e)**(-0.5*( ( (t-ux)/sigmax )**2  )))
    return y

a00, a01, a10, a11 = map(float, input().split())
a = [[a00, a01], [a10, a11]]
start_pis = list( map(float, input().split()) )
pis = start_pis
T = int(input())
y = {}
for i in range(1, T+1):
    y[i] = float(input())

u = [0, 0]
sigma = [1, 1]
gammas = {}

start = time.time()
for iters in range(120):
    alphas = {}
    val0 = pis[0]*normal(sigma[0], u[0], y[1])
    val1 = pis[1]*normal(sigma[1], u[1], y[1])

    alphas[1] = [ val0/(val0+val1), val1/(val0+val1) ]

    for t in range(1, T):
        val0 = ( normal(sigma[0], u[0], y[t+1]) )*( alphas[t][0]*a[0][0] + alphas[t][1]*a[1][0] )
        val1 = ( normal(sigma[1], u[1], y[t+1]) )*( alphas[t][0]*a[0][1] + alphas[t][1]*a[1][1] )
        alphas[t+1] = [ val0/(val0+val1), val1/(val0+val1) ]

    #betas is also correct
    betas = {}

    betas[T] = [1, 1]

    for t in range(T-1, 0, -1):
        val0 = betas[t+1][0]*a[0][0]*normal(sigma[0], u[0], y[t+1]) + betas[t+1][1]*a[0][1]*normal(sigma[1], u[1], y[t+1])
        val1 = betas[t+1][0]*a[1][0]*normal(sigma[0], u[0], y[t+1]) + betas[t+1][1]*a[1][1]*normal(sigma[1], u[1], y[t+1])
        betas[t] = [ val0/(val0+val1), val1/(val0+val1) ]



    #print(betas)
    #gammas is also correct
    gammas = {}
    for t in range(1, T+1):
        val0 = ( alphas[t][0]*betas[t][0] ) / (alphas[t][0]*betas[t][0] + alphas[t][1]*betas[t][1])
        val1 = ( alphas[t][1]*betas[t][1] ) / (alphas[t][0]*betas[t][0] + alphas[t][1]*betas[t][1])
        gammas[t] = [ val0/(val0+val1), val1/(val0+val1) ]
    #print(gammas)
    #epsilons is correct
    epsilons = {}
    for t in range(1, T):
        val00 = ( alphas[t][0]*a[0][0]*betas[t+1][0]*normal(sigma[0], u[0], y[t+1]) )
        val01 = ( alphas[t][0]*a[0][1]*betas[t+1][1]*normal(sigma[1], u[1], y[t+1]) )
        val10 = ( alphas[t][1]*a[1][0]*betas[t+1][0]*normal(sigma[0], u[0], y[t+1]) )
        val11 = ( alphas[t][1]*a[1][1]*betas[t+1][1]*normal(sigma[1], u[1], y[t+1]) )
        tot_sum = val00+val11+val10+val01
        epsilons[t] = [[val00/tot_sum, val01/tot_sum], [val10/tot_sum, val11/tot_sum]]

    new_pis = [gammas[1][0] , gammas[1][1]]

    new_a = [[0,0],[0,0]]

    new_u = [0, 0]

    new_sigma = [0, 0]

    for i in range(2):
        for j in range(2):
            epsilon_sum = 0
            gamma_sum = 0
            for t in range(1,T):
                epsilon_sum += epsilons[t][i][j]
                gamma_sum += gammas[t][i]

            new_a[i][j] += epsilon_sum/gamma_sum

    for i in range(2):
        ytgamma_sum = 0
        gamma_sum = 0
        for t in range(1, T+1):
            ytgamma_sum += y[t]*gammas[t][i]
            gamma_sum += gammas[t][i]

        new_u[i] = ytgamma_sum/gamma_sum

    for i in range(2):
        ytuigammai_sum = 0
        gamma_sum = 0
        for t in range(1, T+1):
            ytuigammai_sum += ( (y[t]-u[i])**2 )* gammas[t][i]
            gamma_sum += gammas[t][i]
        new_sigma[i] = ( ytuigammai_sum / gamma_sum )**0.5

    pis = new_pis
    a = new_a
    u = new_u
    sigma = new_sigma
    # print(alphas)
    # print(betas)
    # print(gammas)
    # print(epsilons)


# print(a)
# print(pis)
# print(u)
# print(sigma)
# print(y)
# print(dp)
# print(a, pis, u, sigma)

for t in range(1, T+1):
    if u[1] > u[0]:
        if gammas[t][0] > 0.5:
            print("Bear")
        else:
            print("Bull")
    else:
        if gammas[t][0] > 0.5:
            print("Bull")
        else:
            print("Bear")

end = time.time()
#print(end - start)