%global packname  ecd
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}
Summary:          Elliptic Lambda Distribution and Option Pricing Model

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmpfr >= 0.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-RcppFaddeeva 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-Rmpfr >= 0.6.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-RcppFaddeeva 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-stabledist 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-digest 

%description
Elliptic lambda distribution and lambda option pricing model have been
evolved into a framework of stable-law inspired distributions, such as the
extended stable lambda distribution for asset return, stable count
distribution for volatility, and Lihn-Laplace process as a leptokurtic
extension of Wiener process. This package contains functions for the
computation of density, probability, quantile, random variable, fitting
procedures, option prices, volatility smile. It also comes with sample
financial data, and plotting routines.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
