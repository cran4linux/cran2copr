%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PTSR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Positive Time Series Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-numDeriv 

%description
A collection of functions to simulate, estimate and forecast a wide range
of regression based dynamic models for positive time series. This package
implements the results presented in Prass, T.S.; Pumi, G.; Taufemback,
C.G. and Carlos, J.H. (2025). "Positive time series regression models:
theoretical and computational aspects". Computational Statistics 40,
1185–1215. <doi:10.1007/s00180-024-01531-z>.

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
