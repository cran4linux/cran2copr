%global packname  distrMod
%global packver   2.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.4
Release:          3%{?dist}%{?buildtag}
Summary:          Object Oriented Implementation of Probability Models

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-RandVar >= 1.2.0
BuildRequires:    R-MASS 
BuildRequires:    R-stats4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-RandVar >= 1.2.0
Requires:         R-MASS 
Requires:         R-stats4 
Requires:         R-methods 
Requires:         R-CRAN-startupmsg 
Requires:         R-CRAN-sfsmisc 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Implements S4 classes for probability models based on packages 'distr' and
'distrEx'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/MASKING
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
