%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qpcR
%global packver   1.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling and Analysis of Real-Time PCR Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Sigmoidal model fitting, optimal model selection and calculation of
various features that are essential in the analysis of quantitative
real-time polymerase chain reaction (qPCR), according to Ritz & Spiess
(2008) <doi:10.1093/bioinformatics/btn227> and Spiess et al. (2008)
<doi:10.1186/1471-2105-9-221>.

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
