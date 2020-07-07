%global packname  ANOM
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}
Summary:          Analysis of Means

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MCPAN 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-nparcomp 
BuildRequires:    R-CRAN-SimComp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MCPAN 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-nparcomp 
Requires:         R-CRAN-SimComp 

%description
Analysis of means (ANOM) as used in technometrical computing. The package
takes results from multiple comparisons with the grand mean (obtained with
'multcomp', 'SimComp', 'nparcomp', or 'MCPAN') or corresponding
simultaneous confidence intervals as input and produces ANOM decision
charts that illustrate which group means deviate significantly from the
grand mean.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
