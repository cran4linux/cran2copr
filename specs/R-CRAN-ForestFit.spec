%global packname  ForestFit
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}
Summary:          Statistical Modelling for Plant Size Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ars 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-ars 
Requires:         R-CRAN-pracma 

%description
Developed for the following tasks . I ) Computing the probability density
function , cumulative distribution function , random generation , and
estimating the parameters of the eleven mixture models . II ) Point
estimation of the parameters of two - parameter Weibull distribution using
twelve methods and three - parameter Weibull distribution using nine
methods . III ) The Bayesian estimators of the three - parameter Weibull
distribution . IV ) Estimating parameters of the three - parameter
Birnbaum - Saunders , generalized exponential , and Weibull distributions
fitted to grouped data using three methods including approximated maximum
likelihood , expectation maximization , and maximum likelihood . V )
Estimating the parameters of the gamma , log-normal , and Weibull mixture
models fitted to the grouped data through the EM algorithm , VI )
Estimating parameters of the nonlinear height curve fitted to the height -
diameter observation , VII ) Estimating parameters , computing probability
density function , cumulative distribution function , and generating
realizations from gamma shape mixture model introduced by Venturini et al.
(2008) <doi:10.1214/07-AOAS156> , and VIII ) Robust multiple linear
regression analysis when error term follows skewed t distribution .

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
