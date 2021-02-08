%global packname  osmgeosample
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Construction of Geostatistical Sampling Designs with OSM Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mapview 
BuildRequires:    R-CRAN-nngeo 
BuildRequires:    R-CRAN-osmdata 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geoR 
Requires:         R-graphics 
Requires:         R-CRAN-mapview 
Requires:         R-CRAN-nngeo 
Requires:         R-CRAN-osmdata 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 
Requires:         R-stats 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sf 
Requires:         R-methods 

%description
The utilisation of the functionality provided by the 'OSMData' and
'geosample' to allow users to create spatially continuous or discrete
random samples from a pre-defined spatial border using OSM data.
Reference: Joao Porto de Albuquerque, Godwin Yeboah, Vangelis Pitidis,
Philipp Ulbrich (2019) <doi:10.13140/RG.2.2.13710.20804>.

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
