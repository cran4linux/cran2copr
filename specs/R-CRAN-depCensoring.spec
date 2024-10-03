%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depCensoring
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for Survival Data with Dependent Censoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rafalib 
BuildRequires:    R-CRAN-rvinecopulib 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-SemiPar.depCens 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pbivnorm 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rafalib 
Requires:         R-CRAN-rvinecopulib 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-SemiPar.depCens 

%description
Several statistical methods for analyzing survival data under various
forms of dependent censoring are implemented in the package. In addition
to accounting for dependent censoring, it offers tools to adjust for
unmeasured confounding factors. The implemented approaches allow users to
estimate the dependency between survival time and dependent censoring
time, based solely on observed survival data. For more details on the
methods, refer to Deresa and Van Keilegom (2021)
<doi:10.1093/biomet/asaa095>, Czado and Van Keilegom (2023)
<doi:10.1093/biomet/asac067>, Crommen et al. (2024)
<doi:10.1007/s11749-023-00903-9> and Willems et al. (2024+)
<https:arxiv.org/abs/2403.11860>.

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
