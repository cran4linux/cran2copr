%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  POEMED
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Enhancement for High-Dimensional Mediation Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 3.0.3
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-withr >= 3.0.3
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-CRAN-ncvreg 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides powerful global tests for high-dimensional mediation analysis
with heterogeneous (and even contrasting) mediation effects, for
continuous, binary, and count outcomes. The power enhancement (PE) idea
augments a Wald test on the total indirect effect with a component that
captures marginal signals from individual mediators, so that active
mediators are detected even when their individual indirect effects cancel
and the total indirect effect is zero. The package also identifies which
individual mediators are active with familywise error rate or false
discovery rate control. The methods implement Yu and Kelley (in press),
"Power Enhancement in High-Dimensional Heterogeneous Mediation Analysis"
(Journal of the American Statistical Association); the package also
simulates mediation data under the homogeneous, heterogeneous, and
contrasting patterns that the article studies, ships its empirical
health-expenditure data as a benchmark and reruns that empirical analysis,
and runs the designs of its Monte Carlo size and power studies. The name,
'POEMED', from POwer-Enhanced MEDiation, encodes the method. Every
estimation and testing function returns a tidy 'data.frame' that prints
with sensible rounding and composes with the broader R ecosystem.

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
