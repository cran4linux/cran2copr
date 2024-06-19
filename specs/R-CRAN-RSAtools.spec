%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSAtools
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Response Surface Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-semTools >= 0.5.5
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-RSA >= 0.10.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-aplpack 
BuildRequires:    R-methods 
Requires:         R-CRAN-semTools >= 0.5.5
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-RSA >= 0.10.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-aplpack 
Requires:         R-methods 

%description
Provides tools for response surface analysis, using a comparative
framework that identifies best-fitting solutions across 37 families of
polynomials. Many of these tools are based upon and extend the 'RSA'
package, by testing a larger scope of polynomials (+27 families), more
diverse response surface probing techniques (+acceleration points), more
plots (+line of congruence, +line of incongruence, both with extrema), and
other useful functions for exporting results.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
