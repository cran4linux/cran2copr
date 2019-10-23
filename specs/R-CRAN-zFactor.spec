%global packname  zFactor
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Calculate the Compressibility Factor 'z' for Hydrocarbon Gases

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-logging 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-knitcitations 
BuildRequires:    R-CRAN-covr 
Requires:         R-CRAN-logging 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-knitcitations 
Requires:         R-CRAN-covr 

%description
Computational algorithms to solve equations and find the 'compressibility'
factor `z` of hydrocarbon gases. Correlations available:
'Hall-Yarborough', 'Dranchuk-AbuKassem', 'Dranchuk-Purvis-Robinson',
'Beggs-Brill', 'Papp', Shell and an Artificial Neural Network correlation
(Ann10) by 'Kamyab' 'et al'. The package uses the original 'Standing-Katz'
chart for statistical comparison and plotting. Applicable to sweet
hydrocarbon gases for now.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tmp
%{rlibdir}/%{packname}/INDEX
