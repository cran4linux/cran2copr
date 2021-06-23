%global __brp_check_rpaths %{nil}
%global packname  SMMT
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Swiss Municipal Data Merger Tool Maps Municipalities Over Time

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 

%description
In Switzerland, the landscape of municipalities is changing rapidly mainly
due to mergers. The Swiss Municipal Data Merger Tool automatically detects
these mutations and maps municipalities over time, i.e. municipalities of
an old state to municipalities of a new state. This functionality is
helpful when working with datasets that are based on different spatial
references. The spatial reference in this context signifies a set of
municipalities at a given point in time.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
