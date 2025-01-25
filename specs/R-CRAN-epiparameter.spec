%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  epiparameter
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Classes and Helper Functions for Working with Epidemiological Parameters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cachem 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-distcrete 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-epiparameterDB 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cachem 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-distcrete 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-epiparameterDB 
Requires:         R-graphics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Classes and helper functions for loading, extracting, converting,
manipulating, plotting and aggregating epidemiological parameters for
infectious diseases. Epidemiological parameters extracted from the
literature are loaded from the 'epiparameterDB' R package.

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
