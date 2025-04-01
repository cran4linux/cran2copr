%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PlotFTIR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plot FTIR Spectra

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 

%description
The goal of 'PlotFTIR' is to easily and quickly kick-start the production
of journal-quality Fourier Transform Infra-Red (FTIR) spectral plots in R
using 'ggplot2'. The produced plots can be published directly or further
modified by 'ggplot2' functions. L'objectif de 'PlotFTIR' est de démarrer
facilement et rapidement la production des tracés spectraux de
spectroscopie infrarouge à transformée de Fourier (IRTF) de qualité
journal dans R à l'aide de 'ggplot2'. Les tracés produits peuvent être
publiés directement ou modifiés davantage par les fonctions 'ggplot2'.

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
