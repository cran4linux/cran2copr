%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcrpart
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tree-Based Varying Coefficient Regression for Generalized Linear and Ordinal Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-nlme >= 3.1.123
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-stats 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-strucchange 
Requires:         R-CRAN-nlme >= 3.1.123
Requires:         R-parallel 
Requires:         R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-strucchange 

%description
Recursive partitioning for varying coefficient generalized linear models
and ordinal linear mixed models. Special features are coefficient-wise
partitioning, non-varying coefficients and partitioning of time-varying
variables in longitudinal regression. A description of a part of this
package was published by Burgin and Ritschard (2017)
<doi:10.18637/jss.v080.i06>.

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
