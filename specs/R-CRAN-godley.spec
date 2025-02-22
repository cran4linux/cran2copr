%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  godley
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stock-Flow-Consistent Model Simulator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-vecsets 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-vecsets 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-visNetwork 

%description
Define, simulate, and validate stock-flow consistent (SFC) macroeconomic
models. The godley R package offers tools to dynamically define model
structures by adding variables and specifying governing systems of
equations. With it, users can analyze how different macroeconomic
structures affect key variables, perform parameter sensitivity analyses,
introduce policy shocks, and visualize resulting economic scenarios. The
accounting structure of SFC models follows the approach outlined in the
seminal study by Godley and Lavoie Godley and Lavoie (2007,
ISBN:978-1-137-08599-3), ensuring a comprehensive integration of all
economic flows and stocks. The algorithms implemented to solve the models
are based on methodologies from Kinsella and O'Shea (2010)
<doi:10.2139/ssrn.1729205>, Peressini and Sullivan (1988,
ISBN:0-387-96614-5), and contributions by Joao Macalos.

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
