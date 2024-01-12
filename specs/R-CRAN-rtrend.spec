%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtrend
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Trend Estimating Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fftwtools 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fftwtools 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-plyr 

%description
The traditional linear regression trend, Modified Mann-Kendall (MK)
non-parameter trend and bootstrap trend are included in this package.
Linear regression trend is rewritten by '.lm.fit'. MK trend is rewritten
by 'Rcpp'. Finally, those functions are about 10 times faster than
previous version in R. Reference: Hamed, K. H., & Rao, A. R. (1998). A
modified Mann-Kendall trend test for autocorrelated data. Journal of
hydrology, 204(1-4), 182-196. <doi:10.1016/S0022-1694(97)00125-X>.

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
