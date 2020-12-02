%global packname  rdhs
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          API Client and Dataset Management for the Demographic and Health Survey (DHS) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-storr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-iotools 
Requires:         R-CRAN-brio 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-storr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-iotools 

%description
Provides a client for (1) querying the DHS API for survey indicators and
metadata (<https://api.dhsprogram.com/#/index.html>), (2) identifying
surveys and datasets for analysis, (3) downloading survey datasets from
the DHS website, (4) loading datasets and associate metadata into R, and
(5) extracting variables and combining datasets for pooled analysis.

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
