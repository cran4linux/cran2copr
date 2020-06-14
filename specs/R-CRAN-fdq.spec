%global packname  fdq
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          2%{?dist}
Summary:          Forest Data Quality

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Fgmutils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-Fgmutils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-stats 

%description
Forest data quality is a package that contains methods of analysis of
forest databases, the purpose of the analyzes is to evaluate the quality
of the data present in the databases focusing on the dimensions of
consistency, pountuality and completeness. Databases can range from forest
inventory data to growth model data. The package has methods to work with
large volumes of data quickly, in addition in certain analyzes it is
possible to generate the graphs for a better understanding of the analysis
and reporting of the analyzed analysis.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
