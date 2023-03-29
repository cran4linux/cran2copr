%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigsnpr
%global packver   1.12.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Massive SNP Arrays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-bigstatsr >= 1.5.11
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600
BuildRequires:    R-CRAN-bigsparser >= 0.6
BuildRequires:    R-CRAN-bigutilsr >= 0.3.3
BuildRequires:    R-CRAN-runonce >= 0.2.3
BuildRequires:    R-CRAN-bigassertr >= 0.1.6
BuildRequires:    R-CRAN-roptim >= 0.1.6
BuildRequires:    R-CRAN-bigparallelr 
BuildRequires:    R-CRAN-bigreadr 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-bigstatsr >= 1.5.11
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-bigsparser >= 0.6
Requires:         R-CRAN-bigutilsr >= 0.3.3
Requires:         R-CRAN-runonce >= 0.2.3
Requires:         R-CRAN-bigassertr >= 0.1.6
Requires:         R-CRAN-bigparallelr 
Requires:         R-CRAN-bigreadr 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-vctrs 

%description
Easy-to-use, efficient, flexible and scalable tools for analyzing massive
SNP arrays. Privé et al. (2018) <doi:10.1093/bioinformatics/bty185>.

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
