%global packname  snht
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Standard Normal Homogeneity Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
Implementation of robust and non-robust Standard Normal Homogeneity Test
(SNHT) for changepoint detection. This test statistic is equal sided, as
proposed in "Homogenization of Radiosonde Temperature Time Series Using
Innovation Statistics" by Haimberger, L., 2007. However, the statistic
contains an estimate of sigma^2 in the denominator instead of sigma, which
seems to be a more appropriate value (based on the paper "Homogenization
of Swedish temperature data. Part I: Homogeneity test for linear trends."
by Alexandersson, H., and A. Moberg, 1997).

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
