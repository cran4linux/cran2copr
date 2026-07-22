%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oalasso
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outcome-Adaptive Lasso Propensity Scores

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt >= 4.6.0
BuildRequires:    R-CRAN-glmnet >= 4.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-cobalt >= 4.6.0
Requires:         R-CRAN-glmnet >= 4.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Estimates propensity scores by the outcome-adaptive lasso of Shortreed and
Ertefaie (2017) <doi:10.1111/biom.12679> and the generalized
outcome-adaptive lasso (GOAL) of Balde, Yang and Lefebvre (2023)
<doi:10.1111/biom.13683>, using 'glmnet' with an exact penalty-scale
correction so that the published objectives and tuning grids are
reproduced. Tuning is by the weighted absolute mean difference balance
criterion. The resulting score is designed to be supplied directly to the
matchit() function of 'MatchIt' as a distance measure, to the weightit()
function of 'WeightIt' as a propensity score, or to the psave() function
of 'psAve' as an appended candidate.

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
