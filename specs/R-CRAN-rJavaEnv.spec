%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rJavaEnv
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          'Java' Environments for R Projects

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 

%description
Quickly install 'Java Development Kit (JDK)' without administrative
privileges and set environment variables in current R session or project
to solve common issues with 'Java' environment management in 'R'.
Recommended to users of 'Java'/'rJava'-dependent 'R' packages such as
'r5r', 'opentripplanner', 'xlsx', 'openNLP', 'rWeka', 'RJDBC',
'tabulapdf', and many more. 'rJavaEnv' prevents common problems like
'Java' not found, 'Java' version conflicts, missing 'Java' installations,
and the inability to install 'Java' due to lack of administrative
privileges.  'rJavaEnv' automates the download, installation, and setup of
the 'Java' on a per-project basis by setting the relevant 'JAVA_HOME' in
the current 'R' session or the current working directory (via '.Rprofile',
with the user's consent). Similar to what 'renv' does for 'R' packages,
'rJavaEnv' allows different 'Java' versions to be used across different
projects, but can also be configured to allow multiple versions within the
same project (e.g.  with the help of 'targets' package). Note: there are a
few extra steps for 'Linux' users, who don't have any 'Java' previously
installed in their system, and who prefer package installation from
source, rather then installing binaries from 'Posit Package Manager'. See
documentation for details.

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
