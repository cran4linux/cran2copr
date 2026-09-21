%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pilotr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Experimental and Behavioural Data from a Portable Design Specification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-stats 

%description
Generative simulation of experimental and behavioural data sets from a
portable JavaScript Object Notation (JSON) design specification shared
with the 'Python' package of the same name. Supports user-specified fixed
effect sizes, crossed by-subject and by-item random intercepts and slopes,
predictors measured with error, realistic response families (Gaussian,
lognormal, shifted lognormal, ex-Gaussian, Bernoulli, Poisson, ordinal and
Beta), and simulation-based power and precision-based design analysis,
including the Type S and Type M errors of Gelman and Carlin (2014)
<doi:10.1177/1745691614551642> and a region of practical equivalence. A
shared cross-language random-number generator means that, given the same
specification and seed, the R and 'Python' implementations produce
identical data: exactly for the Gaussian family and for any family with
rounding set, and to within the last unit in the last place for families
applying a transcendental function to the linear predictor, whose rounding
the IEEE-754 standard does not fix.

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
