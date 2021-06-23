%global __brp_check_rpaths %{nil}
%global packname  partialAR
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          3%{?dist}%{?buildtag}
Summary:          Partial Autoregression

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-zoo 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-plot3D 
Requires:         R-methods 

%description
A time series is said to be partially autoregressive if it can be
represented as a sum of a random walk and an autoregressive sequence
without unit roots. This package fits partially autoregressive time
series, where the autoregressive component is AR(1).  This may be of use
in modeling certain financial time series.

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
