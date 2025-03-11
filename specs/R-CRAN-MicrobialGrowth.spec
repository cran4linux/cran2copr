%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MicrobialGrowth
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates Growth Parameters from Models and Plots the Curve

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlstools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-nlstools 
Requires:         R-stats 
Requires:         R-utils 

%description
Fit growth curves to various known microbial growth models automatically
to estimate growth parameters. Growth curves can be plotted with their
uncertainty band. Growth models are: modified Gompertz model (Zwietering
et al. (1990) <doi:10.1128/aem.56.6.1875-1881.1990>), Baranyi model
(Baranyi and Roberts (1994) <doi:10.1016/0168-1605%%2894%%2990157-0>), Rosso
model (Rosso et al. (1993) <doi:10.1006/jtbi.1993.1099>) and linear model
(Dantigny (2005) <doi:10.1016/j.ijfoodmicro.2004.10.013>).

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
