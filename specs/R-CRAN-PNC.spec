%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PNC
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluating Phylogeny as a Proxy for Ecological Similarity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-phytools 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a trait-based workflow for evaluating whether phylogenetic
relatedness is informative about similarity in measured quantitative
traits within focal species pools and across multiple communities.
Functions support trait data integration, taxon-specific trait extraction,
coverage assessment, optional principal component analysis, and estimation
of phylogenetic signal using Pagel's lambda or Blomberg's K. Curated
quantitative trait datasets are included for plants, birds, mammals,
reptiles, amphibians, and fishes. Paired simulations assess how observed
patterns of missing trait data affect Pagel's lambda estimates and
significance classifications for individual traits. Methods for
quantifying phylogenetic signal are based on Pagel (1999)
<doi:10.1038/44766>, Blomberg et al. (2003)
<doi:10.1111/j.0014-3820.2003.tb00285.x>, and Münkemüller et al. (2012)
<doi:10.1111/j.2041-210X.2012.00196.x>.

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
