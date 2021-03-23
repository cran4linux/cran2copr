%global packname  decorators
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extend the Behaviour of a Function without Explicitly Modifying it

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-purrr 

%description
A decorator is a function that receives a function, extends its behaviour,
and returned the altered function. Any caller that uses the decorated
function uses the same interface as it were the original, undecorated
function. Decorators serve two primary uses: (1) Enhancing the response of
a function as it sends data to a second component; (2) Supporting multiple
optional behaviours. An example of the first use is a timer decorator that
runs a function, outputs its execution time on the console, and returns
the original function's result. An example of the second use is input type
validation decorator that during running time tests whether the caller has
passed input arguments of a particular class. Decorators can reduce
execution time, say by memoization, or reduce bugs by adding defensive
programming routines.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
