%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  projoint
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conjoint Analysis with Reliability Correction and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-estimatr 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-estimatr 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-scales 

%description
Provides tools for analyzing data generated from conjoint survey
experiments, a method widely used in the social sciences for studying
multidimensional preferences. The package implements estimation of
marginal means (MMs) and average marginal component effects (AMCEs), with
corrections for measurement error. Methods include profile-level and
choice-level estimators, bias correction using intra-respondent
reliability (IRR), and visualization utilities. For details on the
methodology, see Clayton, Horiuchi, Kaufman, King, and Komisarchik (2025)
<https://gking.harvard.edu/conjointE>.

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
