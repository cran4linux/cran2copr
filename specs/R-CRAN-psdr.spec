%global __brp_check_rpaths %{nil}
%global packname  psdr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Use Time Series to Generate and Compare Power Spectral Density

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.2
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-devtools >= 2.4.1
BuildRequires:    R-CRAN-qpdf >= 1.1
Requires:         R-stats >= 4.0.2
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-devtools >= 2.4.1
Requires:         R-CRAN-qpdf >= 1.1

%description
Functions that allow you to generate and compare power spectral density
(PSD) plots given time series data. Fast Fourier Transform (FFT) is used
to take a time series data, analyze the oscillations, and then output the
frequencies of these oscillations in the time series in the form of a PSD
plot.Thus given a time series, the dominant frequencies in the time series
can be identified. Additional functions in this package allow the dominant
frequencies of multiple groups of time series to be compared with each
other. To see example usage with the main functions of this package,
please visit this site:
<https://yhhc2.github.io/psdr/articles/Introduction.html>. The
mathematical operations used to generate the PSDs are described in these
sites: <https://www.mathworks.com/help/matlab/ref/fft.html>.
<https://www.mathworks.com/help/signal/ug/power-spectral-density-estimates-using-fft.html>.

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
