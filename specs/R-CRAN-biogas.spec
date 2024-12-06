%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biogas
%global packver   1.61
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.61
Release:          1%{?dist}%{?buildtag}
Summary:          Process Biogas Data and Predict Biogas Production

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
High- and low-level functions for processing biogas data and predicting
biogas production. Molar mass and calculated oxygen demand (COD') can be
determined from a chemical formula. Measured gas volume can be corrected
for water vapor and to (possibly user-defined) standard temperature and
pressure. Gas quantity can be converted between volume, mass, and moles.
Gas composition, cumulative production, or other variables can be
interpolated to a specified time. Cumulative biogas and methane production
(and rates) can be calculated from raw data obtained using volumetric,
manometric, gravimetric, or gas density methods for any number of bottles.
With cumulative methane production data and data on bottle contents,
biochemical methane potential (BMP) or specific methane production (SMP)
can be calculated and summarized, including subtraction of the inoculum
contribution and normalization by substrate mass. Cumulative production
and production rates can be summarized in several different ways (e.g.,
omitting normalization) using the same function. Biogas quantity and
composition can be predicted from substrate composition and additional,
optional data. Inoculum and substrate mass can be determined for planning
BMP experiments. Finally, first-order models can be fit to measurements in
order to extract estimates of ultimate yield and kinetic constants.

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
