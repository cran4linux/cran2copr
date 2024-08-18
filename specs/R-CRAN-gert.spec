%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gert
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Git Client for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libgit2-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-zip >= 2.1.0
BuildRequires:    R-CRAN-openssl >= 2.0.3
BuildRequires:    R-CRAN-credentials >= 1.2.1
BuildRequires:    R-CRAN-rstudioapi >= 0.11
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-sys 
Requires:         R-CRAN-zip >= 2.1.0
Requires:         R-CRAN-openssl >= 2.0.3
Requires:         R-CRAN-credentials >= 1.2.1
Requires:         R-CRAN-rstudioapi >= 0.11
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-sys 

%description
Simple git client for R based on 'libgit2' <https://libgit2.org> with
support for SSH and HTTPS remotes. All functions in 'gert' use basic R
data types (such as vectors and data-frames) for their arguments and
return values. User credentials are shared with command line 'git' through
the git-credential store and ssh keys stored on disk or ssh-agent.

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
