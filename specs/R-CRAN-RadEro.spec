%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RadEro
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Cs-137 Conversion Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-roxygen2 >= 7.2.3
BuildRequires:    R-utils >= 4.3.1
BuildRequires:    R-stats >= 4.3.1
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-devtools >= 2.4.5
BuildRequires:    R-CRAN-usethis >= 2.2.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.7
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-patchwork >= 1.1.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-roxygen2 >= 7.2.3
Requires:         R-utils >= 4.3.1
Requires:         R-stats >= 4.3.1
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-devtools >= 2.4.5
Requires:         R-CRAN-usethis >= 2.2.2
Requires:         R-CRAN-jsonlite >= 1.8.7
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-patchwork >= 1.1.3
Requires:         R-CRAN-Rcpp >= 1.0.11

%description
A straightforward model to estimate soil migration rates across various
soil contexts. Based on the compartmental, vertically-resolved,
physically-based mass balance model of Soto and Navas (2004)
<doi:10.1016/j.jaridenv.2004.02.003> and Soto and Navas (2008)
<doi:10.1016/j.radmeas.2008.02.024>. 'RadEro' provides a user-friendly
interface in R, utilizing input data such as 137Cs inventories and
parameters directly derived from soil samples (e.g., fine fraction
density, effective volume) to accurately capture the 137Cs distribution
within the soil profile. The model simulates annual 137Cs fallout,
radioactive decay, and vertical diffusion, with the diffusion coefficient
calculated from 137Cs reference inventory profiles. Additionally, it
allows users to input custom parameters as calibration coefficients. The
RadEro user manual and protocol, including detailed instructions on how to
format input data and configuration files, can be found at the following
link: <https://github.com/eead-csic-eesa/RadEro>.

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
