%global __brp_check_rpaths %{nil}
%global packname  dequer
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Stacks, Queues, and 'Deques' for R

License:          BSD 2-clause License + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0

%description
Queues, stacks, and 'deques' are list-like, abstract data types. These are
meant to be very cheap to "grow", or insert new objects into. A typical
use case involves storing data in a list in a streaming fashion, when you
do not necessarily know how may elements need to be stored. Unlike R's
lists, the new data structures provided here are not necessarily stored
contiguously, making insertions and deletions at the front/end of the
structure much faster.  The underlying implementation is new and uses a
head/tail doubly linked list; thus, we do not rely on R's environments or
hashing.  To avoid unnecessary data copying, most operations on these data
structures are performed via side-effects.

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
