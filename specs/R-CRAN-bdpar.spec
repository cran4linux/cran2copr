%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bdpar
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Big Data Preprocessing Architecture

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlist 
Requires:         R-tools 
Requires:         R-utils 

%description
Provide a tool to easily build customized data flows to pre-process large
volumes of information from different sources. To this end, 'bdpar' allows
to (i) easily use and create new functionalities and (ii) develop new data
source extractors according to the user needs. Additionally, the package
provides by default a predefined data flow to extract and pre-process the
most relevant information (tokens, dates, ... ) from some textual sources
(SMS, Email, tweets, YouTube comments).

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
