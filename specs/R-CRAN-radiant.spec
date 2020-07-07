%global packname  radiant
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          2%{?dist}
Summary:          Business Analytics using R and Shiny

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-radiant.data >= 1.3.0
BuildRequires:    R-CRAN-radiant.design >= 1.3.0
BuildRequires:    R-CRAN-radiant.basics >= 1.3.0
BuildRequires:    R-CRAN-radiant.model >= 1.3.0
BuildRequires:    R-CRAN-radiant.multivariate >= 1.3.0
BuildRequires:    R-CRAN-import >= 1.1.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-radiant.data >= 1.3.0
Requires:         R-CRAN-radiant.design >= 1.3.0
Requires:         R-CRAN-radiant.basics >= 1.3.0
Requires:         R-CRAN-radiant.model >= 1.3.0
Requires:         R-CRAN-radiant.multivariate >= 1.3.0
Requires:         R-CRAN-import >= 1.1.0

%description
A platform-independent browser-based interface for business analytics in
R, based on the shiny package. The application combines the functionality
of radiant.data, radiant.design, radiant.basics, radiant.model, and
radiant.multivariate.

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
