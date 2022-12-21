%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aphylo
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference and Prediction of Annotations in Phylogenetic Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-fmcmc 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-fmcmc 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-xml2 

%description
Implements a parsimonious evolutionary model to analyze and predict
gene-functional annotations in phylogenetic trees as described in Vega Yon
et al. (2021) <doi:10.1371/journal.pcbi.1007948>. With a focus on
computational efficiency, 'aphylo' makes it possible to estimate pooled
phylogenetic models, including thousands (hundreds) of annotations (trees)
in the same run. The package also provides the tools for visualization of
annotated phylogenies, calculation of posterior probabilities
(prediction,) and goodness-of-fit assessment featured in Vega Yon et al.
(2021).

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
