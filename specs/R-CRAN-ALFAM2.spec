%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ALFAM2
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Model of Ammonia Emission from Field-Applied Manure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-stats 

%description
An implementation of the ALFAM2 dynamic emission model for ammonia
volatilization from field-applied animal slurry (manure with dry matter
below about 15%%). The model can be used to predict cumulative emission and
emission rate of ammonia following field application of slurry.
Predictions may be useful for emission inventory calculations, fertilizer
management, assessment of mitigation strategies, or research aimed at
understanding ammonia emission. Default parameter sets include effects of
application method, slurry composition, and weather. The model structure
is based on a simplified representation of the physical-chemical
slurry-soil-atmosphere system. See Hafner et al. (2018)
<doi:10.1016/j.atmosenv.2018.11.034> for information on the model and
Hafner et al. (2019) <doi:10.1016/j.agrformet.2017.11.027> for more on the
measurement data used for parameter development.

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
