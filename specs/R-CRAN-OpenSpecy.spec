%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenSpecy
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze, Process, Identify, and Share Raman and (FT)IR Spectra

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-hyperSpec 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-shiny 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-hyperSpec 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-shiny 

%description
Raman and (FT)IR spectral analysis tool for plastic particles and other
environmental samples (Cowger et al. 2021,
<doi:10.1021/acs.analchem.1c00123>). With read_any(), Open Specy provides
a single function for reading individual, batch, or map spectral data
files like .asp, .csv, .jdx, .spc, .spa, .0, and .zip. process_spec()
simplifies processing spectra, including smoothing, baseline correction,
range restriction and flattening, intensity conversions, wavenumber
alignment, and min-max normalization. Spectra can be identified in batch
using an onboard reference library (Cowger et al. 2020,
<doi:10.1177/0003702820929064>) using match_spec(). A Shiny app is
available via run_app() or online at
<https://openanalysis.org/openspecy/>.

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
