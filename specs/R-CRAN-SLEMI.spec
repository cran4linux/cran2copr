%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SLEMI
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Learning Based Estimation of Mutual Information

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-foreach 
Requires:         R-methods 

%description
The implementation of the algorithm for estimation of mutual information
and channel capacity from experimental data by classification procedures
(logistic regression). Technically, it allows to estimate
information-theoretic measures between finite-state input and
multivariate, continuous output. Method described in Jetka et al. (2019)
<doi:10.1371/journal.pcbi.1007132>.

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
