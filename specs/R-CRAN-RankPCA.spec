%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RankPCA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rank of Variables Based on Principal Component Analysis for Mixed Data Types

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
Requires:         R-stats 
Requires:         R-CRAN-caret 

%description
Principal Component Analysis (PCA) is a statistical technique used to
reduce the dimensionality of a dataset while preserving as much
variability as possible. By transforming the original variables into a new
set of uncorrelated variables called principal components, PCA helps in
identifying patterns and simplifying the complexity of high-dimensional
data. The 'RankPCA' package provides a streamlined workflow for performing
PCA on datasets containing both categorical and continuous variables. It
facilitates data preprocessing, encoding of categorical variables, and
computes PCA to determine the optimal number of principal components based
on a specified variance threshold. The package also computes composite
indices for ranking observations, which can be useful for various
analytical purposes. Garai, S., & Paul, R. K. (2023)
<doi:10.1016/j.iswa.2023.200202>.

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
