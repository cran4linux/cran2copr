%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nestcolor
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Colors for NEST Graphs

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3

%description
Clinical reporting figures require to use consistent colors and
configurations. As a part of the Roche open-source clinical reporting
project, namely the NEST project, the 'nestcolor' package specifies the
color code and default theme with specifying 'ggplot2' theme parameters.
Users can easily customize color and theme settings before using the reset
of NEST packages to ensure consistent settings in both static and
interactive output at the downstream.

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
