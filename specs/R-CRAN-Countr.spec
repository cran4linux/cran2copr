%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Countr
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Univariate Count Models Based on Renewal Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-VGAM >= 1.1.1
BuildRequires:    R-CRAN-Rdpack >= 0.7.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-standardize 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-VGAM >= 1.1.1
Requires:         R-CRAN-Rdpack >= 0.7.0
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-standardize 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-car 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-RColorBrewer 

%description
Flexible univariate count models based on renewal processes. The models
may include covariates and can be specified with familiar formula syntax
as in glm() and package 'flexsurv'.  The methodology is described by
Kharrat et all (2019) <doi:10.18637/jss.v090.i13> (included as vignette
'Countr_guide' in the package).

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
