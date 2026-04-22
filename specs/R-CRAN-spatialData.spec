%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatialData
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Datasets for Ecological Modeling

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
Provides spatial datasets ready to use for ecological modelling and raster
companion data for prediction: Neanderthal presence during the Last
Interglacial (Benito et al. 2017 <doi:10.1111/jbi.12845>); Plant diversity
metrics for the World's Ecoregions (Maestre et al. 2021
<doi:10.1111/nph.17398>); tree richness across the Americas (Benito et al.
2013 <doi:10.1111/2041-210X.12022>); plant communities from the Sierra
Nevada (Spain) with future climate scenarios (Benito et al. 2013
<doi:10.1111/2041-210X.12022>); butterfly-plant interaction data from
Sierra Nevada (Spain) (Benito et al. 2011
<doi:10.1007/s10584-010-0015-3>); plant species occurrences in Andalusia
(Spain) (Benito et al. 2014 <doi:10.1111/ddi.12148>); presence of the
plant Linaria nigricans and greenhouses (Benito et al. 2009
<doi:10.1007/s10531-009-9604-8>); global NDVI and environmental
predictors, and European oak species occurrences. All datasets include
pre-processed environmental predictors ready for statistical modelling.

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
