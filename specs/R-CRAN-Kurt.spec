%global __brp_check_rpaths %{nil}
%global packname  Kurt
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Performs Kurtosis-Based Statistical Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-matrixcalc >= 1.0.5
BuildRequires:    R-CRAN-labstatR >= 1.0.11
BuildRequires:    R-CRAN-expm >= 0.999.6
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-matrixcalc >= 1.0.5
Requires:         R-CRAN-labstatR >= 1.0.11
Requires:         R-CRAN-expm >= 0.999.6

%description
Computes measures of multivariate kurtosis, matrices of fourth-order
moments and cumulants, kurtosis-based projection pursuit. Franceschini, C.
and Loperfido, N. (2018, ISBN:978-3-319-73905-2). "An Algorithm for
Finding Projections with Extreme Kurtosis". Loperfido, N.
(2017,ISSN:0024-3795). "A New Kurtosis Matrix, with Statistical
Applications".

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
