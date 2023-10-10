%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  success
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Control Charts Estimation Software

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 

%description
Quality control charts for survival outcomes. Allows users to construct
the Continuous Time Generalized Rapid Response CUSUM (CGR-CUSUM)
<doi:10.1093/biostatistics/kxac041>, the Biswas & Kalbfleisch (2008)
<doi:10.1002/sim.3216> CUSUM, the Bernoulli CUSUM and the risk-adjusted
funnel plot for survival data <doi:10.1002/sim.1970>. These procedures can
be used to monitor survival processes for a change in the failure rate.

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
