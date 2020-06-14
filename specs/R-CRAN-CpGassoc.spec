%global packname  CpGassoc
%global packver   2.60
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.60
Release:          2%{?dist}
Summary:          Association Between Methylation and a Phenotype of Interest

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-methods 
Requires:         R-nlme 
Requires:         R-methods 

%description
Is designed to test for association between methylation at CpG sites
across the genome and a phenotype of interest, adjusting for any relevant
covariates. The package can perform standard analyses of large datasets
very quickly with no need to impute the data. It can also handle mixed
effects models with chip or batch entering the model as a random
intercept. Also includes tools to apply quality control filters, perform
permutation tests, and create QQ plots, manhattan plots, and scatterplots
for individual CpG sites.

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
%{rlibdir}/%{packname}/INDEX
