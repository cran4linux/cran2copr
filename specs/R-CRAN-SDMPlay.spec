%global __brp_check_rpaths %{nil}
%global packname  SDMPlay
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Modelling Playground

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-dismo 
BuildRequires:    R-stats 
BuildRequires:    R-base 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-dismo 
Requires:         R-stats 
Requires:         R-base 

%description
Species distribution modelling (SDM) has been developed for several years
to address conservation issues, assess the direct impact of human
activities on ecosystems and predict the potential distribution shifts of
invasive species (see Elith et al. 2006, Pearson 2007, Elith and Leathwick
2009). SDM relates species occurrences with environmental information and
can predict species distribution on their entire occupied space. This
approach has been increasingly applied to Southern Ocean case studies, but
requires corrections in such a context, due to the broad scale area, the
limited number of presence records available and the spatial and temporal
aggregations of these datasets. SDMPlay is a pedagogic package that will
allow you to compute SDMs, to understand the overall method, and to
produce model outputs. The package, along with its associated vignettes,
highlights the different steps of model calibration and describes how to
choose the best methods to generate accurate and relevant outputs. SDMPlay
proposes codes to apply a popular machine learning approach, BRT (Boosted
Regression Trees) and introduces MaxEnt (Maximum Entropy). It contains
occurrences of marine species and environmental descriptors datasets as
examples associated to several vignette tutorials available at
<https://github.com/charleneguillaumot/THESIS/tree/master/SDMPLAY_R_PACKAGE>.

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
