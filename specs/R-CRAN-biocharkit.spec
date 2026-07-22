%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biocharkit
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Biochar Characterisation and Adsorption Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
A toolkit for analysing biochar characterisation and batch adsorption
experiments. Provides functions to parse structured sample identifiers
encoding pyrolysis conditions, read raw FTIR and XRD instrument output,
compute adsorption capacity and removal efficiency, fit adsorption
isotherms following Langmuir (1918) <doi:10.1021/ja02242a004> and Sips
(1948) <doi:10.1063/1.1746922> among other models, fit adsorption kinetics
following Ho and McKay (1999) <doi:10.1016/S0032-9592(98)00112-5> and
Chien and Clayton (1980) <doi:10.2136/sssaj1980.03615995004400020013x>
among other models, fit batches of samples at once, compute van't Hoff
thermodynamic parameters, baseline-correct and pick peaks in FTIR spectra,
deconvolve XRD patterns into a crystallinity index, compute BET surface
area following Brunauer, Emmett, and Teller (1938)
<doi:10.1021/ja01269a023>, compute proximate and ultimate analysis
summaries including directly from a thermogravimetric analysis (TGA)
curve, compute a smoothed derivative thermogravimetric (DTG) curve and
pick its decomposition peaks, fit non-isothermal decomposition kinetics
from multi-heating-rate TGA data following Kissinger (1957)
<doi:10.1021/ac60131a045>, build correlation matrices with p-values, and
produce publication-style base-graphics figures including 600 dpi TIFF
export. Built on base R ('stats', 'graphics', 'grDevices') so it has no
dependency on packages that require external CRAN network access to
install.

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
