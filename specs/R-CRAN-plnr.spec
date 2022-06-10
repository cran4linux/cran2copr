%global __brp_check_rpaths %{nil}
%global packname  plnr
%global packver   2022.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2022.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          A System for Planing Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-stats 

%description
A system to plan analyses within the mental model where you have one (or
more) datasets and want to run either A) the same function multiple times
with different arguments, or B) multiple functions. This is appropriate
when you have multiple strata (e.g. locations, age groups) that you want
to apply the same function to, or you have multiple variables (e.g.
exposures) that you want to apply the same statistical method to, or when
you are creating the output for a report and you need multiple different
tables or graphs.

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
