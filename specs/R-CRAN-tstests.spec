%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tstests
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Goodness of Fit and Forecast Evaluation Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tsmethods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-xts 
Requires:         R-methods 
Requires:         R-CRAN-tsmethods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-xts 

%description
Goodness of Fit and Forecast Evaluation Tests for timeseries models.
Includes, among others, the Generalized Method of Moments (GMM)
Orthogonality Test of Hansen (1982), the Nyblom (1989) parameter constancy
test, the sign-bias test of Engle and Ng (1993), and a range of tests for
value at risk and expected shortfall evaluation.

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
