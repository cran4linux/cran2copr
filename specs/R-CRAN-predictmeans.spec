%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predictmeans
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predicted Means for Linear and Semiparametric Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-glmmTMB 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Predicted means, standard errors, contrasts, multiple comparisons,
permutation and bootstrap tests, R-squared and diagnostics for models
fitted by 'aov', 'lm', 'glm', 'gls', 'lme', 'lmer', 'glmer', 'glmmTMB',
'gam' and 'semireg'. Defaults are chosen on evidence: Kenward-Roger
degrees of freedom and adjusted standard errors for REML 'lmer' fits
(Kenward and Roger (1997) <doi:10.2307/2533558>), permutation p-values
(b+1)/(B+1), stratum standard errors for 'aov' models with Error() terms
as in 'Genstat', and equal-weight means over observed cells with a
warning. Results are tested against 'SAS' PROC MIXED and 'Genstat' output
and the 'pbkrtest', 'nlme' and 'emmeans' packages. Functions stop with a
message rather than return a wrong result, give one-line advice triggered
by the data, and give the same resampling results for any number of cores.

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
