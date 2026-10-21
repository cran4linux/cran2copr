%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qdfauction
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Quantile Density Estimation and Structural Analysis of First-Price Auctions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Nonparametric estimators of the quantile density function (the derivative
of the quantile function): kernel, boundary-corrected kernel,
Poisson-weight and Bernstein-polynomial smoothers, indirect estimators
(Jones (1992) <https://www.ism.ac.jp/editsec/aism/pdf/044_4_0721.pdf>;
Soni, Dewan and Jain (2012) <doi:10.1016/j.csda.2012.04.014>; Chaubey,
Dewan and Li (2024) <doi:10.1080/03610926.2023.2222922>), and linear,
hard-thresholded and block-thresholded wavelet estimators (Chesneau, Dewan
and Doosti (2016) <doi:10.1016/j.csda.2015.08.006>; Shirazi and Doosti
(2022) <doi:10.1080/03610918.2019.1656250>), with smoothing parameters
chosen by biased, robust likelihood (Wu (2019)
<doi:10.1080/07350015.2018.1424633>) or least-squares cross-validation.
The estimators are applied to the structural analysis of first-price
sealed-bid auctions: recovery of private values for independent or
affiliated values and risk-neutral or risk-averse bidders (Doosti, Dewan
and Talebian (2025) <doi:10.1016/j.econlet.2025.112670>; Doosti (2026)
<doi:10.1016/j.econlet.2026.112837>), estimation of the private-value
density with kernel benchmarks (Hickman and Hubbard (2015)
<doi:10.1002/jae.2385>; Marmer and Shneyerov (2012)
<doi:10.1016/j.jeconom.2011.09.020>; Zincenko (2024)
<doi:10.1016/j.jeconom.2024.105734>) and confidence bands (Ma, Marmer and
Shneyerov (2019) <doi:10.1016/j.jeconom.2019.02.006>), and estimation of
the seller's expected revenue and optimal reserve price, with tools for
simulating equilibrium bids and comparing estimators.

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
