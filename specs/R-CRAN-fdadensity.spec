%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdadensity
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis for Density Functions by Transformation to a Hilbert Space

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-fdapace >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-fdapace >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.11.5

%description
An implementation of the methodology described in Petersen and Mueller
(2016) <doi:10.1214/15-AOS1363> for the functional data analysis of
samples of density functions.  Densities are first transformed to their
corresponding log quantile densities, followed by ordinary Functional
Principal Components Analysis (FPCA).  Transformation modes of variation
yield improved interpretation of the variability in the data as compared
to FPCA on the densities themselves.  The standard fraction of variance
explained (FVE) criterion commonly used for functional data is adapted to
the transformation setting, also allowing for an alternative
quantification of variability for density data through the Wasserstein
metric of optimal transport.

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
