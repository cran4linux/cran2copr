%global __brp_check_rpaths %{nil}
%global packname  BatchJobs
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Batch Computing with R

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-BBmisc >= 1.9
BuildRequires:    R-CRAN-checkmate >= 1.8.0
BuildRequires:    R-CRAN-backports >= 1.1.1
BuildRequires:    R-CRAN-RSQLite >= 1.0.9011
BuildRequires:    R-CRAN-stringi >= 0.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sendmailR 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-BBmisc >= 1.9
Requires:         R-CRAN-checkmate >= 1.8.0
Requires:         R-CRAN-backports >= 1.1.1
Requires:         R-CRAN-RSQLite >= 1.0.9011
Requires:         R-CRAN-stringi >= 0.4.1
Requires:         R-methods 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-CRAN-sendmailR 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides Map, Reduce and Filter variants to generate jobs on batch
computing systems like PBS/Torque, LSF, SLURM and Sun Grid Engine.
Multicore and SSH systems are also supported. For further details see the
project web page.

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
