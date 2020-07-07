%global packname  freqdom.fda
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}
Summary:          Functional Time Series: Dynamic Functional Principal Components

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-freqdom 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-base 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-freqdom 

%description
Implementations of functional dynamic principle components analysis.
Related graphic tools and frequency domain methods. These methods directly
use multivariate dynamic principal components implementation, following
the guidelines from Hormann, Kidzinski and Hallin (2016), Dynamic
Functional Principal Component <doi:10.1111/rssb.12076>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
