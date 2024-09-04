%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProSportsDraftData
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Professional Sports Draft Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
We provide comprehensive draft data for major professional sports leagues,
including the National Football League (NFL), National Basketball
Association (NBA), and National Hockey League (NHL). It offers access to
both historical and current draft data, allowing for detailed analysis and
research on player biases and player performance. The package is useful
for sports fans and researchers interested in identifying biases and
trends within scouting reports. Created by web scraping data from leading
websites that cover professional sports player scouting reports, the
package allows users to filter and summarize data for analytical purposes.
For further details on the methods used, please refer to Wickham (2022)
"rvest: Easily Harvest (Scrape) Web Pages"
<https://CRAN.R-project.org/package=rvest> and Harrison (2023) "RSelenium:
R Bindings for Selenium WebDriver"
<https://CRAN.R-project.org/package=RSelenium>.

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
