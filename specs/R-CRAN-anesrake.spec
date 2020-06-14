%global packname  anesrake
%global packver   0.80
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.80
Release:          2%{?dist}
Summary:          ANES Raking Implementation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-weights 

%description
Provides a comprehensive system for selecting variables and weighting data
to match the specifications of the American National Election Studies. The
package includes methods for identifying discrepant variables, raking
data, and assessing the effects of the raking algorithm. It also allows
automated re-raking if target variables fall outside identified bounds and
allows greater user specification than other available raking algorithms.
A variety of simple weighted statistics that were previously in this
package (version .55 and earlier) have been moved to the package
'weights.'

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
