%global __brp_check_rpaths %{nil}
%global packname  MAVTgsa
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Three methods to identify differentially expressed gene sets,ordinary least square test, Multivariate Analysis Of Variancetest with n contrasts and Random forest.

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.2
Requires:         R-core >= 2.13.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-randomForest 
Requires:         R-MASS 

%description
This package is a gene set analysis function for one-sided test (OLS),
two-sided test (multivariate analysis of variance). If the experimental
conditions are equal to 2, the p-value for Hotelling's t^2 test is
calculated. If the experimental conditions are great than 2, the p-value
for Wilks' Lambda is determined and post-hoc test is reported too. Three
multiple comparison procedures, Dunnett, Tukey, and sequential pairwise
comparison, are implemented. The program computes the p-values and FDR
(false discovery rate) q-values for all gene sets. The p-values for
individual genes in a significant gene set are also listed. MAVTgsa
generates two visualization output: a p-value plot of gene sets (GSA plot)
and a GST-plot of the empirical distribution function of the ranked test
statistics of a given gene set. A Random Forests-based procedure is to
identify gene sets that can accurately predict samples from different
experimental conditions or are associated with the continuous phenotypes.

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
%{rlibdir}/%{packname}/INDEX
