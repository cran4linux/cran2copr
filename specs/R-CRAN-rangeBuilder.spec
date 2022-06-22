%global __brp_check_rpaths %{nil}
%global packname  rangeBuilder
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Occurrence Filtering, Geographic and Taxonomic Standardization and Generation of Species Range Polygons

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-alphahull >= 2.5
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-rgeos >= 0.1.4
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-cleangeo 
BuildRequires:    R-methods 
Requires:         R-CRAN-alphahull >= 2.5
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-rgeos >= 0.1.4
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-cleangeo 
Requires:         R-methods 

%description
Provides tools for filtering occurrence records, generating
alpha-hull-derived range polygons and mapping species distributions.

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
