%global packname  stmgp
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Rapid and Accurate Genetic Prediction Modeling for Genome-WideAssociation or Whole-Genome Sequencing Study Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Rapidly build accurate genetic prediction models for genome-wide
association or whole-genome sequencing study data by smooth-threshold
multivariate genetic prediction (STMGP) method. Variable selection is
performed using marginal association test p-values with an optimal p-value
cutoff selected by Cp-type criterion. Quantitative and binary traits are
modeled respectively via linear and logistic regression models. A function
that works through PLINK software (Purcell et al. 2007
<DOI:10.1086/519795>, Chang et al. 2015 <DOI:10.1186/s13742-015-0047-8>)
<https://www.cog-genomics.org/plink2> is provided. Covariates can be
included in regression model.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
