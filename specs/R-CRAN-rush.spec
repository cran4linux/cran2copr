%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rush
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid Asynchronous and Distributed Computing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mirai >= 2.5.0
BuildRequires:    R-CRAN-lgr >= 0.5.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ids 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-redux 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-mirai >= 2.5.0
Requires:         R-CRAN-lgr >= 0.5.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ids 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-mlr3misc 
Requires:         R-parallel 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-redux 
Requires:         R-CRAN-uuid 

%description
Package to tackle large-scale problems asynchronously across a distributed
network. Employing a database centric model, rush enables workers to
communicate tasks and their results over a shared 'Redis' database. Key
features include low task overhead, efficient caching, and robust error
handling. The package powers the asynchronous optimization algorithms in
the 'bbotk' and 'mlr3tuning' packages.

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
