%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  streetscape
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Collect And Investigate Street Views For Urban Science

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-quickPWCR 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-SuperpixelImageSegmentation 
BuildRequires:    R-CRAN-OpenImageR 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-parallelly 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-quickPWCR 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-SuperpixelImageSegmentation 
Requires:         R-CRAN-OpenImageR 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-parallelly 

%description
A collection of functions to search and download street view imagery
('Mapilary' <https://www.mapillary.com/developer/api-documentation>) and
to extract, quantify, and visualize visual features. Moreover, there are
functions provided to generate Qualtrics survey in TXT format using the
collection of street views for various research purposes.

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
