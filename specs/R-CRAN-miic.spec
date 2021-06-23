%global __brp_check_rpaths %{nil}
%global packname  miic
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Causal or Non-Causal Graphical Models Using Information Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
We report an information-theoretic method which learns a large class of
causal or non-causal graphical models from purely observational data,
while including the effects of unobserved latent variables, commonly found
in many datasets. Starting from a complete graph, the method iteratively
removes dispensable edges, by uncovering significant information
contributions from indirect paths, and assesses edge-specific confidences
from randomization of available data. The remaining edges are then
oriented based on the signature of causality in observational data. This
approach can be applied on a wide range of datasets and provide new
biological insights on regulatory networks from single cell expression
data, genomic alterations during tumor development and co-evolving
residues in protein structures. For more information you can refer to:
Cabeli et al. PLoS Comp. Bio. 2020 <doi:10.1371/journal.pcbi.1007866>,
Verny et al. PLoS Comp. Bio. 2017 <doi:10.1371/journal.pcbi.1005662>.

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
