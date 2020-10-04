%global packname  quantilogram
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Cross-Quantilogram

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-np 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-SparseM 
Requires:         R-stats 
Requires:         R-CRAN-np 

%description
Estimation and inference methods for the cross-quantilogram.  The
cross-quantilogram is a measure of nonlinear dependence between two
variables, based on either unconditional or conditional quantile
functions.  The cross-quantilogram can be considered as an extension of
the correlogram, which is a correlation function over multiple lag periods
and mainly focuses on linear dependency.  One can use the
cross-quantilogram to detect the presence of directional predictability
from one time series to another.  This package provides a statistical
inference method based on the stationary bootstrap.  See Linton and Whang
(2007) <doi:10.1016/j.jeconom.2007.01.004> for univariate time series
analysis and Han, Linton, Oka and Whang (2016)
<doi:10.1016/j.jeconom.2016.03.001> for multivariate time series analysis.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
