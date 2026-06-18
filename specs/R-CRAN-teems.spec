%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  teems
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Trade and Environment Equilibrium Modeling System

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-cli >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-cli >= 3.4.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Equilibrium models are frequently employed to examine the potential
impacts of economic, energy, and trade policies as well as form the
foundation of most integrated assessment models. The 'teems' package
handles all aspects of running equilibrium models while facilitating
transparent and reproducible workflows.

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
