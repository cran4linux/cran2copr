%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nflplotR
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          NFL Logo Plots in 'ggplot2' and 'gt'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-magick >= 2.7.3
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-nflreadr >= 1.3.2
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-backports >= 1.1.6
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-ggpath >= 1.0.1
BuildRequires:    R-CRAN-cachem >= 1.0.0
BuildRequires:    R-CRAN-gt >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-magick >= 2.7.3
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-nflreadr >= 1.3.2
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-backports >= 1.1.6
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-ggpath >= 1.0.1
Requires:         R-CRAN-cachem >= 1.0.0
Requires:         R-CRAN-gt >= 0.8.0
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-grid 
Requires:         R-CRAN-lifecycle 

%description
A set of functions to visualize National Football League analysis in
'ggplot2' plots and 'gt' tables.

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
