%global packname  DecisionAnalysis
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Implementation of Multi Objective Decision Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-Cairo 
Requires:         R-methods 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-DiagrammeR 

%description
Aides in the multi objective decision analysis process by simplifying the
creation of value hierarchy tree plots, calculating and plotting single
and multi attribute value function scores, and conducting sensitivity
analysis. Linear, exponential, and categorical single attribute value
functions are supported. For details see Parnell (2013,
ISBN:978-1-118-17313-8) Kirkwood (1997, ISBN:0-534-51692-0).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
