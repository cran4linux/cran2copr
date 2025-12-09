%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  abess
%global packver   0.4.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.11
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Best Subset Selection

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 

%description
Extremely efficient toolkit for solving the best subset selection problem
<https://www.jmlr.org/papers/v23/21-1060.html>. This package is its R
interface. The package implements and generalizes algorithms designed in
<doi:10.1073/pnas.2014241117> that exploits a novel
sequencing-and-splicing technique to guarantee exact support recovery and
globally optimal solution in polynomial times for linear model. It also
supports best subset selection for logistic regression, Poisson
regression, Cox proportional hazard model, Gamma regression,
multiple-response regression, multinomial logistic regression, ordinal
regression, Ising model reconstruction
<doi:10.1080/01621459.2025.2571245>, (sequential) principal component
analysis, and robust principal component analysis. The other valuable
features such as the best subset of group selection
<doi:10.1287/ijoc.2022.1241> and sure independence screening
<doi:10.1111/j.1467-9868.2008.00674.x> are also provided.

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
