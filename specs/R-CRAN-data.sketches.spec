%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  data.sketches
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Streaming Data Sketches

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 

%description
Provides an interface to the 'Apache DataSketches'
(<https://datasketches.apache.org/>) library of streaming algorithms for
approximate analytics on data too large to hold or process exactly.
Sketches are compact, mergeable summaries built in a single pass over a
stream that answer queries such as approximate distinct counts, quantiles
and ranks, frequent items and point-frequency estimates, weighted
sampling, and set membership with mathematically proven error bounds.
Implements Karnin-Lang-Liberty (KLL), Relative Error Quantiles (REQ),
t-Digest, HyperLogLog (HLL), Compressed Probabilistic Counting (CPC),
Theta, Frequent Items, Count-Min, Array of Doubles, Variance Optimal
(VarOpt), Exact and Bounded Probabilistic Proportional-to-Size (EBPPS),
and Bloom filter sketches, with native serialization for interoperability
with other 'Apache DataSketches' implementations.

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
