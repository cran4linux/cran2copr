%global packname  eNetXplorer
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Quantitative Exploration of Elastic Net Families for GeneralizedLinear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-calibrate 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-expm 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-Matrix 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-calibrate 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-expm 

%description
Provides a quantitative toolkit to explore elastic net families and to
uncover correlates contributing to prediction under a cross-validation
framework. Fits linear, binomial (logistic) and multinomial models. Candia
J and Tsang JS, BMC Bioinformatics (2019) 20:189
<doi:10.1186/s12859-019-2778-5>.

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
%{rlibdir}/%{packname}/INDEX
