%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eq5d
%global packver   0.17.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Analysing 'EQ-5D' Data and Calculating 'EQ-5D' Index Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 

%description
EQ-5D is a widely used health-related quality-of-life instrument developed
by the EuroQol Group and used in the clinical and economic evaluation of
health care. Health is described using five dimensions (mobility,
self-care, usual activities, pain/discomfort, and anxiety/depression)
rated on either a three-level (EQ-5D-3L and EQ-5D-Y-3L) or five-level
(EQ-5D-5L) scale. Responses can be reported as EQ-5D health states or
converted to utility index scores using country-specific value sets. The
package provides methods for the valuation, reporting and analysis of
EQ-5D data. Utility index scores can be calculated for EQ-5D-3L, EQ-5D-5L
and EQ-5D-Y-3L data using a wide range of value sets and mapping
approaches. Functionality is also provided for descriptive-system
reporting, severity and distributional summaries, informativity measures,
health-state distribution analysis, longitudinal change analysis,
probability of superiority analysis and Health Profile Grid visualisation.
Methods described in Devlin et al. (2020) <doi:10.1007/978-3-030-47622-9>
are implemented where appropriate. A companion 'Shiny' application is
included for interactive analysis and visualisation of EQ-5D datasets.

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
