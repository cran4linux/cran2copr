%global packname  interflex
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multiplicative Interaction Models Diagnostics and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-lfe >= 2.6.2291
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-mgcv >= 1.8.16
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-Lmoments >= 1.2.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-pcse 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ModelMetrics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lfe >= 2.6.2291
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-mgcv >= 1.8.16
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-Lmoments >= 1.2.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-pcse 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ModelMetrics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-future 

%description
Performs diagnostic tests of multiplicative interaction models and plots
non-linear marginal effects of a treatment on an outcome across different
values of a moderator.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
