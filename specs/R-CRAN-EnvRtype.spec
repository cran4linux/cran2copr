%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EnvRtype
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Envirotyping for Quantitative Genetics and Plant Breeding

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
An enviromics toolkit for genotype-by-environment analysis and
envirotype-informed genomic prediction. Collects worldwide daily and
hourly weather from 'NASA POWER', soil profiles from 'SoilGrids',
elevation and bioclimatic layers from 'WorldClim', agro-ecological zones
from 'FAO GAEZ', and downscaled 'CMIP6' climate scenarios, with
checkpointed retrieval that can resume after an interrupted run. Derives
agro-meteorological parameters (solar radiation, evapotranspiration,
thermal time, atmospheric demand), runs a FAO-56 single crop coefficient
soil water balance, and maps daily weather onto crop developmental stages.
Builds environmental covariable matrices, envirotype typologies and
frequency matrices, mega-environment clusters, historical risk profiles
and target population of environments weights. Reduces interval-resolved
envirotypes by principal component analysis, delineates soil zones with
Gaussian mixture models, and constructs linear, Gaussian and arc-cosine
environmental relatedness kernels. Fits Bayesian reaction-norm kernel
models and predicts trained genotypes at untested locations and planting
dates, with coverage diagnostics, spatial mapping and planting-window
optimisation. Simulation functions generate multi-environment trials and
enviromes with known architecture for power analysis. Methods are
described in Costa-Neto, Galli, Carvalho, Crossa and Fritsche-Neto (2021)
<doi:10.1093/g3journal/jkab040>, and build on the Bayesian
genotype-by-environment kernel sampler of Granato, Cuevas, Luna-Vazquez,
Crossa, Montesinos-Lopez, Burgueno and Fritsche-Neto (2018)
<doi:10.1534/g3.118.200435>.

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
