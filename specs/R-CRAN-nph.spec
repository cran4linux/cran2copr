%global __brp_check_rpaths %{nil}
%global packname  nph
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Planning and Analysing Survival Studies under Non-Proportional Hazards

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-muhaz 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-muhaz 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-multcomp 

%description
Piecewise constant hazard functions are used to flexibly model survival
distributions with non-proportional hazards and to simulate data from the
specified distributions. A function to calculate weighted log-rank tests
for the comparison of two hazard functions is included. Also, a function
to calculate a test using the maximum of a set of test statistics from
weighted log-rank tests (MaxCombo test) is provided. This test utilizes
the asymptotic multivariate normal joint distribution of the separate test
statistics. The correlation is estimated from the data. These methods are
described in Ristl et al. (2021) <doi:10.1002/pst.2062>. Finally, a
function is provided for the estimation and inferential statistics of
various parameters that quantify the difference between two survival
curves. Eligible parameters are differences in survival probabilities, log
survival probabilities, complementary log log (cloglog) transformed
survival probabilities, quantiles of the survival functions, log
transformed quantiles, restricted mean survival times, as well as an
average hazard ratio, the Cox model score statistic (logrank statistic),
and the Cox-model hazard ratio. Adjustments for multiple testing and
simultaneous confidence intervals are calculated using a multivariate
normal approximation to the set of selected parameters.

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
