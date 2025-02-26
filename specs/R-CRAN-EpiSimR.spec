%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpiSimR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Shiny' App to Simulate the Dynamics of Epidemic and Endemic Diseases Spread

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.1
Requires:         R-core >= 4.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.8
BuildRequires:    R-CRAN-deSolve >= 1.40
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinythemes 
Requires:         R-CRAN-openxlsx >= 4.2.8
Requires:         R-CRAN-deSolve >= 1.40
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinythemes 

%description
The 'EpiSimR' package provides an interactive 'shiny' app based on
deterministic compartmental mathematical modeling for simulating and
visualizing the dynamics of epidemic and endemic disease spread. It allows
users to explore various intervention strategies, including vaccination
and isolation, by adjusting key epidemiological parameters. The
methodology follows the approach described by Brauer (2008)
<doi:10.1007/978-3-540-78911-6_2>. Thanks to 'shiny' package.

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
