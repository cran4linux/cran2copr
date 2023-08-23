%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdwplus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of IDW-PLUS

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgrass 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rgrass 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stringr 

%description
Compute spatially explicit land-use metrics for stream survey sites in
GRASS GIS and R as an open-source implementation of IDW-PLUS (Inverse
Distance Weighted Percent Land Use for Streams). The package includes
functions for preprocessing digital elevation and streams data, and one
function to compute all the spatially explicit land use metrics described
in Peterson et al. (2011) <doi:10.1111/j.1365-2427.2010.02507.x> and
previously implemented by Peterson and Pearse (2017)
<doi:10.1111/1752-1688.12558> in ArcGIS-Python as IDW-PLUS.

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
