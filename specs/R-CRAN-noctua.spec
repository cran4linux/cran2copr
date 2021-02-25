%global packname  noctua
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Connect to 'AWS Athena' using R 'AWS SDK' 'paws' ('DBI' Interface)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-paws >= 0.1.5
BuildRequires:    R-CRAN-uuid >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-paws >= 0.1.5
Requires:         R-CRAN-uuid >= 0.1.4
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed to be compatible with the 'R' package 'DBI' (Database Interface)
when connecting to Amazon Web Service ('AWS') Athena
<https://aws.amazon.com/athena/>. To do this the 'R' 'AWS' Software
Development Kit ('SDK') 'paws' <https://github.com/paws-r/paws> is used as
a driver.

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
