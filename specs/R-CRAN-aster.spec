%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aster
%global packver   1.3-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Aster Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trust 
Requires:         R-stats 
Requires:         R-CRAN-trust 

%description
Aster models (Geyer, Wagenius, and Shaw, 2007,
<doi:10.1093/biomet/asm030>; Shaw, Geyer, Wagenius, Hangelbroek, and
Etterson, 2008, <doi:10.1086/588063>; Geyer, Ridley, Latta, Etterson, and
Shaw, 2013, <doi:10.1214/13-AOAS653>) are exponential family regression
models for life history analysis.  They are like generalized linear models
except that elements of the response vector can have different families
(e. g., some Bernoulli, some Poisson, some zero-truncated Poisson, some
normal) and can be dependent, the dependence indicated by a graphical
structure. Discrete time survival analysis, life table analysis,
zero-inflated Poisson regression, and generalized linear models that are
exponential family (e. g., logistic regression and Poisson regression with
log link) are special cases. Main use is for data in which there is
survival over discrete time periods and there is additional data about
what happens conditional on survival (e. g., number of offspring).  Uses
the exponential family canonical parameterization (aster transform of
usual parameterization). There are also random effects versions of these
models.

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
