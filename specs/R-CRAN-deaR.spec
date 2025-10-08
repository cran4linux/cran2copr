%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deaR
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conventional and Fuzzy Data Envelopment Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-optiSolve 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-grDevices 
Requires:         R-CRAN-optiSolve 

%description
Set of functions for Data Envelopment Analysis. It runs both classic and
fuzzy DEA models. See: Banker, R.; Charnes, A.; Cooper, W.W. (1984).
<doi:10.1287/mnsc.30.9.1078>, Charnes, A.; Cooper, W.W.; Rhodes, E.
(1978). <doi:10.1016/0377-2217(78)90138-8> and Charnes, A.; Cooper, W.W.;
Rhodes, E. (1981). <doi:10.1287/mnsc.27.6.668>.

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
