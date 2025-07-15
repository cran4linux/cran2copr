%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conMItion
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Mutual Information Estimation for Multi-Omics Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
The biases introduced in association measures, particularly mutual
information, are influenced by factors such as tumor purity, mutation
burden, and hypermethylation. This package provides the estimation of
conditional mutual information (CMI) and its statistical significance with
a focus on its application to multi-omics data. Utilizing B-spline
functions (inspired by Daub et al. (2004) <doi:10.1186/1471-2105-5-118>),
the package offers tools to estimate the association between heterogeneous
multi- omics data, while removing the effects of confounding factors. This
helps to unravel complex biological interactions. In addition, it includes
methods to evaluate the statistical significance of these associations,
providing a robust framework for multi-omics data integration and
analysis. This package is ideal for researchers in computational biology,
bioinformatics, and systems biology seeking a comprehensive tool for
understanding interdependencies in omics data.

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
