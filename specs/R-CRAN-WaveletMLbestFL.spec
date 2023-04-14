%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaveletMLbestFL
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Best Wavelet Filter-Level for Prepared Wavelet-Based Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-WaveletML 
BuildRequires:    R-CRAN-CEEMDANML 
BuildRequires:    R-CRAN-DescribeDF 
Requires:         R-CRAN-WaveletML 
Requires:         R-CRAN-CEEMDANML 
Requires:         R-CRAN-DescribeDF 

%description
Four filters have been chosen namely 'haar', 'c6', 'la8', and 'bl14'
(Kindly refer to 'wavelets' in 'CRAN' repository for more supported
filters). Levels of decomposition are 2, 3, 4, etc. up to maximum
decomposition level which is ceiling value of logarithm of length of the
series base 2. For each combination two models are run separately. Results
are stored in 'input'. First five metrics are expected to be minimum and
last three metrics are expected to be maximum for a model to be considered
good. Firstly, every metric value (among first five) is searched in every
columns and minimum values are denoted as 'MIN' and other values are
denoted as 'NA'. Secondly, every metric (among last three) is searched in
every columns and maximum values are denoted as 'MAX' and other values are
denoted as 'NA'. 'output' contains the similar number of rows (which is 8)
and columns (which is number filter-level combinations) as of 'input'.
Values in 'output' are corresponding 'NA', 'MIN' or 'MAX'. Finally, the
column containing minimum number of 'NA' values is denoted as the best
('FL'). In special case, if two columns having equal 'NA', it has been
checked among these two columns which one is having least 'NA' in first
five rows and has been inferred as the best. 'FL_metrics_values' are the
corresponding metrics values. 'WARIGAANbest' is the data frame (dimension:
1*8) containing different metrics of the best filter-level combination.
More details can be found in Garai and others (2023)
<doi:10.13140/RG.2.2.11977.42087>.

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
