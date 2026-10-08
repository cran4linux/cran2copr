%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OpenSpecy
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze, Process, Identify, and Share Raman and (FT)IR Spectra

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-hyperSpec 
BuildRequires:    R-CRAN-mmand 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-hyperSpec 
Requires:         R-CRAN-mmand 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-matrixStats 

%description
Raman and (FT)IR spectral analysis tool for plastic particles and other
environmental samples (Cowger et al. 2025,
<doi:10.1021/acs.analchem.5c00962>). With read_any(), Open Specy provides
a single function for reading individual, batch, or map spectral data
files like .asp, .csv, .jdx, .spc, .spa, .0, and .zip. process_spec()
simplifies processing spectra, including smoothing, baseline correction,
range restriction and flattening, intensity conversions, wavenumber
alignment, and min-max normalization. Spectra can be identified in batch
using an onboard reference library using match_spec(). A bundled Shiny app
is available via run_app() or online at
<https://www.openanalysis.org/OpenSpecyV2/>.

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
