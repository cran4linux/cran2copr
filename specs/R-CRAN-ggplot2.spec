%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggplot2
%global packver   3.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Elegant Data Visualisations Using the Grammar of Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-gtable >= 0.1.1
BuildRequires:    R-CRAN-lifecycle > 1.0.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-isoband 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-gtable >= 0.1.1
Requires:         R-CRAN-lifecycle > 1.0.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-isoband 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
A system for 'declaratively' creating graphics, based on "The Grammar of
Graphics". You provide the data, tell 'ggplot2' how to map variables to
aesthetics, what graphical primitives to use, and it takes care of the
details.

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
