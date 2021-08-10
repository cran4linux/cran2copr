%global __brp_check_rpaths %{nil}
%global packname  precautionary
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Safety Diagnostics for Dose-Escalation Trial Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-escalation 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-CRAN-BOIN 
BuildRequires:    R-CRAN-parallelly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-escalation 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-dfcrm 
Requires:         R-CRAN-BOIN 
Requires:         R-CRAN-parallelly 

%description
Enhances various R packages that support the design and simulation of
phase 1 dose-escalation trials, adding diagnostics to examine the safety
characteristics of these designs in light of expected inter-individual
variation in pharmacokinetics and pharmacodynamics. See Norris (2020b),
"Retrospective analysis of a fatal dose-finding trial" <arXiv:2004.12755>
and (2020c) "What Were They Thinking? Pharmacologic priors implicit in a
choice of 3+3 dose-escalation design" <arXiv:2012.05301>.

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
