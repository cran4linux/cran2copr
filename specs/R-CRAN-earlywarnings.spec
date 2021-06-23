%global __brp_check_rpaths %{nil}
%global packname  earlywarnings
%global packver   1.0.59
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.59
Release:          3%{?dist}%{?buildtag}
Summary:          Early Warning Signals Toolbox for Detecting Critical Transitionsin Timeseries

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Kendall 
Requires:         R-KernSmooth 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-som 
Requires:         R-CRAN-spam 
Requires:         R-stats 

%description
The Early-Warning-Signals Toolbox provides methods for estimating
statistical changes in timeseries that can be used for identifying nearby
critical transitions. Based on Dakos et al (2012) Methods for Detecting
Early Warnings of Critical Transitions in Time Series Illustrated Using
Simulated Ecological Data. PLoS ONE 7(7):e41010

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
