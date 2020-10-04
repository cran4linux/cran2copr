%global packname  LIHNPSD
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}%{?buildtag}
Summary:          Poisson Subordinated Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-Bolstad2 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-Rmpfr 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-Bolstad2 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-Rmpfr 

%description
A Poisson Subordinated Distribution to capture major leptokurtic features
in log-return time series of financial data.

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
