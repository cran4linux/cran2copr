%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gcxgclab
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          GCxGC Preprocessing and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.0
BuildRequires:    R-utils >= 4.2.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-Rdpack >= 2.4.0
BuildRequires:    R-CRAN-ptw >= 1.9.16
BuildRequires:    R-CRAN-zoo >= 1.8.11
BuildRequires:    R-CRAN-nls.multstart >= 1.3.0
BuildRequires:    R-CRAN-ncdf4 >= 1.19
BuildRequires:    R-CRAN-nilde >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.0.8
Requires:         R-stats >= 4.2.0
Requires:         R-utils >= 4.2.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-Rdpack >= 2.4.0
Requires:         R-CRAN-ptw >= 1.9.16
Requires:         R-CRAN-zoo >= 1.8.11
Requires:         R-CRAN-nls.multstart >= 1.3.0
Requires:         R-CRAN-ncdf4 >= 1.19
Requires:         R-CRAN-nilde >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.0.8

%description
Provides complete detailed preprocessing of two-dimensional gas
chromatogram (GCxGC) samples. Baseline correction, smoothing, peak
detection, and peak alignment. Also provided are some analysis functions,
such as finding extracted ion chromatograms, finding mass spectral data,
targeted analysis, and nontargeted analysis with either the 'National
Institute of Standards and Technology Mass Spectral Library' or with the
mass data. There are also several visualization methods provided for each
step of the preprocessing and analysis.

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
