%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biocharkitgui
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Shiny' GUI for the 'biocharkit' Biochar Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-biocharkit >= 0.3.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
Requires:         R-CRAN-biocharkit >= 0.3.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 

%description
A point-and-click 'Shiny' interface to the 'biocharkit' package. Lets a
user upload Excel workbooks of biochar characterisation and batch
adsorption data, map spreadsheet columns to the required variables via
dropdown menus, and run sample-ID parsing, adsorption capacity and removal
efficiency calculations, isotherm fitting (Langmuir, Freundlich, Temkin,
Dubinin-Radushkevich, Sips), kinetics fitting (pseudo-first/ second-order,
Elovich, intraparticle diffusion), van't Hoff thermodynamics, batch
fitting across many samples at once, FTIR baseline correction, automatic
peak picking and functional-group analysis, XRD peak deconvolution and
crystallinity index, BET surface area, TGA analysis (DTG curve with
auto-detected decomposition peaks,
moisture/volatile-matter/ash/fixed-carbon straight off a curve for a
single sample or in batch across many, and Kissinger non-isothermal
kinetics from multi-heating-rate data), proximate/ultimate analysis, and
correlation matrices, without writing any R code. Results and 600 dpi TIFF
figures can be downloaded directly from the browser, along with a combined
analysis report.

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
