%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  async
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Coroutines: Generators / Yield, Async / Await, and Streams

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat >= 3.0.0
BuildRequires:    R-CRAN-nseval >= 0.4.3
BuildRequires:    R-CRAN-later 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-testthat >= 3.0.0
Requires:         R-CRAN-nseval >= 0.4.3
Requires:         R-CRAN-later 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-stringr 

%description
Write sequential-looking code that pauses and resumes. gen() creates a
generator, an iterator that returns a value and pauses each time it
reaches a yield() call. async() creates a promise, which runs until it
reaches a call to await(), then resumes when information is available.
These work similarly to generator and async constructs from 'Python' or
'JavaScript'. Objects produced are compatible with the 'iterators' and
'promises' packages. Version 0.3 supports on.exit, single-step debugging,
stream() for making asynchronous iterators, and delimited goto() in
switch() calls.

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
