%global packname  arm
%global packver   1.11-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis Using Regression and Multilevel/HierarchicalModels

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.0
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
BuildRequires:    R-utils 
Requires:         R-Matrix >= 1.0
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-methods 
Requires:         R-nlme 
Requires:         R-utils 

%description
Functions to accompany A. Gelman and J. Hill, Data Analysis Using
Regression and Multilevel/Hierarchical Models, Cambridge University Press,
2007.

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
