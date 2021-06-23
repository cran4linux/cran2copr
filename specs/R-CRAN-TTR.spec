%global __brp_check_rpaths %{nil}
%global packname  TTR
%global packver   0.24.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24.2
Release:          1%{?dist}%{?buildtag}
Summary:          Technical Trading Rules

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xts >= 0.10.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xts >= 0.10.0
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-curl 

%description
A collection of over 50 technical indicators for creating technical
trading rules. The package also provides fast implementations of common
rolling-window functions, and several volatility calculations.

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
