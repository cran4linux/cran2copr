%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pb210dating
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pb-210 Dating of Sediment Cores

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-lubridate 

%description
Dates sediment cores from lead-210 (Pb-210) activity profiles measured by
alpha or gamma spectrometry, following the unified formulation and
nomenclature of Sanchez-Cabeza and Ruiz-Fernandez (2012)
<doi:10.1016/j.gca.2010.12.024>. Implements the Constant Flux (CF) and
Constant Flux Constant Sedimentation (CFCS) dating models, together with
supporting tools for data input, decay correction, missing inventory
estimation, calculation of sediment and mass accumulation rates, and Monte
Carlo propagation of dating uncertainties as described in Sanchez-Cabeza
et al. (2014) <doi:10.1016/j.quageo.2014.06.002>. Also provides functions
to visualize activity profiles and resulting age models.

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
