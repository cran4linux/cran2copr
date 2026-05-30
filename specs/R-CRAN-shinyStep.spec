%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyStep
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          User-Editable R Functions in 'Shiny' Apps with a Step Debugger

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-shinyAce >= 0.4.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-shinyAce >= 0.4.0

%description
A pair of 'Shiny' modules that let end users of a 'Shiny' application
author their own R functions directly in the browser. Host apps can expose
these modules as extension points where user-supplied code augments or
replaces built-in logic, without requiring users to modify the app's
source. Each module embeds an 'Ace' editor with a structured argument
table, an in-frame R console rooted in the paused function's local
environment, and a step debugger that handles for, while, repeat, and
if/else blocks at any nesting depth. Two module flavours are provided:
solo editors for testing a function in isolation with literal argument
values, and embedded editors for pausing a function mid-execution inside a
larger host program.

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
