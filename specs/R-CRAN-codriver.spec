%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  codriver
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Context-Aware AI Assistant for 'RStudio'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellmer >= 0.3.0
BuildRequires:    R-CRAN-rstudioapi >= 0.19.0
BuildRequires:    R-CRAN-rstudio.prefs >= 0.1.6
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ellmer >= 0.3.0
Requires:         R-CRAN-rstudioapi >= 0.19.0
Requires:         R-CRAN-rstudio.prefs >= 0.1.6
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 

%description
A context-aware AI assistant for 'RStudio' that works directly in the
source editor without switching context or opening a separate chat window.
Reads the cursor position and selection to automatically choose the right
action - generate, complete, continue, edit, or comment. Supports
configuration of multiple large language model providers and can be
invoked via the keyboard shortcut or Addins menu.

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
