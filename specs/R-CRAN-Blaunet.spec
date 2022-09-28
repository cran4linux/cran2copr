%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Blaunet
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Analyze Blau Statuses for Measuring Social Distance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plot3Drgl 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-foreign 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plot3Drgl 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-foreign 

%description
Calculate and analyze Blau statuses for quantifying social distance
between individuals belonging to organizations. Relational (network) data
can be incorporated for additional analyses. This project is supported by
Defense Threat Reduction Agency (DTRA) Grant HDTRA-10-1-0043.

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
