%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  future.mirai
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Future' API for Parallel Processing using 'mirai'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mirai >= 0.12.1
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-utils 
Requires:         R-CRAN-mirai >= 0.12.1
Requires:         R-CRAN-future 
Requires:         R-CRAN-parallelly 
Requires:         R-utils 

%description
Implementation of the 'Future' API <doi:10.32614/RJ-2021-048> on top of
the 'mirai' package <doi:10.5281/zenodo.7912722>. This allows you to
process futures, as defined by the 'future' package, in parallel out of
the box, on your local machine or across remote machines. Contrary to
back-ends relying on the 'parallel' package (e.g. 'multisession') and
socket connections, 'mirai_cluster' and 'mirai_multisession', provided
here, can run more than 125 parallel R processes.

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
