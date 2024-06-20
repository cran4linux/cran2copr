%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doublIn
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Incubation or Latency Time using Doubly Interval Censored Observations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-epicontacts 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mStats 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-epicontacts 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mStats 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 

%description
Visualize contact tracing data using a 'shiny' app and estimate the
incubation or latency time of an infectious disease respecting the
following characteristics in the analysis; (i) doubly interval censoring
with (partly) overlapping or distinct windows; (ii) an infection risk
corresponding to exponential growth; (iii) right truncation allowing for
individual truncation times; (iv) different choices concerning the family
of the distribution. For our earlier work, we refer to Arntzen et al.
(2023) <doi:10.1002/sim.9726>. A paper describing our approach in detail
will follow.

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
