%global __brp_check_rpaths %{nil}
%global packname  qqconf
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Creates Simultaneous Testing Bands for QQ-Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-MASS >= 7.3.50
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-robustbase >= 0.93.4
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MASS >= 7.3.50
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-robustbase >= 0.93.4
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-Rcpp 

%description
Provides functionality for creating Quantile-Quantile (QQ) and
Probability-Probability (PP) plots with simultaneous testing bands to
asses significance of sample deviation from a reference distribution.

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
