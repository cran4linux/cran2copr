%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  proximetricsR
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Spectral Preprocessing and Chemometric Calibration of NIR Sensors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-plotly >= 4.0
BuildRequires:    R-CRAN-mathjaxr >= 1.0
BuildRequires:    R-CRAN-digest >= 0.6
BuildRequires:    R-CRAN-prospectr >= 0.2.10
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plotly >= 4.0
Requires:         R-CRAN-mathjaxr >= 1.0
Requires:         R-CRAN-digest >= 0.6
Requires:         R-CRAN-prospectr >= 0.2.10
Requires:         R-CRAN-callr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-Rcpp 

%description
Provides tools to build quantitative chemometric models and applications
for near-infrared (NIR) sensors. Chemometric regression models are based
on partial least squares regression as described by Wold (1975)
<doi:10.1016/B978-0-12-103950-9.50017-4> and modified partial least
squares regression as described by Shenk and Westerhaus (1991)
<doi:10.2135/cropsci1991.0011183X003100020049x>, with further discussion
by Westerhaus (2014) <doi:10.1255/nirn.1492>.

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
