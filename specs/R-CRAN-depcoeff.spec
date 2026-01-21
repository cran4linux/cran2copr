%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  depcoeff
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dependency Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-copula 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-copula 

%description
Functions to compute coefficients measuring the dependence of two or more
than two variables. The functions can be deployed to gain information
about functional dependencies of the variables with emphasis on monotone
functions. The statistics describe how well one response variable can be
approximated by a monotone function of other variables. In regression
analysis the variable selection is an important issue. In this framework
the functions could be useful tools in modeling the regression function.
Detailed explanations on the subject can be found in papers Liebscher
(2014) <doi:10.2478/demo-2014-0004>; Liebscher (2017)
<doi:10.1515/demo-2017-0012>; Liebscher (2021):
<https://arfjournals.com/image/catalog/Journals%%20Papers/AJSS/No%%202%%20(2021)/4-AJSS_123-150.pdf>;
Liebscher (2021): Kendall regression coefficient. Computational Statistics
and Data Analysis 157. 107140.

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
