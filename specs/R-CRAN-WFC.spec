%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WFC
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Workflow-Oriented Survey Weight Calibration

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a disciplined precheck, execution, and diagnostics workflow for
survey weighting and raking. Weight construction requires design-only
data, a verified external target, outcome-blind planning, and human
approval before weight locking, with bilingual reports for decision and
statistical audiences. Converts calibrated and replicate weights into
standard survey designs, provides optional broom-style result projections,
and records serializable production pipeline provenance. Supports fixed,
predeclared soft calibration tolerances and categorical entropy balancing
from verified margins, plus panel attrition weighting, high-influence unit
diagnostics, Fay's balanced repeated replication, and opt-in parallel
execution for long runs. Calibration methods follow Deville and Saerndal
(1992) <doi:10.1080/01621459.1992.10475217>, and entropy balancing follows
Hainmueller (2012) <doi:10.1093/pan/mpr025>.

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
