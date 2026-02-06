%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adjustedCurves
%global packver   0.11.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.4
Release:          1%{?dist}%{?buildtag}
Summary:          Confounder-Adjusted Survival Curves and Cumulative Incidence Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-survival >= 3.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlang 

%description
Estimate and plot confounder-adjusted survival curves using either 'Direct
Adjustment', 'Direct Adjustment with Pseudo-Values', various forms of
'Inverse Probability of Treatment Weighting', two forms of 'Augmented
Inverse Probability of Treatment Weighting', 'Empirical Likelihood
Estimation' or 'Targeted Maximum Likelihood Estimation'. Also includes a
significance test for the difference between two adjusted survival curves
and the calculation of adjusted restricted mean survival times.
Additionally enables the user to estimate and plot cause-specific
confounder-adjusted cumulative incidence functions in the competing risks
setting using the same methods (with some exceptions). For details, see
Denz et. al (2023) <doi:10.1002/sim.9681>.

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
