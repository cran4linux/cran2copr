%global packname  mlt.docreg
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Most Likely Transformations: Documentation and Regression Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp >= 1.4.4
BuildRequires:    R-CRAN-mlt >= 1.0.5
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-lattice 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-CRAN-np 
Requires:         R-CRAN-multcomp >= 1.4.4
Requires:         R-CRAN-mlt >= 1.0.5
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-eha 
Requires:         R-lattice 
Requires:         R-survival 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-truncreg 
Requires:         R-CRAN-np 

%description
Additional documentation, a package vignette and regression tests for
package mlt.

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
