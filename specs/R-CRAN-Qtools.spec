%global packname  Qtools
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          2%{?dist}
Summary:          Utilities for Quantiles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glmx 
BuildRequires:    R-CRAN-Gmisc 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-utils 
Requires:         R-CRAN-glmx 
Requires:         R-CRAN-Gmisc 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-mice 
Requires:         R-boot 

%description
Functions for unconditional and conditional quantiles. These include
methods for transformation-based quantile regression, quantile-based
measures of location, scale and shape, methods for quantiles of discrete
variables, quantile-based multiple imputation, restricted quantile
regression, and directional quantile classification. A vignette is given
in Geraci (2016, The R Journal) <doi:10.32614/RJ-2016-037> and included in
the package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
