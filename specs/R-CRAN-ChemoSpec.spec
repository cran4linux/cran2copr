%global packname  ChemoSpec
%global packver   5.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Chemometrics for Spectroscopy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-readJDX >= 0.4
BuildRequires:    R-CRAN-ChemoSpecUtils >= 0.3
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-readJDX >= 0.4
Requires:         R-CRAN-ChemoSpecUtils >= 0.3
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
A collection of functions for top-down exploratory data analysis of
spectral data including nuclear magnetic resonance (NMR), infrared (IR),
Raman, X-ray fluorescence (XRF) and other similar types of spectroscopy.
Includes functions for plotting and inspecting spectra, peak alignment,
hierarchical cluster analysis (HCA), principal components analysis (PCA)
and model-based clustering. Robust methods appropriate for this type of
high-dimensional data are available. ChemoSpec is designed for structured
experiments, such as metabolomics investigations, where the samples fall
into treatment and control groups. Graphical output is formatted
consistently for publication quality plots. ChemoSpec is intended to be
very user friendly and to help you get usable results quickly. A vignette
covering typical operations is available.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
