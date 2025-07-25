%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PFIM
%global packver   7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Population Fisher Information Matrix

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-knitr 
Requires:         R-utils 
Requires:         R-CRAN-inline 
Requires:         R-CRAN-Deriv 
Requires:         R-methods 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-knitr 

%description
Evaluate or optimize designs for nonlinear mixed effects models using the
Fisher Information matrix. Methods used in the package refer to Mentré F,
Mallet A, Baccar D (1997) <doi:10.1093/biomet/84.2.429>, Retout S, Comets
E, Samson A, Mentré F (2007) <doi:10.1002/sim.2910>, Bazzoli C, Retout S,
Mentré F (2009) <doi:10.1002/sim.3573>, Le Nagard H, Chao L, Tenaillon O
(2011) <doi:10.1186/1471-2148-11-326>, Combes FP, Retout S, Frey N, Mentré
F (2013) <doi:10.1007/s11095-013-1079-3> and Seurat J, Tang Y, Mentré F,
Nguyen TT (2021) <doi:10.1016/j.cmpb.2021.106126>.

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
