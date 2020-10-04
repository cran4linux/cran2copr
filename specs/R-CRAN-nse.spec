%global packname  nse
%global packver   1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.19
Release:          3%{?dist}%{?buildtag}
Summary:          Numerical Standard Errors Computation in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-mcmc 
BuildRequires:    R-CRAN-mcmcse 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-mcmc 
Requires:         R-CRAN-mcmcse 
Requires:         R-CRAN-np 
Requires:         R-CRAN-sandwich 

%description
Collection of functions designed to calculate numerical standard error
(NSE) of univariate time series as described in Ardia et al. (2018)
<doi:10.2139/ssrn.2741587> and Ardia and Bluteau (2017)
<doi:10.21105/joss.00172>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
