%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPLTR
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Partially Linear Tree-Based Regression Model

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-parallel 
Requires:         R-CRAN-rpart 
Requires:         R-parallel 

%description
Combining a generalized linear model with an additional tree part on the
same scale. A four-step procedure is proposed to fit the model and test
the joint effect of the selected tree part while adjusting on confounding
factors. We also proposed an ensemble procedure based on the bagging to
improve prediction accuracy and computed several scores of importance for
variable selection. See 'Cyprien Mbogning et
al.'(2014)<doi:10.1186/2043-9113-4-6> and 'Cyprien Mbogning et
al.'(2015)<doi:10.1159/000380850> for an overview of all the methods
implemented in this package.

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
