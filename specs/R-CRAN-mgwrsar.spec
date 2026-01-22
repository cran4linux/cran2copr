%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mgwrsar
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          GWR, Mixed GWR with Spatial Autocorrelation and Multiscale GWR (Top-Down Scale Approaches)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SMUT 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SMUT 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lifecycle 

%description
Provides methods for Geographically Weighted Regression with spatial
autocorrelation (Geniaux and Martinetti 2017)
<doi:10.1016/j.regsciurbeco.2017.04.001>. Implements Multiscale
Geographically Weighted Regression with Top-Down Scale approaches (Geniaux
2026) <doi:10.1007/s10109-025-00481-4>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
