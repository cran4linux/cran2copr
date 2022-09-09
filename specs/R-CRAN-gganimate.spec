%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gganimate
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          A Grammar of Animated Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tweenr >= 1.0.1
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tweenr >= 1.0.1
Requires:         R-CRAN-stringi 
Requires:         R-grid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-scales 
Requires:         R-grDevices 
Requires:         R-utils 

%description
The grammar of graphics as implemented in the 'ggplot2' package has been
successful in providing a powerful API for creating static visualisation.
In order to extend the API for animated graphics this package provides a
completely new set of grammar, fully compatible with 'ggplot2' for
specifying transitions and animations in a flexible and extensible way.

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
