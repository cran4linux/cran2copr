%global __brp_check_rpaths %{nil}
%global packname  hyperSpec
%global packver   0.100.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.100.0
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Hyperspectral Data, i.e. Spectra + Meta Information (Spatial, Time, Concentration, ...)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-lattice 
Requires:         R-grid 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-testthat 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-dplyr 

%description
Comfortable ways to work with hyperspectral data sets. I.e. spatially or
time-resolved spectra, or spectra with any other kind of information
associated with each of the spectra. The spectra can be data as obtained
in XRF, UV/VIS, Fluorescence, AES, NIR, IR, Raman, NMR, MS, etc. More
generally, any data that is recorded over a discretized variable, e.g.
absorbance = f(wavelength), stored as a vector of absorbance values for
discrete wavelengths is suitable.

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
