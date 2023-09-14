%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AQLSchemes
%global packver   1.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieving Acceptance Sampling Schemes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions are included for recalling AQL (Acceptable Quality Level or
Acceptance Quality Level) Based single, double, and multiple attribute
sampling plans from the Military Standard (MIL-STD-105E) - American
National Standards Institute/American Society for Quality (ANSI/ASQ Z1.4)
tables and for retrieving variable sampling plans from Military Standard
(MIL-STD-414) - American National Standards Institute/American Society for
Quality (ANSI/ASQ Z1.9) tables. The sources for these tables are listed in
the URL: field. Also included are functions for computing the OC
(Operating Characteristic) and ASN (Average Sample Number) coordinates for
the attribute plans it recalls, and functions for computing the estimated
proportion nonconforming and the maximum allowable proportion
nonconforming for variable sampling plans. The MIL-STD AQL Sampling
schemes were the most used and copied set of standards in the world. They
are intended to be used for sampling a stream of lots, and were used in
contract agreements between supplier and customer companies. When the US
military dropped support of MIL-STD 105E and 414, The American National
Standards Institute (ANSI) and the International Standards Organization
(ISO) adopted the standard with few changes or no changes to the central
tables. This package is useful because its computer implementation of
these tables duplicates that available in other commercial software and
subscription online calculators.

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
