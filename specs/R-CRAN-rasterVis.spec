%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rasterVis
%global packver   0.51.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.51.6
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization Methods for Raster Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 3.4.13
BuildRequires:    R-CRAN-terra >= 1.7.17
BuildRequires:    R-CRAN-sp >= 1.0.6
BuildRequires:    R-CRAN-lattice >= 0.22.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-raster >= 3.4.13
Requires:         R-CRAN-terra >= 1.7.17
Requires:         R-CRAN-sp >= 1.0.6
Requires:         R-CRAN-lattice >= 0.22.5
Requires:         R-methods 
Requires:         R-CRAN-latticeExtra 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-viridisLite 

%description
Methods for enhanced visualization and interaction with raster data. It
implements visualization methods for quantitative data and categorical
data, both for univariate and multivariate rasters. It also provides
methods to display spatiotemporal rasters, and vector fields. See the
website for examples.

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
