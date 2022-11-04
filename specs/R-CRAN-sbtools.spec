%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sbtools
%global packver   1.1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          USGS ScienceBase Tools

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-keyring 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-methods 
Requires:         R-CRAN-mime 
Requires:         R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-keyring 

%description
Tools for interacting with U.S. Geological Survey ScienceBase
<https://www.sciencebase.gov> interfaces. ScienceBase is a data cataloging
and collaborative data management platform. Functions included for
querying ScienceBase, and creating and fetching datasets.

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
