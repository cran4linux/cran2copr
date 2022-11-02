%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mockthat
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Function Mocking for Unit Testing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
With the deprecation of mocking capabilities shipped with 'testthat' as of
'edition 3' it is left to third-party packages to replace this
functionality, which in some test-scenarios is essential in order to run
unit tests in limited environments (such as no Internet connection).
Mocking in this setting means temporarily substituting a function with a
stub that acts in some sense like the original function (for example by
serving a HTTP response that has been cached as a file). The only exported
function 'with_mock()' is modeled after the eponymous 'testthat' function
with the intention of providing a drop-in replacement.

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
