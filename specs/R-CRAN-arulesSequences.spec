%global packname  arulesSequences
%global packver   0.2-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.25
Release:          3%{?dist}
Summary:          Mining Frequent Sequences

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-CRAN-arules >= 1.5.1
BuildRequires:    R-methods 
Requires:         R-CRAN-arules >= 1.5.1
Requires:         R-methods 

%description
Add-on for arules to handle and mine frequent sequences. Provides
interfaces to the C++ implementation of cSPADE by Mohammed J. Zaki.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/bin
