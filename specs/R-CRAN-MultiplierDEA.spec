%global packname  MultiplierDEA
%global packver   0.1.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          2%{?dist}
Summary:          Multiplier Data Envelopment Analysis and Cross Efficiency

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-lpSolveAPI 

%description
Functions are provided for calculating efficiency using multiplier DEA
(Data Envelopment Analysis): Measuring the efficiency of decision making
units (Charnes et al., 1978 <doi:10.1016/0377-2217(78)90138-8>) and cross
efficiency using single and two-phase approach. In addition, it includes
some datasets for calculating efficiency and cross efficiency.

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
