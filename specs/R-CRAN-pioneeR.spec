%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pioneeR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Productivity and Efficiency Analysis using DEA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI >= 5.5.2
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-haven >= 2.5.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-bslib >= 0.6.0
BuildRequires:    R-CRAN-reactable >= 0.4.0
BuildRequires:    R-CRAN-bsicons 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-writexl 
Requires:         R-CRAN-lpSolveAPI >= 5.5.2
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-haven >= 2.5.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-bslib >= 0.6.0
Requires:         R-CRAN-reactable >= 0.4.0
Requires:         R-CRAN-bsicons 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-writexl 

%description
Measure productivity and efficiency using Data Envelopment Analysis (DEA).
Available methods include DEA under different technology assumptions,
bootstrapping of efficiency scores and calculation of the Malmquist
productivity index. Analyses can be performed either in the console or
with the provided 'shiny' app. See Banker, R.; Charnes, A.; Cooper, W.W.
(1984) <doi:10.1287/mnsc.30.9.1078>, Färe, R.; Grosskopf, S. (1996)
<doi:10.1007/978-94-009-1816-0>.

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
