%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdWasserstein
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Application of Optimal Transport to Functional Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
These functions were developed to support statistical analysis on
functional covariance operators. The package contains functions to: -
compute 2-Wasserstein distances between Gaussian Processes as in
Masarotto, Panaretos & Zemel (2019) <doi:10.1007/s13171-018-0130-1>; -
compute the Wasserstein barycenter (Frechet mean) as in Masarotto,
Panaretos & Zemel (2019) <doi:10.1007/s13171-018-0130-1>; - perform
analysis of variance testing procedures for functional covariances and
tangent space principal component analysis of covariance operators as in
Masarotto, Panaretos & Zemel (2022) <arXiv:2212.04797>. - perform a
soft-clustering based on the Wasserstein distance where functional data
are classified based on their covariance structure as in Masarotto &
Masarotto (2023) <doi:10.1111/sjos.12692>.

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
