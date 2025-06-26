%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mirai
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Minimalist Async Evaluation Framework for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-nanonext >= 1.6.1
Requires:         R-CRAN-nanonext >= 1.6.1

%description
Designed for simplicity, a 'mirai' evaluates an R expression
asynchronously in a parallel process, locally or distributed over the
network. Modern networking and concurrency, built on 'nanonext' and 'NNG',
ensures reliable scheduling over fast inter-process communications or
TCP/IP secured by TLS.  Launch remote resources via SSH or cluster
managers for distributed computing. The queued architecture scales
efficiently to millions of tasks over thousands of connections, requiring
no storage on the file system.  Innovative features include event-driven
promises, asynchronous parallel map, and seamless serialization of
otherwise non-exportable reference objects.

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
