%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qad
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Quantification of Asymmetric Dependence

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cowplot 

%description
A copula-based measure for quantifying asymmetry in dependence and
associations. Documentation and theory about 'qad' is provided by the
paper by Junker, Griessenberger & Trutschnig (2021,
<doi:10.1016/j.csda.2020.107058>), and the paper by Trutschnig (2011,
<doi:10.1016/j.jmaa.2011.06.013>).

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
