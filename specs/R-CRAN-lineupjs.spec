%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lineupjs
%global packver   4.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          'HTMLWidget' Wrapper of 'LineUp' for Visual Analysis of Multi-Attribute Rankings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmlwidgets 

%description
'LineUp' is an interactive technique designed to create, visualize and
explore rankings of items based on a set of heterogeneous attributes. This
is a 'htmlwidget' wrapper around the JavaScript library 'LineUp.js'. It is
designed to be used in 'R Shiny' apps and 'R Markddown' files. Due to an
outdated 'webkit' version of 'RStudio' it won't work in the integrated
viewer.

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
