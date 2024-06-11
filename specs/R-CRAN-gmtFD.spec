%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmtFD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          General Multiple Tests for Univariate and Multivariate Functional Data

License:          LGPL-2 | LGPL-3 | GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-GFDmcv 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-GFDmcv 
Requires:         R-CRAN-fda 

%description
The multiple contrast tests for univariate were proposed by Munko,
Ditzhaus, Pauly, Smaga, and Zhang (2023) <doi:10.48550/arXiv.2306.15259>.
Recently, they were extended to the multivariate functional data in Munko,
Ditzhaus, Pauly, and Smaga (2024) <doi:10.48550/arXiv.2406.01242>. These
procedures enable us to evaluate the overall hypothesis regarding
equality, as well as specific hypotheses defined by contrasts. In
particular, we can perform post hoc tests to examine particular
comparisons of interest. Different experimental designs are supported,
e.g., one-way and multi-way analysis of variance for functional data.

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
