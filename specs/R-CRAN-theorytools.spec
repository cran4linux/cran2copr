%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  theorytools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          FAIR Theory Construction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-worcs >= 0.1.16
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-worcs >= 0.1.16
Requires:         R-CRAN-gert 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 

%description
An integrated suite of tools for creating, maintaining, and reusing FAIR
(Findable, Accessible, Interoperable, Reusable) theories. Designed to
support transparent and collaborative theory development, the package
enables users to formalize theories, track changes with version control,
assess pre-empirical coherence, and derive testable hypotheses. Aligning
with open science principles and workflows, 'theorytools' facilitates the
systematic improvement of theoretical frameworks and enhances their
discoverability and usability.

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
