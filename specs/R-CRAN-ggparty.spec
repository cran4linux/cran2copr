%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggparty
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot' Visualizations for the 'partykit' Package

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partykit 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rlang 

%description
Extends 'ggplot2' functionality to the 'partykit' package. 'ggparty'
provides the necessary tools to create clearly structured and highly
customizable visualizations for tree-objects of the class 'party'.

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
