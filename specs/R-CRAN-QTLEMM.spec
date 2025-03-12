%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QTLEMM
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          QTL EM Algorithm Mapping and Hotspots Detection

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
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gtools 

%description
For QTL mapping, this package comprises several functions designed to
execute diverse tasks, such as simulating or analyzing data, calculating
significance thresholds, and visualizing QTL mapping results. The
single-QTL or multiple-QTL method, which enables the fitting and
comparison of various statistical models, is employed to analyze the data
for estimating QTL parameters. The models encompass linear regression,
permutation tests, normal mixture models, and truncated normal mixture
models. The Gaussian stochastic process is utilized to compute
significance thresholds for QTL detection on a genetic linkage map within
experimental populations. Two types of data, complete genotyping, and
selective genotyping data from various experimental populations, including
backcross, F2, recombinant inbred (RI) populations, and advanced
intercrossed (AI) populations, are considered in the QTL mapping analysis.
For QTL hotspot detection, statistical methods can be developed based on
either utilizing individual-level data or summarized data. We have
proposed a statistical framework capable of handling both individual-level
data and summarized QTL data for QTL hotspot detection. Our statistical
framework can overcome the underestimation of thresholds resulting from
ignoring the correlation structure among traits. Additionally, it can
identify different types of hotspots with minimal computational cost
during the detection process. Here, we endeavor to furnish the R codes for
our QTL mapping and hotspot detection methods, intended for general use in
genes, genomics, and genetics studies. The QTL mapping methods for the
complete and selective genotyping designs are based on the multiple
interval mapping (MIM) model proposed by Kao, C.-H. , Z.-B. Zeng and R. D.
Teasdale (1999) <doi: 10.1534/genetics.103.021642> and H.-I Lee, H.-A. Ho
and C.-H. Kao (2014) <doi: 10.1534/genetics.114.168385>, respectively. The
QTL hotspot detection analysis is based on the method by Wu, P.-Y., M.-.H.
Yang, and C.-H. Kao (2021) <doi: 10.1093/g3journal/jkab056>.

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
