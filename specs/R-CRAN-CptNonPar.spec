%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CptNonPar
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Change Point Detection for Multivariate Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-iterators 
Requires:         R-stats 

%description
Implements the nonparametric moving sum procedure for detecting changes in
the joint characteristic function (NP-MOJO) for multiple change point
detection in multivariate time series. See McGonigle, E. T., Cho, H.
(2025) <doi:10.1093/biomet/asaf024> for description of the NP-MOJO
methodology.

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
