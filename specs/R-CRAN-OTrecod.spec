%global __brp_check_rpaths %{nil}
%global packname  OTrecod
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Fusion using Optimal Transportation Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-missMDA 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-StatMatch 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-rdist 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.glpk 
BuildRequires:    R-CRAN-ompr 
BuildRequires:    R-CRAN-ompr.roi 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-vcd 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-missMDA 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-StatMatch 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-rdist 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.glpk 
Requires:         R-CRAN-ompr 
Requires:         R-CRAN-ompr.roi 
Requires:         R-CRAN-party 
Requires:         R-CRAN-vcd 

%description
In the context of data fusion, the package provides a set of functions
dedicated to the solving of 'recoding problems' using optimal
transportation theory (Gares, Guernec, Savy (2019)
<doi:10.1515/ijb-2018-0106> and Gares, Omer (2020)
<doi:10.1080/01621459.2020.1775615>). From two databases with no
overlapping part except a subset of shared variables, the functions of the
package assist users until obtaining a unique synthetic database, where
the missing information is fully completed.

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
