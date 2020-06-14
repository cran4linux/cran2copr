%global packname  cRegulome
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Obtain and Visualize Regulome-Gene Expression Correlations inCancer

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-DBI 
Requires:         R-graphics 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-grid 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-igraph 

%description
Builds a 'SQLite' database file of pre-calculated transcription
factor/microRNA-gene correlations (co-expression) in cancer from the
Cistrome Cancer Liu et al. (2011) <doi:10.1186/gb-2011-12-8-r83> and
'miRCancerdb' databases (in press). Provides custom classes and functions
to query, tidy and plot the correlation data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
