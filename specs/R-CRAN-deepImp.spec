%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deepImp
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation with Deep Learning Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-VIM 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-VIM 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Imputation of mixed-type and compositional data with neural networks. Each
network head is a generalised linear model plus a neural-network
correction. Missing values are imputed by point predictions or, for
multiple imputation, by predictive draws on bootstrap fits, with pooling
through 'mice'. The architecture (number and size of hidden layers,
dropout, activation, optimiser) and the training settings are
user-configurable. See Templ (2021) <doi:10.1007/978-3-030-71175-7>.

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
