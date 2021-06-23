%global __brp_check_rpaths %{nil}
%global packname  neo4jshell
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Querying and Managing 'Neo4J' Databases in 'R'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ssh 
BuildRequires:    R-CRAN-sys 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ssh 
Requires:         R-CRAN-sys 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-R.utils 

%description
Sends queries to a specified 'Neo4J' graph database, capturing results in
a dataframe where appropriate. Other useful functions for the importing
and management of data on the 'Neo4J' server and basic local server admin.

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
