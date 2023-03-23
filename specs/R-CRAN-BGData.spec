%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BGData
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Suite of Packages for Analysis of Big Genomic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-crochet >= 2.1.0
BuildRequires:    R-CRAN-symDMatrix >= 2.0.0
BuildRequires:    R-CRAN-BEDMatrix >= 1.4.0
BuildRequires:    R-CRAN-LinkedMatrix >= 1.3.0
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-synchronicity 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-CRAN-bit 
Requires:         R-CRAN-crochet >= 2.1.0
Requires:         R-CRAN-symDMatrix >= 2.0.0
Requires:         R-CRAN-BEDMatrix >= 1.4.0
Requires:         R-CRAN-LinkedMatrix >= 1.3.0
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-synchronicity 
Requires:         R-CRAN-ff 
Requires:         R-CRAN-bit 

%description
An umbrella package providing a phenotype/genotype data structure and
scalable and efficient computational methods for large genomic datasets in
combination with several other packages: 'BEDMatrix', 'LinkedMatrix', and
'symDMatrix'.

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
