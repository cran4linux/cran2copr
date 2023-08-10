%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PWEALL
%global packver   1.3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Monitoring of Survival Trials Accounting for Complex Situations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
Calculates various functions needed for design and monitoring survival
trials accounting for complex situations such as delayed treatment effect,
treatment crossover, non-uniform accrual, and different censoring
distributions between groups. The event time distribution is assumed to be
piecewise exponential (PWE) distribution and the entry time is assumed to
be piecewise uniform distribution. As compared with Version 1.2.1, two
more types of hybrid crossover are added. A bug is corrected in the
function "pwecx" that calculates the crossover-adjusted survival,
distribution, density, hazard and cumulative hazard functions. Also, to
generate the crossover-adjusted event time random variable, a more
efficient algorithm is used and the output includes crossover indicators.

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
