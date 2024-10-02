%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  My.stepwise
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Variable Selection Procedures for Regression Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
The stepwise variable selection procedure (with iterations between the
'forward' and 'backward' steps) can be used to obtain the best candidate
final regression model in regression analysis. All the relevant covariates
are put on the 'variable list' to be selected. The significance levels for
entry (SLE) and for stay (SLS) are usually set to 0.15 (or larger) for
being conservative. Then, with the aid of substantive knowledge, the best
candidate final regression model is identified manually by dropping the
covariates with p value > 0.05 one at a time until all regression
coefficients are significantly different from 0 at the chosen alpha level
of 0.05.

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
