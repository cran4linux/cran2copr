%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggfootball
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Plotting Expected Goals (xG) Stats with 'Understat' Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-gdtools 
BuildRequires:    R-CRAN-gfonts 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsoccer 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-gdtools 
Requires:         R-CRAN-gfonts 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsoccer 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-highcharter 
Requires:         R-utils 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 

%description
Scrapes shots data from 'Understat' <https://understat.com/> and
visualizes it using interactive plots: - A detailed shot map displaying
the location, type, and xG value of shots taken by both teams. - An xG
timeline chart showing the cumulative xG for each team over time,
annotated with the details of scored goals.

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
