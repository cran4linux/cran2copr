%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eplusr
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Using Whole Building Simulation Program 'EnergyPlus'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.2.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-callr >= 2.0.4
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-processx >= 3.2.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-callr >= 2.0.4
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-units 

%description
A rich toolkit of using the whole building simulation program
'EnergyPlus'(<https://energyplus.net>), which enables programmatic
navigation, modification of 'EnergyPlus' models and makes it less painful
to do parametric simulations and analysis.

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
