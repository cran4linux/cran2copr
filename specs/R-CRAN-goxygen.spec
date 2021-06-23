%global __brp_check_rpaths %{nil}
%global packname  goxygen
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          In-Code Documentation for 'GAMS'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-gms 
BuildRequires:    R-CRAN-citation 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-gms 
Requires:         R-CRAN-citation 
Requires:         R-CRAN-yaml 

%description
A collection of tools which extract a model documentation from 'GAMS' code
and comments. In order to use the package you need to install 'pandoc' and
'pandoc-citeproc' first (<https://pandoc.org/>).

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
