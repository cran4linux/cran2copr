%global packname  RSA
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          2%{?dist}
Summary:          Response Surface Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-aplpack 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-methods 
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-ggplot2 
Requires:         R-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-aplpack 
Requires:         R-CRAN-tkrplot 
Requires:         R-methods 

%description
Advanced response surface analysis. The main function RSA computes and
compares several nested polynomial regression models (full second- or
third-order polynomial, shifted and rotated squared difference model,
rising ridge surfaces, basic squared difference model, asymmetric or
level-dependent congruence effect models). The package provides plotting
functions for 3d wireframe surfaces, interactive 3d plots, and contour
plots. Calculates many surface parameters (a1 to a5, principal axes,
stationary point, eigenvalues) and provides standard, robust, or
bootstrapped standard errors and confidence intervals for them.

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
