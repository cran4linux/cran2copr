%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statgenGWAS
%global packver   1.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.13
Release:          1%{?dist}%{?buildtag}
Summary:          Genome Wide Association Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-sommer >= 4.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-LMMsolver 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-sommer >= 4.4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-LMMsolver 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 

%description
Fast single trait Genome Wide Association Studies (GWAS) following the
method described in Kang et al. (2010), <doi:10.1038/ng.548>. One of a
series of statistical genetic packages for streamlining the analysis of
typical plant breeding experiments developed by Biometris.

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
