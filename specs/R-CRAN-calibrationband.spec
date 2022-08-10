%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  calibrationband
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calibration Bands

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Package to assess the calibration of probabilistic classifiers using
confidence bands for monotonic functions. Besides testing the classical
goodness-of-fit null hypothesis of perfect calibration, the confidence
bands calculated within that package facilitate inverted goodness-of-fit
tests whose rejection allows for a sought-after conclusion of a
sufficiently well-calibrated model. The package creates flexible graphical
tools to perform these tests.  For construction details see also
Dimitriadis, Dümbgen, Henzi, Puke, Ziegel (2022) <arXiv:2203.04065>.

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
