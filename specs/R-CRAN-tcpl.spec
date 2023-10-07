%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tcpl
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          ToxCast Data Analysis Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.4
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
Requires:         R-CRAN-data.table >= 1.9.4
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

%description
A set of tools for processing and modeling high-throughput and
high-content chemical screening data. The package was developed for the
the chemical screening data generated by the US EPA ToxCast program, but
can be used for diverse chemical screening efforts.

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
