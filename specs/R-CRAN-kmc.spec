%global packname  kmc
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          2%{?dist}
Summary:          Kaplan-Meier Estimator with Constraints for Right Censored Data-- a Recursive Computational Algorithm

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.1
Requires:         R-core >= 2.13.1
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-emplik 

%description
Given constraints for right censored data, we use a recursive
computational algorithm to calculate the the "constrained" Kaplan-Meier
estimator. The constraint is assumed given in linear estimating equations
or mean functions. We also illustrate how this leads to the empirical
likelihood ratio test with right censored data and accelerated failure
time model with given coefficients. EM algorithm from emplik package is
used to get the initial value. The properties and performance of the EM
algorithm is discussed in Mai Zhou and Yifan Yang (2015)<doi:
10.1007/s00180-015-0567-9> and Mai Zhou and Yifan Yang (2017)
<10.1002/wics.1400>. More applications could be found in Mai Zhou (2015)
<doi: 10.1201/b18598>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
