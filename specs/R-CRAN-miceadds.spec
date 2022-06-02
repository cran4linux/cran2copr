%global __brp_check_rpaths %{nil}
%global packname  miceadds
%global packver   3.13-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.13.12
Release:          1%{?dist}%{?buildtag}
Summary:          Some Additional Multiple Imputation Functions, Especially for 'mice'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-mice >= 3.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mice >= 3.0.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains functions for multiple imputation which complements existing
functionality in R. In particular, several imputation methods for the mice
package (van Buuren & Groothuis-Oudshoorn, 2011,
<doi:10.18637/jss.v045.i03>) are included. Main features of the miceadds
package include plausible value imputation (Mislevy, 1991,
<doi:10.1007/BF02294457>), multilevel imputation for variables at any
level or with any number of hierarchical and non-hierarchical levels
(Grund, Luedtke & Robitzsch, 2018, <doi:10.1177/1094428117703686>; van
Buuren, 2018, Ch.7, <doi:10.1201/9780429492259>), imputation using partial
least squares (PLS) for high dimensional predictors (Robitzsch, Pham &
Yanagida, 2016), nested multiple imputation (Rubin, 2003,
<doi:10.1111/1467-9574.00217>), substantive model compatible imputation
(Bartlett et al., 2015, <doi:10.1177/0962280214521348>), and features for
the generation of synthetic datasets (Reiter, 2005,
<doi:10.1111/j.1467-985X.2004.00343.x>; Nowok, Raab, & Dibben, 2016,
<doi:10.18637/jss.v074.i11>).

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
