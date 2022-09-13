%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IsoriX
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          Isoscape Computation and Inference of Spatial Origins using Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spaMM >= 3.13
BuildRequires:    R-CRAN-rasterVis >= 0.30
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-spaMM >= 3.13
Requires:         R-CRAN-rasterVis >= 0.30
Requires:         R-CRAN-elevatr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-viridisLite 

%description
Building isoscapes using mixed models and inferring the geographic origin
of samples based on their isotopic ratios. This package is essentially a
simplified interface to several other packages which implements a new
statistical framework based on mixed models. It uses 'spaMM' for fitting
and predicting isoscapes, and assigning an organism's origin depending on
its isotopic ratio. 'IsoriX' also relies heavily on the package
'rasterVis' for plotting the maps produced with 'raster' using 'lattice'.

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
