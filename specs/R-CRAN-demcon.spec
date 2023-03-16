%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  demcon
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interfacing with Popular Polity, Institutional, and Constitutional Datasets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-countrycode 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-countrycode 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
An open-source toolkit developed by ISciences, LLC and the DANTE Project
that is intended for learning, accessing, pre-processing, and visualizing
popular political, institutional, and constitutional datasets. ‘demcon'
aims to reduce barriers to entry in political science research by
automating common acquisition and pre-processing procedures. This package
particularly focuses on the V-Dem dataset
(<https://www.v-dem.net/vdemds.html>), and provides adaptations of methods
presented in Fjelde, H., Knutsen, C. H. & Nygård, H. M. 2021,
<doi:10.1093/isq/sqaa076>.

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
