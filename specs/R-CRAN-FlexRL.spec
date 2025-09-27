%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FlexRL
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Flexible Model for Record Linkage

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-CRAN-Matrix >= 1.7
BuildRequires:    R-CRAN-progress >= 1.2.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-testit >= 0.13
Requires:         R-CRAN-Matrix >= 1.7
Requires:         R-CRAN-progress >= 1.2.3
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-testit >= 0.13

%description
Implementation of the Stochastic Expectation Maximisation (StEM) approach
to Record Linkage described in the paper by K. Robach, S. L. van der Pas,
M. A. van de Wiel and M. H. Hof (2024, <doi:10.1093/jrsssc/qlaf016>); see
citation("FlexRL") for details. This is a record linkage method, for
finding the common set of records among 2 data sources based on Partially
Identifying Variables (PIVs) available in both sources. It includes
modelling of dynamic Partially Identifying Variables (e.g. postal code)
that may evolve over time and registration errors (missing values and
mistakes in the registration). Low memory footprint.

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
