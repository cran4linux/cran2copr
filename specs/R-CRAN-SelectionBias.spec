%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SelectionBias
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Bounds for the Selection Bias for Binary Treatment and Outcome Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 

%description
Computes bounds and sensitivity parameters as part of sensitivity analysis
for selection bias. Different bounds are provided: the SV (Smith and
VanderWeele), sharp bounds, AF (assumption-free) bound, GAF (generalized
AF), and CAF (counterfactual AF) bounds. The calculation of the
sensitivity parameters for the SV, sharp, and GAF bounds assume an
additional dependence structure in form of a generalized M-structure. The
bounds can be calculated for any structure as long as the necessary
assumptions hold. See Smith and VanderWeele (2019)
<doi:10.1097/EDE.0000000000001032>, Zetterstrom, Sjölander, and Waernabum
(2025) <doi:10.1177/09622802251374168>, Zetterstrom and Waernbaum (2022)
<doi:10.1515/em-2022-0108>, and Zetterstrom (2024)
<doi:10.1515/em-2023-0033>.

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
