%global __brp_check_rpaths %{nil}
%global packname  optedr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Optimal and D-Augmented Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-orthopolynom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyalert 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-orthopolynom 

%description
Calculates D-, Ds-, A- and I-optimal designs for non-linear models, via an
implementation of the cocktail algorithm (Yu, 2011,
<doi:10.1007/s11222-010-9183-2>). Compares designs via their efficiency,
and D-augments any design with a controlled efficiency. An efficient
rounding function has been provided to transform approximate designs to
exact designs.

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
