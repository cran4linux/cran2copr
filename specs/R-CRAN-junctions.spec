%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  junctions
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          The Breakdown of Genomic Ancestry Blocks in Hybrid Lineages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 5.0.0
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-RcppParallel >= 5.0.0
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-tibble 

%description
Individual based simulations of hybridizing populations, where the
accumulation of junctions is tracked. Furthermore, mathematical equations
are provided to verify simulation outcomes. Both simulations and
mathematical equations are based on Janzen (2018, <doi:10.1101/058107>)
and Janzen (2022, <doi:10.1111/1755-0998.13519>).

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
