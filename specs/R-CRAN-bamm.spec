%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bamm
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Models as a Function of Biotic, Abiotic and Movement Factors (BAM)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-raster >= 3.4.13
BuildRequires:    R-methods >= 3.3
BuildRequires:    R-CRAN-animation >= 2.3
BuildRequires:    R-CRAN-leaflet >= 2.0
BuildRequires:    R-CRAN-sp >= 1.3.0
BuildRequires:    R-CRAN-Matrix >= 1.2.14
BuildRequires:    R-CRAN-magrittr >= 1.2
BuildRequires:    R-CRAN-igraph >= 1.2
BuildRequires:    R-CRAN-future >= 1.18.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-purrr >= 0.2
BuildRequires:    R-CRAN-RSpectra >= 0.13.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-Rdpack >= 0.11
BuildRequires:    R-CRAN-furrr >= 0.1.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-raster >= 3.4.13
Requires:         R-methods >= 3.3
Requires:         R-CRAN-animation >= 2.3
Requires:         R-CRAN-leaflet >= 2.0
Requires:         R-CRAN-sp >= 1.3.0
Requires:         R-CRAN-Matrix >= 1.2.14
Requires:         R-CRAN-magrittr >= 1.2
Requires:         R-CRAN-igraph >= 1.2
Requires:         R-CRAN-future >= 1.18.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-purrr >= 0.2
Requires:         R-CRAN-RSpectra >= 0.13.1
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-Rdpack >= 0.11
Requires:         R-CRAN-furrr >= 0.1.0

%description
Species Distribution Modeling (SDM) is a practical methodology that aims
to estimate the area of distribution of a species. However, most of the
work has focused on estimating static expressions of the correlation
between environmental variables. The outputs of correlative species
distribution models can be interpreted as maps of the suitable environment
for a species but not generally as maps of its actual distribution.
Soberón and Peterson (2005) <doi:10.17161/bi.v2i0.4> presented the BAM
scheme, a heuristic framework that states that the occupied area of a
species occurs on sites that have been accessible through dispersal (M)
and have both favorable biotic (B) and abiotic conditions (A). The 'bamm'
package implements classes and functions to operate on each element of the
BAM and by using a cellular automata model where the occupied area of a
species at time t is estimated by the multiplication of three binary
matrices: one matrix represents movements (M), another abiotic -niche-
tolerances (A), and a third, biotic interactions (B). The theoretical
background of the package can be found in Soberón and Osorio-Olvera (2022)
<arXiv:2212.06308>.

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
