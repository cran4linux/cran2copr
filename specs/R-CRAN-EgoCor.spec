%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EgoCor
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Presentation of Estimated Exponential Semi-Variograms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-SpatialTools 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-SpatialTools 
Requires:         R-stats 

%description
User friendly interface based on the R package 'gstat' to fit exponential
parametric models to empirical semi-variograms in order to model the
spatial correlation structure of health data. Geo-located health outcomes
of survey participants may be used to model spatial effects on health in
an ego-centred approach.  The package contains a range of functions to
help explore the spatial structure of the data as well as visualize the
fit of exponential models for various metaparameter combinations with
respect to the number of lag intervals and maximal distance.  Furthermore,
the outcome of interest can be adjusted for covariates by fitting a linear
regression in a preliminary step before the semi-variogram fitting
process.

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
