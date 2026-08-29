%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ctgimme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous-Time Subgrouping with GIMME

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-OpenMx 
Requires:         R-parallel 
Requires:         R-CRAN-ps 
Requires:         R-CRAN-qgraph 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates group-, subgroup-, and individual-level dynamic structures from
multivariate intensive longitudinal data using continuous-time state-space
models. The subgrouping procedure combines iterative shared-path searches
with recurrent-evidence feature screening and partitioning around medoids.
The continuous-time group iterative multiple model estimation method is
described in Park et al. (2025) <doi:10.1080/10705511.2024.2429544>.

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
