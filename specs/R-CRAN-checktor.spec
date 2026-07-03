%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  checktor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extra CRAN Submission Checks

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-xmlparsedata 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-xmlparsedata 

%description
Provides automated checks for common Comprehensive R Archive Network
(CRAN) submission issues that are not caught by standard 'R CMD check'.
Consolidates ad-hoc requirements that CRAN reviewers enforce but standard
checks do not surface, helping 'R' package maintainers identify and fix
issues before submission to reduce rejection rates. Covers code-pattern
issues, DESCRIPTION-field formatting, documentation problems, and general
package structure concerns.

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
