%global packname  arc
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Association Rule Classification

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.5.0
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-discretization 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-datasets 
Requires:         R-CRAN-arules >= 1.5.0
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-discretization 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-datasets 

%description
Implements the Classification-based on Association Rules (CBA) (Bing Liu,
Wynne Hsu, Yiming Ma (1999)
<http://dl.acm.org/citation.cfm?id=3000292.3000305>) algorithm for
association rule classification (ARC). The package also contains several
convenience methods that allow to automatically set CBA parameters
(minimum confidence, minimum support) and it also natively handles numeric
attributes by integrating a pre-discretization step. The rule generation
phase is handled by the 'arules' package. To further decrease the size of
the CBA models produced by the 'arc' package, postprocessing by the 'qCBA'
package is suggested.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
