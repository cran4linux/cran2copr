%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semEffect
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Equation Model Effect Analysis and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-piecewiseSEM 
BuildRequires:    R-CRAN-plspm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-piecewiseSEM 
Requires:         R-CRAN-plspm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-RColorBrewer 

%description
Provides standardized effect decomposition (direct, indirect, and total
effects) for three major structural equation modeling frameworks:
'lavaan', 'piecewiseSEM', and 'plspm'. Automatically handles zero-effect
variables, generates publication-ready 'ggplot2' visualizations, and
returns both wide-format and long-format effect tables. Supports effect
filtering, multi-model object inputs, and customizable visualization
parameters. For a general overview of the methods used in this package,
see Rosseel (2012) <doi:10.18637/jss.v048.i02> and Lefcheck (2016)
<doi:10.1111/2041-210X.12512>.

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
