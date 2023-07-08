%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlstrOpalr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Support Compatibility Between 'Maelstrom' R Packages and 'Opal' Environment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-opalr 
BuildRequires:    R-CRAN-fabR 
BuildRequires:    R-CRAN-madshapR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-opalr 
Requires:         R-CRAN-fabR 
Requires:         R-CRAN-madshapR 

%description
The goal of this package is to provide functions to support compatibility
between 'Maelstrom' R packages and 'Opal' environment. 'Opal' is the
'OBiBa' core database application for biobanks. It is used to build data
repositories that integrates data collected from multiple sources. 'Opal
Maelstrom' is a specific implementation of this software. This 'Opal'
client is specifically designed to interact with 'Opal Maelstrom'
distributions to perform operations on the R server side. The user must
have adequate credentials. Please see <https://opaldoc.obiba.org/en/dev/>
for complete documentation.

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
