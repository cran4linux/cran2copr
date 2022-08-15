%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waveslim
%global packver   1.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Wavelet Routines for One-, Two-, and Three-Dimensional Signal Processing

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Basic wavelet routines for time series (1D), image (2D) and array (3D)
analysis.  The code provided here is based on wavelet methodology
developed in Percival and Walden (2000); Gencay, Selcuk and Whitcher
(2001); the dual-tree complex wavelet transform (DTCWT) from Kingsbury
(1999, 2001) as implemented by Selesnick; and Hilbert wavelet pairs
(Selesnick 2001, 2002). All figures in chapters 4-7 of GSW (2001) are
reproducible using this package and R code available at the book
website(s) below.

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
