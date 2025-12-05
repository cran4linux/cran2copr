%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  taskqueue
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Task Queue for Parallel Computing Based on PostgreSQL

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-ssh 
Requires:         R-CRAN-settings 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-ssh 

%description
Implements a task queue system for asynchronous parallel computing using
'PostgreSQL' <https://www.postgresql.org/> as a backend. Designed for
embarrassingly parallel problems where tasks do not communicate with each
other. Dynamically distributes tasks to workers, handles uneven load
balancing, and allows new workers to join at any time. Particularly useful
for running large numbers of independent tasks on high-performance
computing (HPC) clusters with 'SLURM' <https://slurm.schedmd.com/> job
schedulers.

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
