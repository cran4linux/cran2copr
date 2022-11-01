%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RHRV
%global packver   4.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Heart Rate Variability Analysis of ECG Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-waveslim >= 1.6.4
BuildRequires:    R-CRAN-lomb >= 1.0
BuildRequires:    R-CRAN-nonlinearTseries >= 0.2.3
Requires:         R-CRAN-waveslim >= 1.6.4
Requires:         R-CRAN-lomb >= 1.0
Requires:         R-CRAN-nonlinearTseries >= 0.2.3

%description
Allows users to import data files containing heartbeat positions in the
most broadly used formats, to remove outliers or points with unacceptable
physiological values present in the time series, to plot HRV data, and to
perform time domain, frequency domain and nonlinear HRV analysis. See
Garcia et al. (2017) <DOI:10.1007/978-3-319-65355-6>.

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
