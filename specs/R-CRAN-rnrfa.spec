%global packname  rnrfa
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          UK National River Flow Archive Data from R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-parallel 
Requires:         R-CRAN-tibble 

%description
Utility functions to retrieve data from the UK National River Flow Archive
(<https://nrfa.ceh.ac.uk/>, terms and conditions:
<https://nrfa.ceh.ac.uk/costs-terms-and-conditions>). The package contains
R wrappers to the UK NRFA data temporary-API. There are functions to
retrieve stations falling in a bounding box, to generate a map and
extracting time series and general information. The package is fully
described in Vitolo et al (2016) "rnrfa: An R package to Retrieve, Filter
and Visualize Data from the UK National River Flow Archive"
<https://journal.r-project.org/archive/2016/RJ-2016-036/RJ-2016-036.pdf>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
