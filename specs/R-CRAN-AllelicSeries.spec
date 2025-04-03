%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AllelicSeries
%global packver   0.1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Allelic Series Test

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RNOmni 
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RNOmni 
Requires:         R-CRAN-SKAT 

%description
Implementation of gene-level rare variant association tests targeting
allelic series: genes where increasingly deleterious mutations have
increasingly large phenotypic effects. The COding-variant Allelic Series
Test (COAST) operates on the benign missense variants (BMVs), deleterious
missense variants (DMVs), and protein truncating variants (PTVs) within a
gene. COAST uses a set of adjustable weights that tailor the test towards
rejecting the null hypothesis for genes where the average magnitude of
effect increases monotonically from BMVs to DMVs to PTVs. See McCaw ZR,
O’Dushlaine C, Somineni H, Bereket M, Klein C, Karaletsos T, Casale FP,
Koller D, Soare TW. (2023) "An allelic series rare variant association
test for candidate gene discovery" <doi:10.1016/j.ajhg.2023.07.001>.

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
