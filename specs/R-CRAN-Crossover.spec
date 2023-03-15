%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Crossover
%global packver   0.1-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.21
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Search of Crossover Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-crossdes >= 1.1.1
BuildRequires:    R-CRAN-CommonJavaJars >= 1.0.5
BuildRequires:    R-CRAN-rJava >= 0.8.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-JavaGD 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-crossdes >= 1.1.1
Requires:         R-CRAN-CommonJavaJars >= 1.0.5
Requires:         R-CRAN-rJava >= 0.8.3
Requires:         R-CRAN-RcppArmadillo >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-JavaGD 
Requires:         R-CRAN-multcomp 
Requires:         R-stats4 
Requires:         R-CRAN-digest 

%description
Generate and analyse crossover designs from combinatorial or search
algorithms as well as from literature and a GUI to access them.

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
