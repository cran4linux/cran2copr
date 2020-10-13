%global packname  flexmix
%global packver   2.3-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.17
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Mixture Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-modeltools >= 0.2.16
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-utils 
Requires:         R-CRAN-modeltools >= 0.2.16
Requires:         R-CRAN-lattice 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-utils 

%description
A general framework for finite mixtures of regression models using the EM
algorithm is implemented. The E-step and all data handling are provided,
while the M-step can be supplied by the user to easily define new models.
Existing drivers implement mixtures of standard linear models, generalized
linear models and model-based clustering.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
