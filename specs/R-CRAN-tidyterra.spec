%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyterra
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          'tidyverse' Methods and 'ggplot2' Helpers for 'terra' Objects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-terra >= 1.8.10
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-terra >= 1.8.10
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
Extension of the 'tidyverse' for 'SpatRaster' and 'SpatVector' objects of
the 'terra' package. It includes also new 'geom_' functions that provide a
convenient way of visualizing 'terra' objects with 'ggplot2'.

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
