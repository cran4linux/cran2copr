%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TFisher
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Thresholding Fisher's P-Value Combination Method

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Matrix 

%description
We provide the cumulative distribution function (CDF), quantile, and
statistical power calculator for a collection of thresholding Fisher's
p-value combination methods, including Fisher's p-value combination
method, truncated product method and, in particular, soft-thresholding
Fisher's p-value combination method which is proven to be optimal in some
context of signal detection. The p-value calculator for the omnibus
version of these tests are also included. For reference, please see Hong
Zhang, Tong Tong, John Landers and Zheyang Wu (2020) "TFisher: A powerful
truncation and weighting procedure for combining p-values"
<doi:10.1214/19-AOAS1302>.

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
