%global packname  bvartools
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Bayesian Inference of Vector Autoregressive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-coda 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-stats 

%description
Assists in the set-up of algorithms for Bayesian inference of vector
autoregressive (VAR) models. Functions for posterior simulation,
forecasting, impulse response analysis and forecast error variance
decomposition are largely based on the introductory texts of Koop and
Korobilis (2010) <doi:10.1561/0800000013> and Luetkepohl (2007, ISBN:
9783540262398).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
