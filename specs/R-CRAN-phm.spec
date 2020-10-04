%global packname  phm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Phrase Mining

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.6.2
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-tm >= 0.7.7
BuildRequires:    R-CRAN-slam >= 0.1.46
Requires:         R-utils >= 3.6.2
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-tm >= 0.7.7
Requires:         R-CRAN-slam >= 0.1.46

%description
Functions to extract and handle commonly occurring principal phrases
obtained from collections of texts.

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
