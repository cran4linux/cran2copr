%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmdl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Language to Manage Many Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-janitor 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-janitor 

%description
A system for describing and manipulating the many models that are
generated in causal inference and data analysis projects, as based on the
causal theory and criteria of Austin Bradford Hill (1965)
<doi:10.1177/003591576505800503>. This system includes the addition of
formal attributes that modify base `R` objects, including terms and
formulas, with a focus on variable roles in the "do-calculus" of modeling,
as described in Pearl (2010) <doi:10.2202/1557-4679.1203>. For example,
the definition of exposure, outcome, and interaction are implicit in the
roles variables take in a formula. These premises allow for a more fluent
modeling approach focusing on variable relationships, and assessing effect
modification, as described by VanderWeele and Robins (2007)
<doi:10.1097/EDE.0b013e318127181b>. The essential goal is to help
contextualize formulas and models in causality-oriented workflows.

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
