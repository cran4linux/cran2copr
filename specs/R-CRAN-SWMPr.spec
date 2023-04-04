%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SWMPr
%global packver   2.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieving, Organizing, and Analyzing Estuary Monitoring Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-oce 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-oce 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-XML 

%description
Tools for retrieving, organizing, and analyzing environmental data from
the System Wide Monitoring Program of the National Estuarine Research
Reserve System <https://cdmo.baruch.sc.edu/>. These tools address common
challenges associated with continuous time series data for environmental
decision making.

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
