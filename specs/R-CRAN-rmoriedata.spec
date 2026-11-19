%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmoriedata
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Disclosure Control for Aggregate Releases with Open Datasets

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-rmoriebricklayer >= 1.1.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rmoriebricklayer >= 1.1.0
Requires:         R-stats 
Requires:         R-utils 

%description
Disclosure-control tools for releasing aggregate statistics, with open
datasets to use them on. Differential privacy: an exact discrete Laplace
sampler for counts and the analytic Gaussian mechanism for means, drawing
on the operating system's random source, with privacy-budget accounting.
Checks of k-anonymity and l-diversity, and cell suppression audited for
exact recovery from the margins. The datasets are snapshots of publicly
available tables from open-data portals built on the Comprehensive
Knowledge Archive Network ('CKAN', <https://ckan.org/>), 'Socrata'
(<https://dev.socrata.com/>), and 'Opendatasoft'
(<https://www.huwise.com/>) (Chicago, New York City, Toronto, Vancouver,
and others), Statistics Canada Canadian Centre for Justice and Community
Safety Statistics ('CCJS') tables, a multi-agent-reviewed corpus of
Ontario Special Investigations Unit ('SIU', <https://www.siu.on.ca/>)
director's reports, and synthetic fixtures, with functions that read and
verify them.

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
