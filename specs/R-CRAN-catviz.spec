%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  catviz
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Causal Assignment Trees for CSDiD and DR-DDD Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-grid 
Requires:         R-CRAN-rlang 

%description
Tools for constructing, labeling, and visualizing Causal Assignment Trees
(CATs) in settings with staggered adoption. Supports Callaway and
Sant'Anna difference-in-differences (CSDiD) and doubly robust
difference-in-difference-differences (DR-DDD) designs. The package helps
clarify treatment timing, never-treated vs. not-yet-treated composition,
and subgroup structure, and produces publication-quality diagrams and
summary tables. Current functionality focuses on data-to-node mapping,
node counts, cohort-year summaries, and high-quality tree plots suitable
for empirical applications prior to estimation. Methods are based on
Callaway and Sant'Anna (2021) <doi:10.1016/j.jeconom.2020.12.001>,
Sant'Anna and Zhao (2020) <doi:10.1016/j.jeconom.2020.06.003>, and Kilanko
(2026) <https://github.com/VictorKilanko/catviz>.

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
