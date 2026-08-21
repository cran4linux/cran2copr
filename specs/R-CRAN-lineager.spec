%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lineager
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Row-Level Data Provenance and Exclusion Tracking

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.1.0

%description
Provides row-level data provenance tracking for analytical pipelines. Tags
datasets with unique lineage identifiers that persist through filter,
join, and derive operations. Requires documented reasons for every row
exclusion, capturing who was removed, why, and at which pipeline stage.
Variable derivations are registered as structured specifications linking
output variables back to their source. Any row in any downstream dataset
can be traced back to its origin via lg_trace(). Generates structured HTML
provenance reports suitable for regulatory submissions, internal audit, or
analytical documentation. General-purpose: works for clinical data,
machine learning pipelines, financial modelling, epidemiology, or any
workflow where row-level accountability matters. Optional features support
pharmaceutical users including population flag definitions,
source-to-analysis variable mapping, and Reviewer's Guide-aligned report
output. Complements the 'regulog' package for tamper-evident session-level
audit logging. For more details see <https://reprostats.org/lineager/>.

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
