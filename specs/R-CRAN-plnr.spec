%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plnr
%global packver   2025.11.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2025.11.22
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Planning and Executing Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
A comprehensive framework for planning and executing analyses in R. It
provides a structured approach to running the same function multiple times
with different arguments, executing multiple functions on the same
datasets, and creating systematic analyses across multiple strata or
variables. The framework is particularly useful for applying the same
analysis across multiple strata (e.g., locations, age groups), running
statistical methods on multiple variables (e.g., exposures, outcomes),
generating multiple tables or graphs for reports, and creating systematic
surveillance analyses. Key features include efficient data management,
structured analysis planning, flexible execution options, built-in
debugging tools, and hash-based caching.

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
