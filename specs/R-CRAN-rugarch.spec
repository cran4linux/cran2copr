%global packname  rugarch
%global packver   1.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          2%{?dist}
Summary:          Univariate GARCH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.34
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-spd 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-SkewHyperbolic 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-spd 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-SkewHyperbolic 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-utils 

%description
ARFIMA, in-mean, external regressors and various GARCH flavors, with
methods for fit, forecast, simulation, inference and plotting.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rugarch.tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
