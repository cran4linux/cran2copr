%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AutoWeatherIndices
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Weather Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-gtools 

%description
Weather indices are formed from weather variables in this package. The
users can input any number of weather variables recorded over any number
of weeks. This package has no restriction on the number of weeks and
weather variables to be taken as input.The details of the method can be
seen (i)'Joint effects of weather variables on rice yields' by R. Agrawal,
R. C. Jain and M. P. Jha in Mausam, vol. 34, pp. 189-194,
1983,<doi:10.54302/mausam.v34i2.2392>,(ii)'Improved weather indices based
Bayesian regression model for forecasting crop yield' by M. Yeasin, K. N.
Singh, A. Lama and B. Gurung in Mausam, vol. 72, pp.879-886,
2021,<doi:10.54302/mausam.v72i4.670>.

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
