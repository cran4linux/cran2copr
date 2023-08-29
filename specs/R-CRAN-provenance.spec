%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  provenance
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Toolbox for Sedimentary Provenance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-IsoplotR >= 5.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-IsoplotR >= 5.2
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
Bundles a number of established statistical methods to facilitate the
visual interpretation of large datasets in sedimentary geology. Includes
functionality for adaptive kernel density estimation, principal component
analysis, correspondence analysis, multidimensional scaling, generalised
procrustes analysis and individual differences scaling using a variety of
dissimilarity measures. Univariate provenance proxies, such as
single-grain ages or (isotopic) compositions are compared with the
Kolmogorov-Smirnov, Kuiper, Wasserstein-2 or Sircombe-Hazelton L2
distances. Categorical provenance proxies such as chemical compositions
are compared with the Aitchison and Bray-Curtis distances,and count data
with the chi-square distance. Varietal data can either be converted to one
or more distributional datasets, or directly compared using the
multivariate Wasserstein distance. Also included are tools to plot
compositional and count data on ternary diagrams and point-counting data
on radial plots, to calculate the sample size required for specified
levels of statistical precision, and to assess the effects of hydraulic
sorting on detrital compositions. Includes an intuitive query-based user
interface for users who are not proficient in R.

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
