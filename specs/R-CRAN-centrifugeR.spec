%global packname  centrifugeR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Balancing Centrifuge Rotors

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.2.9
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-pracma >= 2.2.9
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
Find the numbers of tubes that can be loaded in centrifuge rotors and give
the instructions on how to balance these tubes in cases of equal or
unequal masses. The methods of the package are constructed based on Sivek
(2010) <doi:10.1515/integ.2010.031> and Peil and Hauryliuk (2010)
<arXiv:1004.3671>.

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
%{rlibdir}/%{packname}/INDEX
