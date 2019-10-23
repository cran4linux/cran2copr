%global packname  classiFunc
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Classification of Functional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.8.2
BuildRequires:    R-CRAN-BBmisc >= 1.11
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-fdasrvf 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-rucrdtw 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-checkmate >= 1.8.2
Requires:         R-CRAN-BBmisc >= 1.11
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-fdasrvf 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-rucrdtw 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
Efficient implementation of k-nearest neighbor estimation and kernel
estimation for functional data classification.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
