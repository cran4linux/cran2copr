%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pxweb
%global packver   0.16.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to PXWEB APIs

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr >= 1.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-jsonlite 

%description
Generic interface for the PX-Web/PC-Axis API. The PX-Web/PC-Axis API is
used by organizations such as Statistics Sweden and Statistics Finland to
disseminate data. The R package can interact with all PX-Web/PC-Axis APIs
to fetch information about the data hierarchy, extract metadata and
extract and parse statistics to R data.frame format. PX-Web is a solution
to disseminate PC-Axis data files in dynamic tables on the web.  Since
2013 PX-Web contains an API to disseminate PC-Axis files.

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
