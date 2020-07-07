%global packname  kutils
%global packver   1.70
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.70
Release:          3%{?dist}
Summary:          Project Management Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-RUnit 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-foreign 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-RUnit 

%description
Tools for data importation, recoding, and inspection. There are functions
to create new project folders, R code templates, create uniquely named
output directories, and to quickly obtain a visual summary for each
variable in a data frame.  The main feature here is the systematic
implementation of the "variable key" framework for data importation and
recoding.  We are eager to have community feedback about the variable key
and the vignette about it. In version 1.7, the function 'semTable' is
removed. It was deprecated since 1.67. That is provided in a separate
package, 'semTable'.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/TODO
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
