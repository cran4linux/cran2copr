%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  opusreader2
%global packver   0.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Read Spectroscopic Data from Bruker OPUS Binary Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Reads data from Bruker OPUS binary files of Fourier-Transform infrared
spectrometers of the company Bruker Optics GmbH & Co. This package is
released independently from Bruker, and Bruker and OPUS are registered
trademarks of Bruker Optics GmbH & Co. KG.
<https://www.bruker.com/en/products-and-solutions/infrared-and-raman/opus-spectroscopy-software/latest-release.html>.
It lets you import both measurement data and parameters from OPUS files.
The main method is `read_opus()`, which reads one or multiple OPUS files
into a standardized list class. Behind the scenes, the reader parses the
file header for assigning spectral blocks and reading binary data from the
respective byte positions, using a reverse engineering approach. Infrared
spectroscopy combined with chemometrics and machine learning is an
established method to scale up chemical diagnostics in various industries
and scientific fields.

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
