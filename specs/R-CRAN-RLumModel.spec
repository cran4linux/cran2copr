%global packname  RLumModel
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Ordinary Differential Equations to Understand Luminescence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-deSolve >= 1.21
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.400.2.0
BuildRequires:    R-CRAN-Luminescence >= 0.9.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-deSolve >= 1.21
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-Luminescence >= 0.9.0
Requires:         R-utils 
Requires:         R-methods 

%description
A collection of functions to simulate luminescence signals in quartz and
Al2O3 based on published models.

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
