%global __brp_check_rpaths %{nil}
%global packname  Rexperigen
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to Experigen

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 

%description
Provides convenience functions to communicate with an Experigen server:
Experigen (<http://github.com/aquincum/experigen>) is an online framework
for creating linguistic experiments, and it stores the results on a
dedicated server. This package can be used to retrieve the results from
the server, and it is especially helpful with registered experiments, as
authentication with the server has to happen.

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
