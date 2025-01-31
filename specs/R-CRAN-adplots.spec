%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adplots
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ad-Plot and Ud-Plot for Visualizing Distributional Properties and Normality

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
The empirical cumulative average deviation function introduced by the
author is utilized to develop both Ad- and Ud-plots. The Ad-plot can
identify symmetry, skewness, and outliers of the data distribution,
including anomalies. The Ud-plot created by slightly modifying Ad-plot is
exceptional in assessing normality, outperforming normal QQ-plot, normal
PP-plot, and their derivations. The d-value that quantifies the degree of
proximity between the Ud-plot and the graph of the estimated normal
density function helps guide to make decisions on confirmation of
normality. Full description of this methodology can be found in the
article by Wijesuriya (2025) <doi:10.1080/03610926.2024.2440583>.

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
