%global packname  joinet
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Elastic Net Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-palasso 
BuildRequires:    R-CRAN-cornet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-palasso 
Requires:         R-CRAN-cornet 

%description
Implements high-dimensional multivariate regression by stacked
generalisation (Wolpert 1992 <doi:10.1016/S0893-6080(05)80023-1>). For
positively correlated outcomes, a single multivariate regression is
typically more predictive than multiple univariate regressions. Includes
functions for model fitting, extracting coefficients, outcome prediction,
and performance measurement. If required, install MRCE from GitHub
(<https://github.com/cran/MRCE>).

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
