%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coxphf
%global packver   1.13.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13.4
Release:          1%{?dist}%{?buildtag}
Summary:          Cox Regression with Firth's Penalized Likelihood

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 

%description
Implements Firth's penalized maximum likelihood bias reduction method for
Cox regression which has been shown to provide a solution in case of
monotone likelihood (nonconvergence of likelihood function), see Heinze
and Schemper (2001) and Heinze and Dunkler (2008). The program fits
profile penalized likelihood confidence intervals which were proved to
outperform Wald confidence intervals.

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
