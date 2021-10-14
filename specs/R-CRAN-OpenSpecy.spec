%global __brp_check_rpaths %{nil}
%global packname  OpenSpecy
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze, Process, Identify, and Share, Raman and (FT)IR Spectra

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-hyperSpec 
BuildRequires:    R-CRAN-hexView 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-hyperSpec 
Requires:         R-CRAN-hexView 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-shiny 

%description
Raman and (FT)IR spectral analysis tool for plastic particles and other
environmental samples (Cowger et al. 2021,
<doi:10.1021/acs.analchem.1c00123>). Supported features include reading
spectral data files (.asp, .csv, .jdx, .spc, .spa, .0), Savitzky-Golay
smoothing of spectral intensities with smooth_intens(), correcting
background noise with subtr_bg() in accordance with Zhao et al. (2007)
<doi:10.1366/000370207782597003>, and identifying spectra using an onboard
reference library (Cowger et al. 2020, <doi:10.1177/0003702820929064>).
Analyzed spectra can be shared with the Open Specy community. A Shiny app
is available via run_app() or online at
<https://wincowger.shinyapps.io/OpenSpecy/>.

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
