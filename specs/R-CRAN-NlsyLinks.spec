%global packname  NlsyLinks
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          2%{?dist}
Summary:          Utilities and Kinship Information for Research with the NLSY

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-methods 

%description
Utilities and kinship information for behavior genetics and developmental
research using the National Longitudinal Survey of Youth (NLSY;
<http://www.bls.gov/nls/>).

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
