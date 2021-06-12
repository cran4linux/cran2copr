%global packname  QTLEMM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          QTL Mapping and Hotspots Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
For QTL mapping, it consists of several functions to perform various
tasks, including simulating or analyzing data, computing the significance
thresholds and visualizing the QTL mapping results. The single-QTL or
multiple-QTL method that allows a host of statistical models to be fitted
and compared is applied to analyze the data for the estimation of QTL
parameters. The models include the linear regression, permutation test,
normal mixture model and truncated normal mixture model. The Gaussian
stochastic process is implemented to compute the significance thresholds
for QTL detection onto a genetic linkage map in the experimental
populations. Two types of data, the complete genotyping or selective
genotyping data, from various experimental populations, including
backcross, F2, recombinant inbred (RI) populations, advanced intercrossed
(AI) populations, are considered in the QTL mapping analysis. For QTL
hotpot detection, the statistical methods can be developed based on either
using the individual-level data or using the summarized data. We have
proposed a statistical framework that can handle both the individual-level
data and summarized QTL data for QTL hotspots detection. Our statistical
framework can overcome the underestimation of threshold arising from
ignoring the correlation structure among traits, and also identify the
different types of hotspots with very low computational cost during the
detection process. Here, we attempt to provide the R code for our
statistical framework. The QTL mapping program is carried out by EM
process, which can be seen in Kao, C.-H. ,Z.-B. Zeng and R. D. Teasdale
(1999) <doi:10.1534/genetics.103.021642>. The analyze of selective
genotyping can be seen in H.-I LEE, H.-A. HO and C.-H. Kao (2014)
<doi:10.1534/genetics.114.168385>. The analyze of QTL hotspot detection
can be seen in Wu, P.-Y., M.-.H. Yang, and C.-H. Kao (2020)
<doi:10.1101/2020.08.13.249342>.

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
