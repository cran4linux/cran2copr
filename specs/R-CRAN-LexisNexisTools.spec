%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LexisNexisTools
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Working with Files from 'LexisNexis'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.0
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-utils >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 1.4.0
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-CRAN-quanteda >= 1.1.0
BuildRequires:    R-CRAN-stringdist >= 0.9.4.0
BuildRequires:    R-CRAN-quanteda.textstats 
Requires:         R-methods >= 3.3.0
Requires:         R-parallel >= 3.3.0
Requires:         R-stats >= 3.3.0
Requires:         R-utils >= 3.3.0
Requires:         R-CRAN-tibble >= 1.4.0
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-CRAN-quanteda >= 1.1.0
Requires:         R-CRAN-stringdist >= 0.9.4.0
Requires:         R-CRAN-quanteda.textstats 

%description
My PhD supervisor once told me that everyone doing newspaper analysis
starts by writing code to read in files from the 'LexisNexis' newspaper
archive (retrieved e.g., from <https://www.lexisnexis.com/> or any of the
partner sites). However, while this is a nice exercise I do recommend, not
everyone has the time. This package takes files downloaded from the
newspaper archive of 'LexisNexis', reads them into R and offers functions
for further processing.

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
