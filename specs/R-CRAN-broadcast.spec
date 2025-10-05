%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  broadcast
%global packver   0.1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Broadcasted Array Operations Like 'NumPy'

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-methods 

%description
Implements efficient 'NumPy'-like broadcasted operations for atomic and
recursive arrays. In the context of operations involving 2 (or more)
arrays, “broadcasting” refers to efficiently recycling array dimensions
without allocating additional memory. Besides linking to 'Rcpp',
'broadcast' does not use any external libraries in any way; 'broadcast'
was essentially made from scratch and can be installed out-of-the-box. The
implementations available in 'broadcast' include, but are not limited to,
the following. 1) Broadcasted element-wise operations on any 2 arrays;
they support a large set of relational, arithmetic, Boolean, string, and
bit-wise operations. 2) A faster, more memory efficient, and broadcasted
abind-like function, for binding arrays along an arbitrary dimension. 3)
Broadcasted ifelse-like, and apply-like functions. 4) Casting functions,
that cast subset-groups of an array to a new dimension, cast nested lists
to dimensional lists, and vice-versa. 5) A few linear algebra functions
for statistics. The functions in the 'broadcast' package strive to
minimize computation time and memory usage (which is not just better for
efficient computing, but also for the environment).

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
