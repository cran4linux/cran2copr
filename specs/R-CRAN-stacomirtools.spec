%global packname  stacomirtools
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          'ODBC' Connection Class for Package stacomiR

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-utils 
Requires:         R-CRAN-RODBC 
Requires:         R-methods 
Requires:         R-CRAN-xtable 
Requires:         R-utils 

%description
S4 class wrappers for the 'ODBC' connection, also provides some utilities
to paste small datasets to clipboard, rename columns. It is used by the
package 'stacomiR' for connections to the database. Development versions
of 'stacomiR' are available in R-forge.

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

%files
%{rlibdir}/%{packname}
