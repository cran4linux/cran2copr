%global packname  tsnetwork
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Constructing Dynamic Networks for Time-Series Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-CRAN-QUIC 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-longitudinal 
BuildRequires:    R-parallel 
Requires:         R-CRAN-QUIC 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-longitudinal 
Requires:         R-parallel 

%description
Implements the method in Behrouzi, Abegaz, and Wit (2018)
<arXiv:1805.09840> to learn intra-time and inter-time conditional
independence networks for ordinal time-series data and mixed
discrete-and-continuous time-series data. This package assumes a
stationary process, where both instantaneous and dynamic networks stay
fixed over time.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
