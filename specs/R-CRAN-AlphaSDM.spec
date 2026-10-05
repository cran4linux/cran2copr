%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AlphaSDM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Models on 'AlphaEarth' Satellite Embeddings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.41
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.41
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-utils 

%description
Fits species distribution models and maps habitat suitability at up to 10
m resolution from occurrence records alone, using the 'AlphaEarth'
Foundations satellite embeddings (Brown et al. 2025)
<doi:10.48550/arXiv.2507.22291>. The embeddings, 64 values per pixel per
year from a geospatial foundation model, replace environmental layers, so
none need to be sourced or aligned. Provides tools to format occurrence
records, place pseudo-absences, train and evaluate an ensemble of machine
learning models, and export habitat-suitability rasters. Sampling, model
training and prediction all run on 'Google Earth Engine', which requires a
free account for noncommercial use.

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
