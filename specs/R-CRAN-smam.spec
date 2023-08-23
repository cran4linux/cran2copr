%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smam
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Modeling of Animal Movements

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-EnvStats 

%description
Animal movement models including Moving-Resting Process with Embedded
Brownian Motion (Yan et al., 2014, <doi:10.1007/s10144-013-0428-8>;
Pozdnyakov et al., 2017, <doi:10.1007/s11009-017-9547-6>), Brownian Motion
with Measurement Error (Pozdnyakov et al., 2014, <doi:10.1890/13-0532.1>),
Moving-Resting-Handling Process with Embedded Brownian Motion (Pozdnyakov
et al., 2020, <doi:10.1007/s11009-020-09774-1>), Moving-Resting Process
with Measurement Error (Hu et al., 2021, <doi:10.1111/2041-210X.13694>),
Moving-Moving Process with two Embedded Brownian Motions.

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
