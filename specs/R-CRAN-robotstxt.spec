%global packname  robotstxt
%global packver   0.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          1%{?dist}
Summary:          A 'robots.txt' Parser and 'Webbot'/'Spider'/'Crawler'Permissions Checker

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-future.apply >= 1.0.0
BuildRequires:    R-CRAN-spiderbar >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.6.2
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-future.apply >= 1.0.0
Requires:         R-CRAN-spiderbar >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides functions to download and parse 'robots.txt' files. Ultimately
the package makes it easy to check if bots (spiders, crawler, scrapers,
...) are allowed to access specific resources on a domain.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
