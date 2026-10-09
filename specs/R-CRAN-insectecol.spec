%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  insectecol
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Insect Ecology Data Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A collection of analytical tools for insect ecology research, currently
covering age-stage, two-sex life table analysis, dose-response bioassays,
temperature-dependent development and insect phenology prediction. The
life table module follows the age-stage, two-sex life table theory of Chi
(1988) <doi:10.1093/ee/17.1.26> and Chi et al. (2020)
<doi:10.1127/entomologia/2020/0936>. It supports fast batch processing of
multi-group datasets, validates raw 'csv' data, computes cohort size, mean
fecundity, age-stage survival rates, age-specific survival, age-specific
fecundity, life expectancy, and derived population parameters (net
reproductive rate, intrinsic and finite rates of increase, mean generation
time), simultaneously generates age-stage survival curves for all groups,
and exports all tabular results and plots to 'Excel' in a single run. The
bioassay module estimates lethal concentrations by the traditional and the
weighted (improved) linear regression methods and by probit analysis
(Bliss, 1934) <doi:10.1126/science.79.2037.38>, with the control-mortality
correction of Abbott (1925) <doi:10.1093/jee/18.2.265a>, 95%% confidence
intervals and chi-square goodness-of-fit tests; the lethal proportion can
be set freely (e.g., 25%%, 50%%, 70%% or 90%%), so any LC value such as the
LC25, LC70 or LC90 can be computed, not only the LC50. The regression
plots and tables are exported to 'Excel'. The degree-day module estimates
the developmental threshold temperature and the effective accumulated
temperature by the linear degree-day method (Campbell et al., 1974)
<doi:10.2307/2402197>, and fits the common nonlinear temperature-
dependent development models following Logan et al. (1976)
<doi:10.1093/ee/5.6.1133> (Logan-6), Lactin et al. (1995)
<doi:10.1093/ee/24.1.68> and Briere et al. (1999)
<doi:10.1093/ee/28.1.22>, plus a 7-parameter Wang model; it selects the
best model by AICc, predicts durations and accumulates field degree-days.
The emergence module applies the stage-grading method to a single survey
of the population stage structure, i.e. to stage-frequency data (Kiritani
and Nakasuji, 1967) <doi:10.1007/bf02514921> and Manly (1974)
<doi:10.1007/bf00345751>, and projects the beginning, peak and end of the
adult emergence period (the 16%%, 50%% and 84%% quantiles), optionally
shifting the eclosion dates by the pre-oviposition period and the egg
duration to forecast larval hatch. Further extensions, such as median
lethal temperature/time (LT50), are planned.

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
