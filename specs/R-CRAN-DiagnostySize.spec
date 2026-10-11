%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiagnostySize
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          App for Calculating the Sample Size in a Diagnostic Study

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-htmltools 
Requires:         R-stats 

%description
We developed a 'shiny' app for the optimal sample size calculations for
diagnostic accuracy studies proposed in Stark and Zapf (2020)
<doi:10.1177/0962280220913588>, and Stark et al. (2022)
<doi:10.1186/s12874-022-01564-2>, so people without programming skills can
use this approach as well. Until now, this approach was just available via
'R' scripts. This app, 'DiagnostySize', lets users apply the optimal
sample size calculation approach, ensuring that no endpoint (sensitivity
or specificity) is overpowered. Within the app, users can run the optimal
sample size and power calculations for different study designs through a
user interface.

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
