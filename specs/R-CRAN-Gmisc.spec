%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Gmisc
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Descriptive Statistics, Transition Plots, and More

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-htmlTable >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-forestplot 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
Requires:         R-CRAN-htmlTable >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-forestplot 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-glue 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-yaml 
Requires:         R-utils 

%description
Tools for making the descriptive "Table 1" used in medical articles, a
transition plot for showing changes between categories (also known as a
Sankey diagram), flow charts by extending the grid package, a method for
variable selection based on the SVD, Bézier lines with arrows
complementing the ones in the 'grid' package, and more.

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
