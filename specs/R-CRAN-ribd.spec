%global packname  ribd
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pedigree-based Relatedness Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-pedtools 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-glue 

%description
Recursive algorithms for computing various relatedness coefficients,
including pairwise kinship, kappa and identity coefficients. Both
autosomal and X-linked coefficients are computed. Founders are allowed to
be inbred, enabling construction of any given kappa coefficients (Vigeland
(2020) <doi:10.1007/s00285-020-01505-x>). In addition to the standard
pairwise coefficients, ribd also computes a range of lesser-known
coefficients, including generalised kinship coefficients (Karigl (1981)
<doi:10.1111/j.1469-1809.1981.tb00341.x>; Weeks and Lange (1988)
<https:www.ncbi.nlm.nih.gov/pmc/articles/PMC1715269>), two-locus
coefficients (Thompson (1988) <doi:10.1093/imammb/5.4.261>) and
multi-person coefficients. This package is part of the ped suite, a
collection of packages for pedigree analysis in R.

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
