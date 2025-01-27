%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ABM
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Agent Based Model Simulation Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 

%description
A high-performance, flexible and extensible framework to develop
continuous-time agent based models. Its high performance allows it to
simulate millions of agents efficiently. Agents are defined by their
states (arbitrary R lists). The events are handled in chronological order.
This avoids the multi-event interaction problem in a time step of
discrete-time simulations, and gives precise outcomes. The states are
modified by provided or user-defined events. The framework provides a
flexible and customizable implementation of state transitions (either
spontaneous or caused by agent interactions), making the framework
suitable to apply to epidemiology and ecology, e.g., to model life history
stages, competition and cooperation, and disease and information spread.
The agent interactions are flexible and extensible. The framework provides
random mixing and network interactions, and supports multi-level mixing
patterns.  It can be easily extended to other interactions such as inter-
and intra-households (or workplaces and schools) by subclassing an R6
class. It can be used to study the effect of age-specific, group-specific,
and contact- specific intervention strategies, and complex interactions
between individual behavior and population dynamics. This modeling concept
can also be used in business, economical and political models. As a
generic event based framework, it can be applied to many other fields.
More information about the implementation and examples can be found at
<https://github.com/junlingm/ABM>.

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
