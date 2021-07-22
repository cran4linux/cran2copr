%global __brp_check_rpaths %{nil}
%global packname  rTG
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Methods to Analyse Seasonal Radial Tree Growth Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-mgcv >= 1.8.34
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-knitr >= 1.19
BuildRequires:    R-CRAN-brnn >= 0.6
BuildRequires:    R-CRAN-dplyr >= 0.1.0
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-mgcv >= 1.8.34
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-knitr >= 1.19
Requires:         R-CRAN-brnn >= 0.6
Requires:         R-CRAN-dplyr >= 0.1.0

%description
Methods for comparing different regression algorithms for describing the
temporal dynamics of secondary tree growth (xylem and phloem). Users can
compare the accuracy of the most common fitting methods usually used to
analyse xylem and phloem data, i.e., Gompertz function and General
Additive Models (GAMs); and an algorithm newly introduced to the field,
i.e., Bayesian Regularised Neural Networks (brnn). The core function of
the package is XPSgrowth(), while the results can be interpreted using
implemented generic S3 methods, such as plot() and summary().

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
