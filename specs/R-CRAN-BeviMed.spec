%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BeviMed
%global packver   5.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Evaluation of Variant Involvement in Mendelian Disease

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
A fast integrative genetic association test for rare diseases based on a
model for disease status given allele counts at rare variant sites.
Probability of association, mode of inheritance and probability of
pathogenicity for individual variants are all inferred in a Bayesian
framework - 'A Fast Association Test for Identifying Pathogenic Variants
Involved in Rare Diseases', Greene et al 2017
<doi:10.1016/j.ajhg.2017.05.015>.

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
