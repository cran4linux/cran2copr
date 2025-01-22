%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dMrs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Competing Risk in Dependent Net Survival Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-relsurv 

%description
Provides statistical tools for analyzing net and relative survival, with a
key feature of relaxing the assumption of independent censoring and
incorporating the effect of dependent competing risks. It employs a
copula-based methodology, specifically the Archimedean copula, to simulate
data, conduct survival analysis, and offer comparisons with other methods.
This approach is detailed in the work of Adatorwovor et al. (2022)
<doi:10.1515/ijb-2021-0016>.

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
