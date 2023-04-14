%global __brp_check_rpaths %{nil}
%global packname  bulletr
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Algorithms for Matching Bullet Lands

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-smoother 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-smoother 

%description
Analyze bullet lands using nonparametric methods. We provide a reading
routine for x3p files (see <http://www.openfmc.org> for more information)
and a host of analysis functions designed to assess the probability that
two bullets were fired from the same gun barrel.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
