%global packname  iWISA
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Wavelet-Based Index of Storm Activity

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-splines 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggplot2 
Requires:         R-splines 
Requires:         R-graphics 

%description
A powerful system for estimating an improved wavelet-based index of
magnetic storm activity, storm activity preindex (from individual station)
and SQ variations. It also serves as a flexible visualization tool.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
