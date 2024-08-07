%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robfilter
%global packver   4.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Time Series Filters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Implementations for several robust procedures that allow for (online)
extraction of the signal of univariate or multivariate time series by
applying robust regression techniques to a moving time window are
provided. Included are univariate filtering procedures based on
repeated-median regression as well as hybrid and trimmed filters derived
from it; see Schettlinger et al. (2006) <doi:10.1515/BMT.2006.010>. The
adaptive online repeated median by Schettlinger et al. (2010)
<doi:10.1002/acs.1105> and the slope comparing adaptive repeated median by
Borowski and Fried (2013) <doi:10.1007/s11222-013-9391-7> choose the width
of the moving time window adaptively. Multivariate versions are also
provided; see Borowski et al. (2009) <doi:10.1080/03610910802514972> for a
multivariate online adaptive repeated median and Borowski (2012)
<doi:10.17877/DE290R-14393> for a multivariate slope comparing adaptive
repeated median. Furthermore, a repeated-median based filter with
automatic outlier replacement and shift detection is provided; see Fried
(2004) <doi:10.1080/10485250410001656444>.

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
