%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metevalue
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          E-Value in the Omics Data Association Studies

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-dplyr 

%description
In the omics data association studies, it is common to conduct the p-value
corrections to control the false significance. Among those p-value
correction methods, E-value is recently studied based on V. Vovk and R.
Wang (2021) <doi:10.1214/20-AOS2020>. This package provides e-value
calculation for several types of omics data association studies.
Currently, four data formats are supported: BiSeq, MDRfinder, methylKit
and metilene data. The relevant references are listed below: Katja
Hebestreit and Hans-Ulrich Klein (2022) <doi:10.18129/B9.bioc.BiSeq>;
Altuna Akalin et.al (2012) <doi:10.18129/B9.bioc.methylKit>.

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
