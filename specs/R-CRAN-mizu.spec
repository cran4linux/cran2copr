%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mizu
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Thread-Speed 'Async' and Parallel R over Shared Memory

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3

%description
Parallel computation and data exchange between R processes on the same
machine: lock-free channels, work-stealing task pools, and a parallel map
over 'POSIX' shared memory (Linux, macOS) or 'Win32' file mappings
(Windows), with the hot path entirely in user space. Communication is
cheap enough that work can be divided as finely as with threads. Vectors
and data frames transfer zero-copy, received as 'ALTREP' views over the
shared pages, and 'Apache Arrow' tables and record batches travel as a
single frame with zero-copy conversion in both directions. Receives and
task results integrate with 'later' and 'promises' for non-blocking,
event-driven applications such as 'shiny'. Channels, pools, and maps
interoperate with 'pymizu', so a peer or worker can equally be a Python
process. It complements 'mirai', and its payloads interoperate with 'mori'
shared objects.

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
