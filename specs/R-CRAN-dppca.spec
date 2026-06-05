%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dppca
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differentially Private Principal Component Analysis Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 

%description
Provides tools for differentially private principal component analysis
(PCA) visualization. It includes functions for estimating private
principal component directions, constructing private scree and proportion
of variance explained summaries, and visualizing two-dimensional PCA score
summaries using additive and sparse histogram mechanisms. Group-wise score
visualizations and an interactive 'shiny' app are also provided. Private
principal component directions are based on Kim and Jung (2025)
<doi:10.1002/sam.70053>. Private scree summaries use mechanisms motivated
by Dwork and Roth (2014) <doi:10.1561/0400000042>, Ramsay and Spicker
(2025) <doi:10.48550/arXiv.2501.14095>, and Yu, Ren and Zhou (2024)
<doi:10.3150/23-BEJ1706>. Private score plot frames use smooth sensitivity
quantiles from Nissim, Raskhodnikova and Smith (2007)
<doi:10.1145/1250790.1250803>. Private score histograms use additive and
sparse histogram ideas from Wasserman and Zhou (2010)
<doi:10.1198/jasa.2009.tm08651> and Karwa and Vadhan (2018)
<doi:10.4230/LIPIcs.ITCS.2018.44>.

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
