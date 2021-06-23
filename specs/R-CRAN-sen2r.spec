%global __brp_check_rpaths %{nil}
%global packname  sen2r
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Find, Download and Process Sentinel-2 Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.9.2
BuildRequires:    R-CRAN-stars >= 0.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-geojsonio 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RcppTOML 
Requires:         R-CRAN-sf >= 0.9.2
Requires:         R-CRAN-stars >= 0.4.1
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-geojsonio 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RcppTOML 

%description
Functions to download Sentinel-2 optical images and perform preliminary
processing operations. 'sen2r' provides the instruments required to easily
perform (and eventually automate) the steps necessary to build a complete
Sentinel-2 processing chain. A Graphical User Interface to facilitate data
processing is also provided. For additional documentation refer to the
following article: Ranghetti et al. (2020)
<doi:10.1016/j.cageo.2020.104473>.

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
