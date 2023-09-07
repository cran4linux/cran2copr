%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  natmanager
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Install the 'Natverse' Packages from Scratch

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis >= 2.0.0
BuildRequires:    R-CRAN-gh >= 1.2.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-pak 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-usethis >= 2.0.0
Requires:         R-CRAN-gh >= 1.2.1
Requires:         R-utils 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-pak 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-withr 

%description
Provides streamlined installation for packages from the 'natverse', a
suite of R packages for computational neuroanatomy built on top of the
'nat' 'NeuroAnatomy Toolbox' package. Installation of the complete
'natverse' suite requires a 'GitHub' user account and personal access
token 'GITHUB_PAT'. 'natmanager' will help the end user set this up if
necessary.

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
