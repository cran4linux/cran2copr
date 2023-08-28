%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VMDML
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Mode Decomposition Based Machine Learning Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VMDecomp 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-nnfor 
Requires:         R-CRAN-VMDecomp 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-nnfor 

%description
Application of Variational Mode Decomposition based different Machine
Learning models for univariate time series forecasting. For method details
see (i) K. Dragomiretskiy and D. Zosso (2014)
<doi:10.1109/TSP.2013.2288675>; (ii) Pankaj Das (2020)
<http://krishi.icar.gov.in/jspui/handle/123456789/44138>.

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
