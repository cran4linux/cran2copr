%global packname  ISEtools
%global packver   3.1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1.1
Release:          2%{?dist}
Summary:          Tools for Ion Selective Electrodes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Xmisc 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Xmisc 
Requires:         R-CRAN-coda 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Characterisation and calibration of single or multiple Ion Selective
Electrodes (ISEs); activity estimation of experimental samples. Implements
methods described in: Dillingham, P.W., Radu, T., Diamond, D., Radu, A.
and McGraw, C.M. (2012) <doi:10.1002/elan.201100510> and Dillingham, P.W.,
Alsaedi, B.S.O. and McGraw, C.M. (2017) <doi:10.1109/ICSENS.2017.8233898>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
