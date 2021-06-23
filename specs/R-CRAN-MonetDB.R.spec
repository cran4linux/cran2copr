%global __brp_check_rpaths %{nil}
%global packname  MonetDB.R
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Connect MonetDB to R

License:          MPL (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-digest >= 0.6.4
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-methods 
BuildRequires:    R-codetools 
Requires:         R-CRAN-digest >= 0.6.4
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-testthat 
Requires:         R-methods 
Requires:         R-codetools 

%description
Allows to pull data from MonetDB into R.

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
