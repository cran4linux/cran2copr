%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  probably
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Post-Processing Predicted Values

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-yardstick >= 1.3.0
BuildRequires:    R-CRAN-workflows >= 1.1.4
BuildRequires:    R-CRAN-tidyselect >= 1.1.2
BuildRequires:    R-CRAN-tune >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-vctrs >= 0.4.1
BuildRequires:    R-CRAN-generics >= 0.1.3
BuildRequires:    R-CRAN-butcher 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-yardstick >= 1.3.0
Requires:         R-CRAN-workflows >= 1.1.4
Requires:         R-CRAN-tidyselect >= 1.1.2
Requires:         R-CRAN-tune >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-generics >= 0.1.3
Requires:         R-CRAN-butcher 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-withr 

%description
Models can be improved by post-processing class probabilities, by:
recalibration, conversion to hard probabilities, assessment of equivocal
zones, and other activities. 'probably' contains tools for conducting
these operations as well as calibration tools and conformal inference
techniques for regression models.

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
