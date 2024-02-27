%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Unico
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Cross-Omics Deconvolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-testit 
BuildRequires:    R-utils 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-config 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-testit 
Requires:         R-utils 

%description
UNIfied Cross-Omics deconvolution (Unico) deconvolves standard
2-dimensional bulk matrices of samples by features into a 3-dimensional
tensors representing samples by features by cell types. Unico stands out
as the first principled model-based deconvolution method that is
theoretically justified for any heterogeneous genomic data. For more
details see Chen and Rahmani et al. (2024)
<doi:10.1101/2024.01.27.577588>.

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
