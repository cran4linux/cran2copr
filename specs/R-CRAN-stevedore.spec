%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stevedore
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Docker Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         docker
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.3.0
BuildRequires:    R-CRAN-yaml >= 2.1.18
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-curl >= 2.3.0
Requires:         R-CRAN-yaml >= 2.1.18
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-jsonlite 

%description
Work with containers over the Docker API.  Rather than using system calls
to interact with a docker client, using the API directly means that we can
receive richer information from docker.  The interface in the package is
automatically generated using the 'OpenAPI' (a.k.a., 'swagger')
specification, and all return values are checked in order to make them
type stable.

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
