%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leafareaR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Leaf Area Modeling, Evaluation, and Prediction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for leaf area estimation based on leaf length, leaf width, and
observed leaf area. The package supports data validation, predictor
generation, descriptive statistics, exploratory graphics, scatterplot
matrices, linear models, nonlinear models, mixed models, model evaluation,
ranking, equation generation, prediction, export of results and plots, and
an interactive 'shiny' application. Methods implemented in the package are
aligned with non-destructive allometric workflows described by Ribeiro et
al. (2024) <doi:10.1016/j.sajb.2024.07.006>, Ribeiro et al. (2023)
<doi:10.1590/1807-1929/agriambi.v27n3p209-215>, and Ribeiro et al. (2025)
<doi:10.1590/0103-8478cr20230550>.

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
