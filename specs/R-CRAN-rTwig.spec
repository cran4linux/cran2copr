%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rTwig
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Realistic Quantitative Structure Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.6.3
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-tidytable 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-colourvalues 
BuildRequires:    R-CRAN-Morpho 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-kit 
BuildRequires:    R-CRAN-rmatio 
BuildRequires:    R-CRAN-randomcoloR 
Requires:         R-CRAN-Matrix >= 1.6.3
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-tidytable 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cobs 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-colourvalues 
Requires:         R-CRAN-Morpho 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-kit 
Requires:         R-CRAN-rmatio 
Requires:         R-CRAN-randomcoloR 

%description
Real Twig is a method to correct branch overestimation in quantitative
structure models. Overestimated cylinders are correctly tapered using
measured twig diameters of corresponding tree species. Supported
quantitative structure modeling software includes 'TreeQSM' and
'SimpleForest'. Also included is a novel database of twig diameters and
tools for fractal analysis of point clouds.

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
