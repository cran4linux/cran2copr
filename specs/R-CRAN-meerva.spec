%global packname  meerva
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
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
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
Analyze data with measurement error when there is a validation subsample
randomly selected from the full sample.  The method assumes surrogate
variables measured with error are available for the full sample, and
reference variables measured with little or no error are available for
this randomly selected subsample of the full sample.  Measurement errors
may be differential or non differential, in any or all predictors
(simultaneously) as well as outcome.  The "augmented" estimates derived
are based upon the multivariate correlation between regression model
parameter estimates for the reference variables and for the surrogate
variables in the validation subset.  Because the validation subsample is
chosen at random whatever biases are imposed by measurement error,
non-differential or differential, are reflected in this correlation and
can be used to derive estimates for the reference variables using data
from the whole sample.  The main functions in the package are meerva.fit
which calculates estimates for a dataset, and meerva.sim.block which
simulates multiple datasets as described by the user, and analyzes these
datasets, storing the regression coefficient estimates for inspection.
This work derives from Chen Y-H, Chen H. (2000)
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
