%global __brp_check_rpaths %{nil}
%global packname  rsparkling
%global packver   0.2.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.19
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for H2O Sparkling Water

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-h2o >= 3.8.3.3
BuildRequires:    R-CRAN-sparklyr >= 0.3
BuildRequires:    R-utils 
Requires:         R-CRAN-h2o >= 3.8.3.3
Requires:         R-CRAN-sparklyr >= 0.3
Requires:         R-utils 

%description
An extension package for 'sparklyr' that provides an R interface to H2O
Sparkling Water machine learning library (see
<https://github.com/h2oai/sparkling-water> for more information).

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
