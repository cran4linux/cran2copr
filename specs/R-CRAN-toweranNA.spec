%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toweranNA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Method for Handling Missing Values in Prediction Applications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-regtools >= 0.8.0
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-stats 
Requires:         R-CRAN-regtools >= 0.8.0
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-pdist 
Requires:         R-stats 

%description
Non-imputational method for handling missing values in a prediction
context, meaning that not only are there missing values in the training
dataset, but also some values may be missing in future cases to be
predicted. Based on the notion of regression averaging (Matloff (2017,
ISBN: 9781498710916)).

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
