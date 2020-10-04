%global packname  symSEM
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Symbolic Computation for Structural Equation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-metaSEM 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-metaSEM 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-mvtnorm 

%description
A collection of functions for symbolic computation using 'Ryacas' package
for structural equation models. This package includes functions to
calculate model-implied covariance (and correlation) matrix and sampling
covariance matrix of functions of variables using the first-order Taylor
approximation. Reference: McArdle and McDonald (1984)
<doi:10.1111/j.2044-8317.1984.tb00802.x>.

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
