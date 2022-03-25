%global __brp_check_rpaths %{nil}
%global packname  admix
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Package Admix for Admixture (aka Contamination) Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-base 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-base 
Requires:         R-CRAN-fdrtool 
Requires:         R-graphics 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements several methods to estimate the unknown quantities related to
two-component admixture models, where the two components can belong to any
distribution (note that in the case of multinomial mixtures, the two
components must belong to the same family). Estimation methods depend on
the assumptions made on the unknown component density (see Bordes and
Vandekerkhove (2010) <doi:10.3103/S1066530710010023>; Patra and Sen (2016)
<doi:10.1111/rssb.12148>); Milhaud, Pommeret, Salhi and Vandekerkhove
(2021) <doi:10.1016/j.jspi.2021.05.010>). In practice, one can estimate
both the mixture weight and the unknown component density in a wide
variety of frameworks. On top of that, hypothesis tests can be performed
in one and two-samples contexts to test the unknown component density.
Finally, clustering of unknown mixture components is also feasible in a
K-samples setting.

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
