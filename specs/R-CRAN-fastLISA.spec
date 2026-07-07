%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastLISA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Local Indicators of Spatial Association (LISA)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computes various Local Indicators of Spatial Association (LISA)
statistics, including univariate and bivariate local Moran's I, Empirical
Bayes local Moran's I, univariate and multivariate local Geary's C, and
Getis-Ord G and G* statistics. The methods follow Anselin (1995), Getis
and Ord (1992), and Anselin (2019). Leverages a high-performance, plain-C
backend with optional OpenMP multi-core support for fast permutation-based
pseudo-p-value calculation. Accepts any 'spdep' listw spatial weight
matrix, including custom and non-contiguity weights. Uses sample
standardisation (n-1) and 'rgeoda'-style permutation p-values. Output
cluster codes match 'rgeoda' conventions, including the Isolated category
for observations without neighbours.

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
