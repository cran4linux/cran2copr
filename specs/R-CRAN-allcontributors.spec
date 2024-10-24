%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  allcontributors
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Acknowledge all Contributors to a Project

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-gitcreds 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-gitcreds 
Requires:         R-CRAN-magrittr 

%description
Acknowledge all contributors to a project via a single function call. The
function appends to a 'README' or other specified file(s) a table with
names of all individuals who contributed via code or repository issues.
The package also includes several additional functions to extract and
quantify contributions to any repository.

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
