%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gosset
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Data Analysis in Experimental Agriculture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-PlackettLuce 
BuildRequires:    R-CRAN-psychotools 
BuildRequires:    R-CRAN-qvcalc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-methods 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-PlackettLuce 
Requires:         R-CRAN-psychotools 
Requires:         R-CRAN-qvcalc 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-patchwork 
Requires:         R-parallel 

%description
Methods to analyse experimental agriculture data, from data synthesis to
model selection and visualisation, with a focus on ranking data from
decentralised on-farm trials with the 'tricot' approach (van Etten et al.
2019 <doi:10.1017/S0014479716000739>). Includes tools to build rankings,
fit and cross-validate Plackett-Luce models and trees, compare traits with
Kendall's tau, and summarise results as worth, regret and preference
indices. The package is named after W.S. Gosset aka 'Student', a pioneer
of modern statistics in small sample experimental design and analysis.

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
