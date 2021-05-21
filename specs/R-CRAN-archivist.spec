%global packname  archivist
%global packver   2.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Storing, Restoring and Searching for R Objects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-flock 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-flock 

%description
Data exploration and modelling is a process in which a lot of data
artifacts are produced. Artifacts like: subsets, data aggregates, plots,
statistical models, different versions of data sets and different versions
of results. The more projects we work with the more artifacts are produced
and the harder it is to manage these artifacts. Archivist helps to store
and manage artifacts created in R. Archivist allows you to store selected
artifacts as a binary files together with their metadata and relations.
Archivist allows to share artifacts with others, either through shared
folder or github. Archivist allows to look for already created artifacts
by using it's class, name, date of the creation or other properties. Makes
it easy to restore such artifacts. Archivist allows to check if new
artifact is the exact copy that was produced some time ago. That might be
useful either for testing or caching.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
