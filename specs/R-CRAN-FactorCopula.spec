%global packname  FactorCopula
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Factor Copula Models for Mixed Continuous and Discrete Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-polycor 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-abind 
Requires:         R-utils 
Requires:         R-CRAN-polycor 

%description
Estimation, model selection and goodness-of-fit of factor copula models
for mixed continuous and discrete data in Kadhem and Nikoloulopoulos
(2019) <arXiv:1907.07395>.

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
