%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  W4MRUtils
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Functions for Harmonized W4M Tool Development

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Provides a set of utility function to prevent the spread of utility
scripts in W4M (Workflow4Metabolomics) tools, and centralize them in a
single package. To note, some are meant to be replaced by the use of
dedicated packages in the future, like the parse_args() function: it is
here only to prepare the ground for more global changes in W4M scripts and
tools. This package is used by part of the W4M Galaxy modules, some of
them being available on the community-maintained GitHub repository for
Metabolomics' Galaxy tools
<https://github.com/workflow4metabolomics/tools-metabolomics>. See
Delporte et al (2025) <doi:10.1002/cpz1.70095> for more details.

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
