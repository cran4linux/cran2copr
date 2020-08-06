%global packname  univariateML
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Maximum Likelihood Estimation for Univariate Densities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-logitnorm 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-nakagami 
BuildRequires:    R-CRAN-fGarch 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-logitnorm 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-nakagami 
Requires:         R-CRAN-fGarch 

%description
User-friendly maximum likelihood estimation (Fisher (1921)
<doi:10.1098/rsta.1922.0009>) of univariate densities.

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
