%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geoTS
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Handling and Analyzing Time Series of Satellite Images

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-CRAN-ff >= 2.2.14
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-sp >= 1.2.0
BuildRequires:    R-CRAN-doParallel >= 1.0.14
BuildRequires:    R-CRAN-robustbase >= 0.95.0
Requires:         R-parallel >= 3.6.1
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-CRAN-ff >= 2.2.14
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-sp >= 1.2.0
Requires:         R-CRAN-doParallel >= 1.0.14
Requires:         R-CRAN-robustbase >= 0.95.0

%description
Provides functions and methods for: splitting large raster objects into
smaller chunks, transferring images from a binary format into raster
layers, transferring raster layers into an 'RData' file, calculating the
maximum gap (amount of consecutive missing values) of a numeric vector,
and fitting harmonic regression models to periodic time series. The
homoscedastic harmonic regression model is based on G. Roerink, M. Menenti
and W. Verhoef (2000) <doi:10.1080/014311600209814>.

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
