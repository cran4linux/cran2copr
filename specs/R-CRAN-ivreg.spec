%global packname  ivreg
%global packver   0.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Stage Least-Squares Regression with Diagnostics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car >= 3.0.9
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-stats 
Requires:         R-CRAN-car >= 3.0.9
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-lmtest 
Requires:         R-stats 

%description
Instrumental variable estimation for linear models by two-stage
least-squares (2SLS) regression. The main ivreg() model-fitting function
is designed to provide a workflow as similar as possible to standard lm()
regression. A wide range of methods is provided for fitted ivreg model
objects, including extensive functionality for computing and graphing
regression diagnostics in addition to other standard model tools.

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
