%global packname  linkspotter
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Bivariate Correlations Calculation and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-minerva 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rAmCharts 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-minerva 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rAmCharts 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 

%description
Compute and visualize using the 'visNetwork' package all the bivariate
correlations of a dataframe. Several and different types of correlation
coefficients (Pearson's r, Spearman's rho, Kendall's tau, distance
correlation, maximal information coefficient and equal-freq
discretization-based maximal normalized mutual information) are used
according to the variable couple type (quantitative vs categorical,
quantitative vs quantitative, categorical vs categorical).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
