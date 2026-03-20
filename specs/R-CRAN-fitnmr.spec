%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitnmr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Nuclear Magnetic Resonance Peak Fitting and Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Tools for fitting and analyzing 1D-4D nuclear magnetic resonance spectra
with analytical models of peak shapes and peak groups. The package reads
spectra in 'NMRPipe' format, builds constrained parameter structures for
chemical shifts, line widths, scalar couplings, volumes, and phases, and
performs nonlinear least-squares optimization for iterative peak discovery
or simultaneous fits across multiple spectra. It also provides methods for
visualization, preprocessing, and kinetic analysis of 1D time-series data,
including automated phase optimization, solvent suppression, time-domain
correction for frequency shifts and line broadening, modeling spectra as
linear combinations of two component spectra, and exponential rate
fitting.

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
