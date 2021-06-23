%global __brp_check_rpaths %{nil}
%global packname  mosaicCalc
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Function-Based Numerical and Symbolic Differentiation and Antidifferentiation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mosaicCore 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mosaic 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-mosaicCore 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-mosaic 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
Part of the Project MOSAIC (<http://mosaic-web.org/>) suite that provides
utility functions for doing calculus (differentiation and integration) in
R. The main differentiation and antidifferentiation operators are
described using formulas and return functions rather than numerical
values. Numerical values can be obtained by evaluating these functions.

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
