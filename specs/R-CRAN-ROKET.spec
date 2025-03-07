%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROKET
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Transport-Based Kernel Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-smarter 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-MiRKAT 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-smarter 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-MiRKAT 

%description
Perform optimal transport on somatic point mutations and kernel regression
hypothesis testing by integrating pathway level similarities at the gene
level (Little et al. (2023) <doi:10.1111/biom.13769>). The software
implements balanced and unbalanced optimal transport and omnibus tests
with 'C++' across a set of tumor samples and allows for multi-threading to
decrease computational runtime.

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
