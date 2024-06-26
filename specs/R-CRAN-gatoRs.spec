%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gatoRs
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Geographic and Taxonomic Occurrence R-Based Scrubbing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CoordinateCleaner >= 3.0.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-ridigbio 
BuildRequires:    R-CRAN-rgbif 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-spThin 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-CoordinateCleaner >= 3.0.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ridigbio 
Requires:         R-CRAN-rgbif 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-spThin 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-spatstat.geom 

%description
Streamlines downloading and cleaning biodiversity data from Integrated
Digitized Biocollections (iDigBio) and the Global Biodiversity Information
Facility (GBIF).

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
