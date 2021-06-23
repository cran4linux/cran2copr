%global __brp_check_rpaths %{nil}
%global packname  Rdca
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          DCA Tools for Decline Rate Analysis and EUR Forecast

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Arps Decline Curve Analysis (DCA) models for production rate, cumulative
production, nominal decline rate, the derivative of loss-ratio, and
estimated ultimate recovery (EUR) predictions for oil and gas wells. Arps,
J. J. (1945) <doi:10.2118/945228-G>. Robertson, S. (1988)
<https://www.onepetro.org/general/SPE-18731-MS>.

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
