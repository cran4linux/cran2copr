%global packname  VIM
%global packver   6.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Imputation of Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-colorspace 
Requires:         R-grid 
Requires:         R-CRAN-car 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-vcd 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-ranger 

%description
New tools for the visualization of missing and/or imputed values are
introduced, which can be used for exploring the data and the structure of
the missing and/or imputed values. Depending on this structure of the
missing values, the corresponding methods may help to identify the
mechanism generating the missing values and allows to explore the data
including missing values. In addition, the quality of imputation can be
visually explored using various univariate, bivariate, multiple and
multivariate plot methods. A graphical user interface available in the
separate package VIMGUI allows an easy handling of the implemented plot
methods.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
