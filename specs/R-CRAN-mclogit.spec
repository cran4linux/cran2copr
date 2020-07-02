%global packname  mclogit
%global packver   0.8.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5.1
Release:          1%{?dist}
Summary:          Multinomial Logit Models, with or without Random Effects orOverdispersion

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-memisc 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-memisc 
Requires:         R-methods 

%description
Provides estimators for multinomial logit models in their conditional
logit and baseline logit variants, with or without random effects, with or
without overdispersion. Random effects models are estimated using the PQL
technique (based on a Laplace approximation) or the MQL technique (based
on a Solomon-Cox approximation). Estimates should be treated with caution
if the group sizes are small.

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
