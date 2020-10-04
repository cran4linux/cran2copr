%global packname  vsgoftest
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests Based on Kullback-Leibler Divergence

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fitdistrplus 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-stats 
Requires:         R-CRAN-fitdistrplus 

%description
An implementation of Vasicek and Song goodness-of-fit tests. Several
functions are provided to estimate differential Shannon entropy, i.e.,
estimate Shannon entropy of real random variables with density, and test
the goodness-of-fit of some family of distributions, including uniform,
Gaussian, log-normal, exponential, gamma, Weibull, Pareto, Fisher, Laplace
and beta distributions; see Lequesne and Regnault (2018)
<arXiv:1806.07244>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
