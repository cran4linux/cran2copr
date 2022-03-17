%global __brp_check_rpaths %{nil}
%global packname  git2r
%global packver   0.30.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.30.1
Release:          1%{?dist}%{?buildtag}
Summary:          Provides Access to Git Repositories

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    libgit2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    libssh2-devel
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-utils 

%description
Interface to the 'libgit2' library, which is a pure C implementation of
the 'Git' core methods. Provides access to 'Git' repositories to extract
data and running some basic 'Git' commands.

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
