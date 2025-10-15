%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  douconca
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Double Constrained Correspondence Analysis for Trait-Environment Analysis in Ecology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-vegan >= 2.6.8
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-vegan >= 2.6.8
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Double constrained correspondence analysis (dc-CA) analyzes (multi-)trait
(multi-)environment ecological data by using the 'vegan' package and
native R code. Throughout the two step algorithm of ter Braak et al.
(2018) is used. This algorithm combines and extends community- (sample-)
and species-level analyses, i.e. the usual community weighted means
(CWM)-based regression analysis and the species-level analysis of
species-niche centroids (SNC)-based regression analysis. The two steps use
canonical correspondence analysis to regress the abundance data on to the
traits and (weighted) redundancy analysis to regress the CWM of the
orthonormalized traits on to the environmental predictors. The function
dc_CA() has an option to divide the abundance data of a site by the site
total, giving equal site weights. This division has the advantage that the
multivariate analysis corresponds with an unweighted (multi-trait)
community-level analysis, instead of being weighted. The first step of the
algorithm uses vegan::cca(). The second step uses wrda() but vegan::rda()
if the site weights are equal. This version has a predict() function. For
details see ter Braak et al. 2018 <doi:10.1007/s10651-017-0395-x>. and ter
Braak & van Rossum 2025 <doi:10.1016/j.ecoinf.2025.103143>.

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
