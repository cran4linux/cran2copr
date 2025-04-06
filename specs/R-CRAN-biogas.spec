%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biogas
%global packver   1.64.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.64.0
Release:          1%{?dist}%{?buildtag}
Summary:          Process Biogas Data and Predict Biogas Production

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Functions for calculating biochemical methane potential (BMP) from
laboratory measurements and other types of data processing and prediction
useful for biogas research. Raw laboratory measurements for diverse
methods (volumetric, manometric, gravimetric, gas density) can be
processed to calculate BMP. Theoretical maximum BMP or methane or biogas
yield can be predicted from various measures of substrate composition.
Molar mass and calculated oxygen demand (COD') can be determined from a
chemical formula. Measured gas volume can be corrected for water vapor and
to standard (or user-defined) temperature and pressure. Gas quantity can
be converted between volume, mass, and moles. A function for planning BMP
experiments can consider multiple constraints in suggesting substrate or
inoculum quantities, and check for problems. Inoculum and substrate mass
can be determined for planning BMP experiments. Finally, a set of
first-order models can be fit to measured methane production rate or
cumulative yield in order to extract estimates of ultimate yield and
kinetic constants. See Hafner et al. (2018)
<doi:10.1016/j.softx.2018.06.005> for details. OBA is a web application
that provides access to some of the package functionality:
<https://biotransformers.shinyapps.io/oba1/>. The Standard BMP Methods
website documents the calculations in detail:
<https://www.dbfz.de/en/BMP>.

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
