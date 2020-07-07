%global packname  knitcitations
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}
Summary:          Citations for 'Knitr' Markdown Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RefManageR >= 0.8.2
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-RefManageR >= 0.8.2
Requires:         R-CRAN-httr >= 0.3
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-utils 

%description
Provides the ability to create dynamic citations in which the
bibliographic information is pulled from the web rather than having to be
entered into a local database such as 'bibtex' ahead of time. The package
is primarily aimed at authoring in the R 'markdown' format, and can
provide outputs for web-based authoring such as linked text for inline
citations.  Cite using a 'DOI', URL, or 'bibtex' file key.  See the
package URL for details.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
