%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reslife
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Mean Residual Life (MRL) and Related Values for Different Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-gsl 

%description
A pair of functions for calculating mean residual life (MRL) , median
residual life, and percentile residual life using the outputs of either
the 'flexsurv' package or parameters provided by the user. Input
information about the distribution, the given 'life' value, the
percentile, and the type of residual life, and the function will return
your desired values. For the 'flexsurv' option, the function allows the
user to input their own data for making predictions. This function is
based on Jackson (2016) <doi:10.18637/jss.v070.i08>.

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
