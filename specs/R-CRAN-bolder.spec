%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bolder
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Add-Ins for Formatted Section Titles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-rstudioapi 

%description
Provides 'RStudio' add-ins and helper functions for converting the current
editor line, or a supplied character string, into formatted section titles
for 'R' scripts. When used as an add-in, it uses 'rstudioapi' to read the
active document context and replace only the selected line, so users can
bind the add-ins to keyboard shortcuts. The formatter trims common comment
and heading markers, converts the label to uppercase, and renders three
styles: a five-line boxed title, a framed subtitle, and a simple inline
header. Generated titles are padded or centered to a configurable width,
using the package-specific width option when set and the session display
width otherwise, which helps keep analysis scripts visually consistent and
easier to navigate.

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
