%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CytobankAPI
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cytobank API Wrapper for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.7
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-jose 
Requires:         R-CRAN-curl >= 2.7
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-jose 

%description
Tools to interface with Cytobank's API via R, organized by endpoints that
represent various areas of Cytobank functionality. Learn more about
Cytobank at <https://www.beckman.com/flow-cytometry/software>.

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
