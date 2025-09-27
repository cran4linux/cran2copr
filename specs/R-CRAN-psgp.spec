%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psgp
%global packver   0.3-24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.24
Release:          1%{?dist}%{?buildtag}
Summary:          Projected Spatial Gaussian Process Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-intamap 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-intamap 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-Rcpp 

%description
Implements projected sparse Gaussian process Kriging ('Ingram et. al.',
2008, <doi:10.1007/s00477-007-0163-9>) as an additional method for the
'intamap' package. More details on implementation ('Barillec et. al.',
2010, <doi:10.1016/j.cageo.2010.05.008>).

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
