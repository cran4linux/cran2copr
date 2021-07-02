%global __brp_check_rpaths %{nil}
%global packname  BOSO
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bilevel Optimization Selector Operator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
A novel feature selection algorithm for linear regression called BOSO
(Bilevel Optimization Selector Operator). The main contribution is the use
a bilevel optimization problem to select the variables in the training
problem that minimize the error in the validation set. Preprint available:
[Valcarcel, L. V., San Jose-Eneriz, E., Cendoya, X., Rubio, A., Agirre,
X., Prosper, F., & Planes, F. J. (2020). "BOSO: a novel feature selection
algorithm for linear regression with high-dimensional data." bioRxiv.
<doi:10.1101/2020.11.18.388579>]. In order to run the vignette, it is
recommended to install the 'bestsubset' package, using the following
command: devtools::install_github(repo="ryantibs/best-subset",
subdir="bestsubset"). If you do not have gurobi, run
devtools::install_github(repo="lvalcarcel/best-subset",
subdir="bestsubset").

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
