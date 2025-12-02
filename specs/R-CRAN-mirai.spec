%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mirai
%global packver   2.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Minimalist Async Evaluation Framework for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-nanonext >= 1.7.2
Requires:         R-CRAN-nanonext >= 1.7.2

%description
Designed for simplicity, a 'mirai' evaluates an R expression
asynchronously, locally or distributed over the network. Built on
'nanonext' and 'NNG' for modern networking and concurrency, scales
efficiently to millions of tasks over thousands of parallel processes.
Provides optimal scheduling over fast 'IPC', TCP, and TLS connections,
integrating with SSH or cluster managers. Implements event-driven promises
for reactive programming, and supports custom serialization for
cross-language data types.

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
