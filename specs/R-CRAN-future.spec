%global __brp_check_rpaths %{nil}
%global packname  future
%global packver   1.21.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.21.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Parallel and Distributed Processing in R for Everyone

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-parallelly >= 1.21.0
BuildRequires:    R-CRAN-listenv >= 0.8.0
BuildRequires:    R-CRAN-globals >= 0.13.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-parallelly >= 1.21.0
Requires:         R-CRAN-listenv >= 0.8.0
Requires:         R-CRAN-globals >= 0.13.1
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-tools 
Requires:         R-utils 

%description
The purpose of this package is to provide a lightweight and unified Future
API for sequential and parallel processing of R expression via futures.
The simplest way to evaluate an expression in parallel is to use `x %%<-%% {
expression }` with `plan(multiprocess)`. This package implements
sequential, multicore, multisession, and cluster futures.  With these, R
expressions can be evaluated on the local machine, in parallel a set of
local machines, or distributed on a mix of local and remote machines.
Extensions to this package implement additional backends for processing
futures via compute cluster schedulers etc. Because of its unified API,
there is no need to modify any code in order switch from sequential on the
local machine to, say, distributed processing on a remote compute cluster.
Another strength of this package is that global variables and functions
are automatically identified and exported as needed, making it
straightforward to tweak existing code to make use of futures.

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
