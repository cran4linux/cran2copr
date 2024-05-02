%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSEAL
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Analysis Library

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-statcomp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-synchronicity 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-wdm 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-statcomp 
Requires:         R-stats 
Requires:         R-CRAN-synchronicity 
Requires:         R-utils 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-wdm 

%description
The library allows to perform a multivariate time series classification
based on the use of Discrete Wavelet Transform for feature extraction, a
step wise discriminant to select the most relevant features and finally,
the use of a linear or quadratic discriminant for classification. Note
that all these steps can be done separately which allows to implement new
steps. Velasco, I., Sipols, A., de Blas, C. S., Pastor, L., & Bayona, S.
(2023) <doi:10.1186/S12938-023-01079-X>. Percival, D. B., & Walden, A. T.
(2000,ISBN:0521640687). Maharaj, E. A., & Alonso, A. M. (2014)
<doi:10.1016/j.csda.2013.09.006>.

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
