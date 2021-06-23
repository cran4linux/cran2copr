%global __brp_check_rpaths %{nil}
%global packname  ergMargins
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Process Analysis for Exponential Random Graph Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-statnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-btergm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-xergm.common 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-statnet 
Requires:         R-stats 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-network 
Requires:         R-CRAN-btergm 
Requires:         R-methods 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-xergm.common 

%description
Calculates marginal effects and conducts process analysis in exponential
family random graph models (ERGM). Includes functions to conduct mediation
and moderation analyses and to diagnose multicollinearity. URL:
<https://github.com/sduxbury/ergMargins>. BugReports:
<https://github.com/sduxbury/ergMargins/issues>. Duxbury, Scott W (2021)
<doi:10.1177/0049124120986178>. Long, J. Scott, and Sarah Mustillo (2018)
<doi:10.1177/0049124118799374>. Mize, Trenton D. (2019)
<doi:10.15195/v6.a4>. Karlson, Kristian Bernt, Anders Holm, and Richard
Breen (2012) <doi:10.1177/0081175012444861>. Duxbury, Scott W (2018)
<doi:10.1177/0049124118782543>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
