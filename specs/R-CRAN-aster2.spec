%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aster2
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Aster Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
Aster models are exponential family regression models for life history
analysis.  They are like generalized linear models except that elements of
the response vector can have different families (e. g., some Bernoulli,
some Poisson, some zero-truncated Poisson, some normal) and can be
dependent, the dependence indicated by a graphical structure. Discrete
time survival analysis, zero-inflated Poisson regression, and generalized
linear models that are exponential family (e. g., logistic regression and
Poisson regression with log link) are special cases. Main use is for data
in which there is survival over discrete time periods and there is
additional data about what happens conditional on survival (e. g., number
of offspring).  Uses the exponential family canonical parameterization
(aster transform of usual parameterization). Unlike the aster package,
this package does dependence groups (nodes of the graph need not be
conditionally independent given their predecessor node), including
multinomial and two-parameter normal as families.  Thus this package also
generalizes mark-capture-recapture analysis.

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
