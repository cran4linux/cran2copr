%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  musicNMR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conversion of Nuclear Magnetic Resonance Spectra in Audio Files

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave 
Requires:         R-CRAN-seewave 

%description
A collection of functions for converting and visualization the free
induction decay of mono dimensional nuclear magnetic resonance (NMR)
spectra into an audio file. It facilitates the conversion of Bruker
datasets in files WAV. The sound of NMR signals could provide an
alternative to the current representation of the individual metabolic
fingerprint and supply equally significant information. The package
includes also NMR spectra of the urine samples provided by four healthy
donors. Based on Cacciatore S, Saccenti E, Piccioli M. Hypothesis: the
sound of the individual metabolic phenotype? Acoustic detection of NMR
experiments. OMICS. 2015;19(3):147-56. <doi:10.1089/omi.2014.0131>.

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
