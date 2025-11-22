%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ergm.sign
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Exponential-Family Models for Signed Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-statnet.common 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-ergm.multi 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tergm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-graphlayouts 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-statnet.common 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-ergm.multi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tergm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-graphlayouts 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-purrr 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 

%description
Extends the 'ergm.multi' packages from the Statnet suite to fit (temporal)
exponential-family random graph models for signed networks. The framework
models positive and negative ties as interdependent, which allows
estimation and testing of structural balance theory. The package also
includes options for descriptive summaries, visualization, and simulation
of signed networks. See Krivitsky, Koehly, and Marcum (2020)
<doi:10.1007/s11336-020-09720-7> and Fritz, C., Mehrl, M., Thurner, P. W.,
& Kauermann, G. (2025) <doi:10.1017/pan.2024.21>.

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
