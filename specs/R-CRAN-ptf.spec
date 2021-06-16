%global packname  ptf
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probit Tensor Factorization

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-rARPACK >= 0.11
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-rARPACK >= 0.11

%description
Efficient algorithms to implement Probit Tensor Factorization (PTF) model
for statistical relational learning, which not only inherits the
computation efficiency from the classic tensor factorization model but
also accounts for the binary nature of relational data. The methodology is
based on Ye Liu (2021)
<https://repository.lib.ncsu.edu/bitstream/handle/1840.20/37507/etd.pdf?sequence=1>
"Computational Methods for Complex Models with Latent Structure".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
