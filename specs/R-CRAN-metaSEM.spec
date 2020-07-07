%global packname  metaSEM
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          2%{?dist}
Summary:          Meta-Analysis using Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-OpenMx 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-ellipse 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-lavaan 

%description
A collection of functions for conducting meta-analysis using a structural
equation modeling (SEM) approach via the 'OpenMx' and 'lavaan' packages.
It also implements various procedures to perform meta-analytic structural
equation modeling on the correlation and covariance matrices.

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
