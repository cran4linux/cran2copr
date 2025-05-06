%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tcpl
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          ToxCast Data Analysis Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-ctxR >= 1.1.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RMariaDB 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tcplfit2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-gt 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-ctxR >= 1.1.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RMariaDB 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tcplfit2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-gt 

%description
The ToxCast Data Analysis Pipeline ('tcpl') is an R package that manages,
curve-fits, plots, and stores ToxCast data to populate its linked MySQL
database, 'invitrodb'. The package was developed for the chemical
screening data curated by the US EPA's Toxicity Forecaster (ToxCast)
program, but 'tcpl' can be used to support diverse chemical screening
efforts.

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
