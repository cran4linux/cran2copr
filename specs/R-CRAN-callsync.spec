%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  callsync
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Recording Synchronisation, Call Detection and Assignment, Audio Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave >= 2.2.0
BuildRequires:    R-CRAN-oce >= 1.7
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-tuneR >= 1.4.0
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-signal >= 0.7
Requires:         R-CRAN-seewave >= 2.2.0
Requires:         R-CRAN-oce >= 1.7
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-tuneR >= 1.4.0
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-signal >= 0.7

%description
Intended to analyse recordings from multiple microphones (e.g., backpack
microphones in captive setting). It allows users to align recordings even
if there is non-linear drift of several minutes between them. A call
detection and assignment pipeline can be used to find vocalisations and
assign them to the vocalising individuals (even if the vocalisation is
picked up on multiple microphones). The tracing and measurement functions
allow for detailed analysis of the vocalisations and filtering of noise.
Finally, the package includes a function to run spectrographic cross
correlation, which can be used to compare vocalisations. It also includes
multiple other functions related to analysis of vocal behaviour.

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
