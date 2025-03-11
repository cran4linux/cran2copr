%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brandr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Brand Identity Management Using brand.yml Standard

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-grDevices >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-checkmate >= 2.3.2
BuildRequires:    R-CRAN-yaml >= 2.3.10
BuildRequires:    R-CRAN-colorspace >= 2.1.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-here >= 1.0.1
Requires:         R-grDevices >= 4.3.0
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-checkmate >= 2.3.2
Requires:         R-CRAN-yaml >= 2.3.10
Requires:         R-CRAN-colorspace >= 2.1.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-here >= 1.0.1

%description
A system to facilitate brand identity management using the brand.yml
standard, providing functions to consistently access and apply brand
colors, typography, and other visual elements across your R projects.

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
