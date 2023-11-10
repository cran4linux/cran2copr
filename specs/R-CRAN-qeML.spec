%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qeML
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quick and Easy Machine Learning Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-regtools >= 0.8.0
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-tufte 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-toweranNA 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-partools 
BuildRequires:    R-CRAN-FOCI 
Requires:         R-CRAN-regtools >= 0.8.0
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-tufte 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-toweranNA 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-partools 
Requires:         R-CRAN-FOCI 

%description
The letters 'qe' in the package title stand for "quick and easy," alluding
to the convenience goal of the package. We bring together a variety of
machine learning (ML) tools from standard R packages, providing wrappers
with a simple, convenient, and uniform interface.

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
