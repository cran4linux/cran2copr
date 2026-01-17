%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jtools
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Presentation of Social Scientific Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-pkgconfig 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-tibble 

%description
This is a collection of tools for more efficiently understanding and
sharing the results of (primarily) regression analyses. There are also a
number of miscellaneous functions for statistical and programming
purposes. Support for models produced by the survey and lme4 packages are
points of emphasis.

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
