%global packname  sn
%global packver   1.6-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.2
Release:          2%{?dist}%{?buildtag}
Summary:          The Skew-Normal and Related Distributions Such as the Skew-t

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-mnormt >= 1.5.4
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-mnormt >= 1.5.4
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 
Requires:         R-CRAN-quantreg 

%description
Build and manipulate probability distributions of the skew-normal family
and some related ones, notably the skew-t family, and provide related
statistical methods for data fitting and model diagnostics, in the
univariate and the multivariate case.

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
