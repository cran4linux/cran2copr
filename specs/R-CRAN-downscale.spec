%global __brp_check_rpaths %{nil}
%global packname  downscale
%global packver   4.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Downscaling Species Occupancy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.4.20
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-minpack.lm >= 1.1.9
BuildRequires:    R-CRAN-cubature >= 1.1.2
BuildRequires:    R-CRAN-Rmpfr >= 0.5.7
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster >= 2.4.20
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-minpack.lm >= 1.1.9
Requires:         R-CRAN-cubature >= 1.1.2
Requires:         R-CRAN-Rmpfr >= 0.5.7
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 

%description
Uses species occupancy at coarse grain sizes to predict species occupancy
at fine grain sizes. Ten models are provided to fit and extrapolate the
occupancy-area relationship, as well as methods for preparing atlas data
for modelling. See Marsh et. al. (2018) <doi:10.18637/jss.v086.c03>.

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
