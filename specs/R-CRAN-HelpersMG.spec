%global __brp_check_rpaths %{nil}
%global packname  HelpersMG
%global packver   4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.8
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Environmental Analyses, Ecotoxicology and Various R Functions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Contains miscellaneous functions useful for managing 'NetCDF' files (see
<https://en.wikipedia.org/wiki/NetCDF>), get moon phase and time for sun
rise and fall, tide level, analyse and reconstruct periodic time series of
temperature with irregular sinusoidal pattern, show scales and wind rose
in plot with change of color of text, Metropolis-Hastings algorithm for
Bayesian MCMC analysis, plot graphs or boxplot with error bars, search
files in disk by there names or their content, read the contents of all
files from a folder at one time.

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
