%global __brp_check_rpaths %{nil}
%global packname  FORTLS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Processing of TLS Point Cloud Data for Forestry Purposes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-Distance 
BuildRequires:    R-CRAN-ggvoronoi 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-Distance 
Requires:         R-CRAN-ggvoronoi 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vroom 

%description
Process automation of Terrestrial Laser Scanner (TLS) point cloud data
derived from single scans. 'FORTLS' enables (i) detection of trees and
estimation of diameter at breast height (dbh), (ii) estimation of some
stand variables (e.g. density, basal area, mean and dominant height),
(iii) computation of metrics related to important forest attributes
estimated in Forest Inventories (FIs) at stand level and (iv) optimization
of plot design for combining TLS data and field measured data.
Documentation about 'FORTLS' is described in Molina-Valero et al. (2020,
<doi:10.3390/IECF2020-08066>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
