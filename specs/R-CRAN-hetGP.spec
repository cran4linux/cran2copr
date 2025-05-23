%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hetGP
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Heteroskedastic Gaussian Process Modeling and Design under Replication

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-mco 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-mco 
Requires:         R-CRAN-quadprog 

%description
Performs Gaussian process regression with heteroskedastic noise following
the model by Binois, M., Gramacy, R., Ludkovski, M. (2016)
<doi:10.48550/arXiv.1611.05902>, with implementation details in Binois, M.
& Gramacy, R. B. (2021) <doi:10.18637/jss.v098.i13>. The input dependent
noise is modeled as another Gaussian process. Replicated observations are
encouraged as they yield computational savings. Sequential design
procedures based on the integrated mean square prediction error and
lookahead heuristics are provided, and notably fast update functions when
adding new observations.

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
