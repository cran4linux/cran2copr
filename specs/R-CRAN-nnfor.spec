%global __brp_check_rpaths %{nil}
%global packname  nnfor
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Forecasting with Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-CRAN-uroot 
BuildRequires:    R-methods 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tsutils 
Requires:         R-CRAN-uroot 
Requires:         R-methods 

%description
Automatic time series modelling with neural networks. Allows fully
automatic, semi-manual or fully manual specification of networks. For
details of the specification methodology see: (i) Crone and Kourentzes
(2010) <doi:10.1016/j.neucom.2010.01.017>; and (ii) Kourentzes et al.
(2014) <doi:10.1016/j.eswa.2013.12.011>.

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
