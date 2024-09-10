%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RefBasedMI
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reference-Based Imputation for Longitudinal Clinical Trials with Protocol Deviation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-assertthat 

%description
Imputation of missing numerical outcomes for a longitudinal trial with
protocol deviations. The package uses distinct treatment arm-based
assumptions for the unobserved data, following the general algorithm of
Carpenter, Roger, and Kenward (2013) <doi:10.1080/10543406.2013.834911>,
and the causal model of White, Royes and Best (2020)
<doi:10.1080/10543406.2019.1684308>. Sensitivity analyses to departures
from these assumptions can be done by the Delta method of Roger. The
program uses the same algorithm as the 'mimix' 'Stata' package written by
Suzie Cro, with additional coding for the causal model and delta method.
The reference-based methods are jump to reference (J2R), copy increments
in reference (CIR), copy reference (CR), and the causal model, all of
which must specify the reference treatment arm. Other methods are missing
at random (MAR) and the last mean carried forward (LMCF).
Individual-specific imputation methods (and their reference groups) can be
specified.

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
