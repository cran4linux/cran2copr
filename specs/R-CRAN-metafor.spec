%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metafor
%global packver   3.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis Package for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-metadat 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-metadat 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-pbapply 

%description
A comprehensive collection of functions for conducting meta-analyses in R.
The package includes functions to calculate various effect sizes or
outcome measures, fit equal-, fixed-, random-, and mixed-effects models to
such data, carry out moderator and meta-regression analyses, and create
various types of meta-analytical plots (e.g., forest, funnel, radial,
L'Abbe, Baujat, bubble, and GOSH plots). For meta-analyses of binomial and
person-time data, the package also provides functions that implement
specialized methods, including the Mantel-Haenszel method, Peto's method,
and a variety of suitable generalized linear (mixed-effects) models (i.e.,
mixed-effects logistic and Poisson regression models). Finally, the
package provides functionality for fitting meta-analytic
multivariate/multilevel models that account for non-independent sampling
errors and/or true effects (e.g., due to the inclusion of multiple
treatment studies, multiple endpoints, or other forms of clustering).
Network meta-analyses and meta-analyses accounting for known correlation
structures (e.g., due to phylogenetic relatedness) can also be conducted.
An introduction to the package can be found in Viechtbauer (2010)
<doi:10.18637/jss.v036.i03>.

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
