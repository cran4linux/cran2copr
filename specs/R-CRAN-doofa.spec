%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doofa
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Designs for Order-of-Addition Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-combinat 

%description
A facility to generate efficient designs for order-of-additions
experiments under pair-wise-order model, see Dennis K. J. Lin and Jiayu
Peng (2019)."Order-of-addition experiments: A review and some new
thoughts".  Quality Engineering, 31:1, 49-59,
<doi:10.1080/08982112.2018.1548021>. It also provides a facility to
generate component orthogonal arrays under component position model, see
Jian-Feng Yang, Fasheng Sun & Hongquan Xu (2020): "A Component Position
Model, Analysis and Design for Order-of-Addition Experiments".
Technometrics, <doi:10.1080/00401706.2020.1764394>.

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
