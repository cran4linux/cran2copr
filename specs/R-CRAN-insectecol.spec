%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  insectecol
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
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
Requires:         R-CRAN-readr 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A collection of analytical tools for insect ecology research, currently
covering age-stage, two-sex life table analysis and dose-response
bioassays. The life table module supports fast batch processing of
multi-group datasets, validates raw 'csv' data, computes cohort size, mean
fecundity, age-stage survival rates, age-specific survival, age-specific
fecundity, life expectancy, and derived population parameters (net
reproductive rate, intrinsic and finite rates of increase, mean generation
time), simultaneously generates age-stage survival curves for all groups,
and exports all tabular results and plots to 'Excel' in a single run. The
bioassay module estimates lethal concentrations by the traditional and the
weighted (improved) linear regression methods and by probit analysis, with
Abbott correction, 95%% confidence intervals and chi-square goodness-of-fit
tests; the lethal proportion can be set freely (e.g., 25%%, 50%%, 70%% or
90%%), so any LC value such as the LC25, LC70 or LC90 can be computed, not
only the LC50. The regression plots and tables are exported to 'Excel'.
Planned extensions include more insect ecology indicators, such as median
lethal temperature/time (LT50) and thermal constants (effective
accumulated temperature).

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
