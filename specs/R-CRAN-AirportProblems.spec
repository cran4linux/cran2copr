%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AirportProblems
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Cost Allocation for Airport Problems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 
Requires:         R-stats 
Requires:         R-utils 

%description
Airport problems, introduced by Littlechild and Owen (1973)
<https://www.jstor.org/stable/2629727>, are cost allocation problems where
agents share the cost of a facility (or service) based on their ordered
needs. Valid allocations must satisfy no-subsidy constraints, meaning that
no group of agents contributes more than the highest cost of its members
(i.e., no agent is allowed to subsidize another). A rule is a mechanism
that selects an allocation vector for a given problem. This package
computes several rules proposed in the literature, including both standard
rules and their variants, such as weighted versions, rules for clones, and
rules based on the agents’ hierarchy order. These rules can be applied to
various problems of interest, including the allocation of liabilities and
the maintenance of irrigation systems, among others. Moreover, the package
provides functions for graphical representation, enabling users to
visually compare the outcomes produced by each rule, or to display the
no-subsidy set. In addition, it includes four datasets illustrating
different applications and examples of airport problems. For a more
detailed explanation of all concepts, see Thomson (2024)
<doi:10.1016/j.mathsocsci.2024.03.007>.

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
