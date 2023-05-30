%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  macroBiome
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Mapping the Distribution of the Biomes and Bioclimate

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-palinsol 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rworldxtra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-strex 
Requires:         R-CRAN-palinsol 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rworldxtra 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-strex 

%description
Procedures for simulating biomes by equilibrium vegetation models, with a
special focus on paleoenvironmental applications. Three widely used
equilibrium biome models are currently implemented in the package: the
Holdridge Life Zone (HLZ) system (Holdridge 1947,
<doi:10.1126/science.105.2727.367>), the Köppen-Geiger classification
(KGC) system (Köppen 1936,
<https://koeppen-geiger.vu-wien.ac.at/pdf/Koppen_1936.pdf>) and the BIOME
model (Prentice et al. 1992, <doi:10.2307/2845499>). Three climatic
forest-steppe models are also implemented. An approach for estimating
monthly time series of relative sunshine duration from temperature and
precipitation data (Yin 1999, <doi:10.1007/s007040050111>) is also
adapted, allowing process-based biome models to be combined with
high-resolution paleoclimate simulation datasets (e.g., CHELSA-TraCE21k
v1.0 dataset: <https://chelsa-climate.org/chelsa-trace21k/>).

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
