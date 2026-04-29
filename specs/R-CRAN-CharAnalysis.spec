%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CharAnalysis
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Peak Detection and Fire History from Sediment-Charcoal Records

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
A program for reconstructing local fire histories from high-resolution,
continuously sampled lake-sediment charcoal records. 'CharAnalysis'
decomposes a charcoal record into low- and high-frequency components and
uses locally defined thresholds to separate fire signal from noise,
following the approach of Higuera et al. (2009) <doi:10.1890/07-2019.1>,
with underlying assumptions and rationale described in Higuera et al.
(2010) <doi:10.1071/WF09134>. The package is designed for macroscopic
charcoal records with contiguous sampling fine enough to resolve
individual fire events, and is not appropriate for low-resolution or
discontinuously sampled records. See the package URL for the User's Guide
and application examples.

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
