%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DEA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Envelopment Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Nonparametric efficiency measurement by data envelopment analysis.
Provides radial (Charnes-Cooper-Rhodes and Banker-Charnes-Cooper)
technical efficiency under constant, variable, non-increasing and
non-decreasing returns to scale, the slacks-based measure of Tone (2001),
the additive model of Charnes and others (1985), and the directional
distance function of Chambers, Chung and Fare (1996), all through one
interface and one result object.  Efficiency estimates are accompanied by
peers, slacks, returns-to-scale classification, scale efficiency and the
optimal multipliers, and by bias-corrected estimates and confidence
intervals from the smoothed homogeneous bootstrap of Simar and Wilson
(1998).  Where prices are known, cost, revenue and Nerlovian profit
efficiency separate the technical component from the allocative one; where
they are not, cross-efficiency with the secondary goals of Doyle and Green
(1994) ranks units that a self-appraisal leaves tied.  This package
succeeds the archived 'DEA' package of Diaz-Martinez and
Fernandez-Menendez (2008).

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
