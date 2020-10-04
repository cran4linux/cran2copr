%global packname  antitrust
%global packver   0.99.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.14
Release:          2%{?dist}%{?buildtag}
Summary:          Tools for Antitrust Practitioners

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-numDeriv 

%description
A collection of tools for antitrust practitioners, including the ability
to calibrate different consumer demand systems and simulate the effects of
mergers under different competitive regimes.

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
