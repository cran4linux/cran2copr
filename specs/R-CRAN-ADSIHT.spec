%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ADSIHT
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Double Sparse Iterative Hard Thresholding

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-snowfall 

%description
Solving high-dimensional double sparse linear regression via an iterative
hard thresholding algorithm. Furthermore, the method is extended to
jointly estimate multiple graphical models.  For more details, please see
<https://www.jmlr.org/papers/v25/23-0653.html> and
<doi:10.48550/arXiv.2503.18722>.

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
