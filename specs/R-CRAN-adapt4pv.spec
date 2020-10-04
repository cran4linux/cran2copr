%global packname  adapt4pv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Adaptive Approaches for Signal Detection in Pharmacovigilance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 3.0.2
BuildRequires:    R-Matrix >= 1.0.6
BuildRequires:    R-CRAN-speedglm 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-glmnet >= 3.0.2
Requires:         R-Matrix >= 1.0.6
Requires:         R-CRAN-speedglm 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
A collection of several pharmacovigilance signal detection methods based
on adaptive lasso. Additional lasso-based and propensity score-based
signal detection approaches are also supplied.

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
