%global packname  cdcfluview
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve Flu Season Data from the United States Centers for Disease Control and Prevention ('CDC') 'FluView' Portal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-units >= 0.4.6
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-MMWRweek 
Requires:         R-CRAN-units >= 0.4.6
Requires:         R-CRAN-httr 
Requires:         R-CRAN-progress 
Requires:         R-tools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-MMWRweek 

%description
The 'U.S.' Centers for Disease Control and Prevention (CDC) maintain a
portal <https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html> for
accessing state, regional and national influenza statistics as well as
mortality surveillance data. The web interface makes it difficult and
time-consuming to select and retrieve influenza data. Tools are provided
to access the data provided by the portal's underlying 'API'.

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
