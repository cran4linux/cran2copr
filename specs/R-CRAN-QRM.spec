%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QRM
%global packver   0.4-35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.35
Release:          1%{?dist}%{?buildtag}
Summary:          Provides R-Language Code to Examine Quantitative Risk Management Concepts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-timeDate 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-gsl 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-mgcv 
Requires:         R-methods 
Requires:         R-CRAN-timeDate 

%description
Provides functions/methods to accompany the book Quantitative Risk
Management: Concepts, Techniques and Tools by Alexander J. McNeil,
Ruediger Frey, and Paul Embrechts.

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
