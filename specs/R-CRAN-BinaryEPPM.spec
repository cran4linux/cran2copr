%global packname  BinaryEPPM
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          3%{?dist}
Summary:          Mean and Variance Modeling of Binary Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-lmtest 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Modeling under- and over-dispersed binary data using extended Poisson
process models (EPPM) as in the article Faddy and Smith (2012)
<doi:10.1002/bimj.201100214> .

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
