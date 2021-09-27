%global __brp_check_rpaths %{nil}
%global packname  LSDsensitivity
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis Tools for LSD Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-LSDinterface >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-lawstat 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-DiceKriging 
Requires:         R-CRAN-LSDinterface >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-kSamples 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-lawstat 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-car 
Requires:         R-CRAN-randtoolbox 
Requires:         R-parallel 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-DiceKriging 

%description
Tools for sensitivity analysis of LSD simulation models. Reads
object-oriented data produced by LSD simulation models and performs
screening and global sensitivity analysis (Sobol decomposition method,
Saltelli et al. (2008) ISBN:9780470725177). A Kriging or polynomial
meta-model (Kleijnen (2009) <doi:10.1016/j.ejor.2007.10.013>) is estimated
using the simulation data to provide the data required by the Sobol
decomposition. LSD (Laboratory for Simulation Development) is free
software developed by Marco Valente (documentation and downloads available
at <https://www.labsimdev.org/>).

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
