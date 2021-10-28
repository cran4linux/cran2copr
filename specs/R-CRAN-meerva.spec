%global __brp_check_rpaths %{nil}
%global packname  meerva
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Data with Measurement Error Using a Validation Subsample

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 

%description
Sometimes data for analysis are obtained using more convenient or less
expensive means yielding "surrogate" variables for what could be obtained
more accurately, albeit with less convenience; or less conveniently or at
more expense yielding "reference" variables, thought of as being measured
without error. Analysis of the surrogate variables measured with error
generally yields biased estimates when the objective is to make inference
about the reference variables. Often it is thought that ignoring the
measurement error in surrogate variables only biases effects toward the
null hypothesis, but this need not be the case. Measurement errors may
bias parameter estimates either toward or away from the null hypothesis.
If one has a data set with surrogate variable data from the full sample,
and also reference variable data from a randomly selected subsample, then
one can assess the bias introduced by measurement error in parameter
estimation, and use this information to derive improved estimates based
upon all available data. Formulaically these estimates based upon the
reference variables from the validation subsample combined with the
surrogate variables from the whole sample can be interpreted as starting
with the estimate from reference variables in the validation subsample,
and "augmenting" this with additional information from the surrogate
variables. This suggests the term "augmented" estimate.  The meerva
package calculates these augmented estimates in the regression setting
when there is a randomly selected subsample with both surrogate and
reference variables. Measurement errors may be differential or
non-differential, in any or all predictors (simultaneously) as well as
outcome. The augmented estimates derive, in part, from the multivariate
correlation between regression model parameter estimates from the
reference variables and the surrogate variables, both from the validation
subset. Because the validation subsample is chosen at random any biases
imposed by measurement error, whether non-differential or differential,
are reflected in this correlation and these correlations can be used to
derive estimates for the reference variables using data from the whole
sample.  The main functions in the package are meerva.fit which calculates
estimates for a dataset, and meerva.sim.block which simulates multiple
datasets as described by the user, and analyzes these datasets, storing
the regression coefficient estimates for inspection.  The augmented
estimates, as well as how measurement error may arise in practice, is
described in more detail by Kremers WK (2021) <arXiv:2106.14063> and is an
extension of the works by Chen Y-H, Chen H. (2000)
<doi:10.1111/1467-9868.00243>, Chen Y-H. (2002)
<doi:10.1111/1467-9868.00324>, Wang X, Wang Q (2015)
<doi:10.1016/j.jmva.2015.05.017> and Tong J, Huang J, Chubak J, et al.
(2020) <doi:10.1093/jamia/ocz180>.

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
