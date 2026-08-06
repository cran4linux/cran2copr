%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StressCensoR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Stress-Strength Reliability Estimation Under Censoring Schemes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Generalized framework for data generation, Maximum Likelihood Estimation,
and Bayesian estimation of stress-strength reliability R = P(Y < X) for
arbitrary continuous distributions under censoring schemes based on
Chapter 9 of 'Balakrishnan', 'Cramer', and 'Kundu' (2023)
<ISBN:978-0-12-398387-9>. Users provide probability density functions,
cumulative distribution functions, survival functions, support bounds,
parameter ranges, and sample sizes. Implements data generation under
Type-I, Type-II, progressive Type-II, Type-I hybrid, Type-II hybrid,
generalized hybrid, progressive hybrid, joint, block random, middle, and
truncation censoring schemes, accompanied by diagnostic histograms, dot
plots, and autocorrelation plots. Maximum Likelihood Estimation supports
optimization routines including 'Newton-Raphson',
'Broyden'-'Fletcher'-'Goldfarb'-'Shanno' ('BFGS'), 'BFGS' in R ('BFGSR'),
'Berndt'-'Hall'-'Hall'-'Hausman' ('BHHH'), Simulated Annealing ('SANN'),
Conjugate Gradients ('CG'), and 'Nelder'-'Mead' ('NM'), returning
summaries ('AIC', 'coef', 'logLik', 'nIter', 'stdEr', summary, 'vcov').
Bayesian estimation of stress-strength reliability R = P(Y < X) is
performed via Gibbs sampling, Metropolis-Hastings algorithm, Importance
Sampling, and 'Lindley' approximation (1980). Methods and censoring
schemes are described in 'Balakrishnan', 'Cramer', and 'Kundu' (2023,
ISBN:978-0-12-398387-9), 'Lindley' (1980)
<doi:10.1111/j.2517-6161.1980.tb01102.x>, 'Geweke' (1989)
<doi:10.2307/2290062>, 'Metropolis' (1953) <doi:10.1063/1.1699114>,
'Hastings' (1970) <doi:10.1093/biomet/57.1.97>, 'Geman' and 'Geman' (1984)
<doi:10.1109/TPAMI.1984.4767596>, 'Kundu' and 'Gupta' (2005)
<doi:10.1016/j.jspi.2004.09.006>, 'Kundu' and 'Gupta' (2006)
<doi:10.1016/j.csda.2005.02.007>, 'Berndt', 'Hall', 'Hall', and 'Hausman'
(1974) <doi:10.3386/t0003>, 'Fletcher' (1987, ISBN:978-0-471-91547-8), and
'Nelder' and 'Mead' (1965) <doi:10.1093/comjnl/7.4.308>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
