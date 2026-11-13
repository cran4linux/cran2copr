%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mascot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Live Mood-Driven Mascots for 'Shiny' Apps and 'Quarto' Sites

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-htmltools >= 0.5.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-htmltools >= 0.5.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 

%description
Adds a character drawn in code to 'Shiny' apps and 'Quarto' sites. The
character shows a mood with status text beside it and animates when the
mood changes; a 'Shiny' server can change its mood, status, speech bubble
and gestures, and a click can run an action or open a menu. It follows
light and dark mode and takes its colours from built-in palettes or custom
colours. Custom characters can be described in 'JSON' and checked before
use, and an interactive app demonstrates every function.

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
