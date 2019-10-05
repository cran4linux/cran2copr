%global packname  MPS
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Estimating Through the Maximum Product Spacing Approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch

%description
Developed for computing the probability density function, computing the
cumulative distribution function, computing the quantile function, random
generation, drawing q-q plot, and estimating the parameters of 24 G-family
of statistical distributions via the maximum product spacing approach
introduced in <https://www.jstor.org/stable/2345411>. The set of families
contains: beta G distribution, beta exponential G distribution, beta
extended G distribution, exponentiated G distribution, exponentiated
exponential Poisson G distribution, exponentiated generalized G
distribution, exponentiated Kumaraswamy G distribution, gamma type I G
distribution, gamma type II G distribution, gamma uniform G distribution,
gamma-X generated of log-logistic family of G distribution, gamma-X family
of modified beta exponential G distribution, geometric exponential Poisson
G distribution, generalized beta G distribution, generalized transmuted G
distribution, Kumaraswamy G distribution, log gamma type I G distribution,
log gamma type II G distribution, Marshall Olkin G distribution, Marshall
Olkin Kumaraswamy G distribution, modified beta G distribution, odd
log-logistic G distribution, truncated-exponential skew-symmetric G
distribution, and Weibull G distribution.

%prep
%setup -q -c -n %{packname}


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
