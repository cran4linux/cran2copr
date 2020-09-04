%global packname  refund
%global packver   0.1-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.22
Release:          1%{?dist}%{?buildtag}
Summary:          Regression with Functional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00.0
Requires:         R-core >= 3.00.0
BuildArch:        noarch
BuildRequires:    R-mgcv >= 1.8.23
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-Matrix 
BuildRequires:    R-lattice 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-gamm4 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-RLRsim 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbs 
BuildRequires:    R-methods 
Requires:         R-mgcv >= 1.8.23
Requires:         R-CRAN-fda 
Requires:         R-Matrix 
Requires:         R-lattice 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-magic 
Requires:         R-nlme 
Requires:         R-CRAN-gamm4 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-RLRsim 
Requires:         R-splines 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-pbs 
Requires:         R-methods 

%description
Methods for regression for functional data, including function-on-scalar,
scalar-on-function, and function-on-function regression. Some of the
functions are applicable to image data.

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
