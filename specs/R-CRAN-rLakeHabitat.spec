%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rLakeHabitat
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolate Bathymetry and Quantify Physical Aquatic Habitat

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-CRAN-tidyterra 
BuildRequires:    R-CRAN-rLakeAnalyzer 
BuildRequires:    R-CRAN-isoband 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gganimate 
Requires:         R-CRAN-tidyterra 
Requires:         R-CRAN-rLakeAnalyzer 
Requires:         R-CRAN-isoband 

%description
Offers bathymetric interpolation using Inverse Distance Weighted and
Ordinary Kriging via the 'gstat' and 'terra' packages. Other functions
focus on quantifying physical aquatic habitats (e.g., littoral,
epliminion, metalimnion, hypolimnion) from interpolated digital elevation
models (DEMs). Functions were designed to calculate these metrics across
water levels for use in reservoirs but can be applied to any DEM and will
provide values for fixed conditions. Parameters like Secchi disk depth or
estimated photic zone, thermocline depth, and water level fluctuation
depth are included in most functions.

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
