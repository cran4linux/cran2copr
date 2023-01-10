%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdcMicro
%global packver   5.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Disclosure Control Methods for Anonymization of Data and Risk Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-VIM >= 4.7.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-prettydoc 
Requires:         R-CRAN-VIM >= 4.7.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-car 
Requires:         R-CRAN-carData 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-tools 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-prettydoc 

%description
Data from statistical agencies and other institutions are mostly
confidential. This package (see also Templ, Kowarik and Meindl (2017)
<doi:10.18637/jss.v067.i04>) can be used for the generation of anonymized
(micro)data, i.e. for the creation of public- and scientific-use files.
The theoretical basis for the methods implemented can be found in Templ
(2017) <doi:10.1007/978-3-319-50272-4>. Various risk estimation and
anonymisation methods are included. Note that the package includes a
graphical user interface (Meindl and Templ, 2019 <doi:10.3390/a12090191>)
that allows to use various methods of this package.

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
