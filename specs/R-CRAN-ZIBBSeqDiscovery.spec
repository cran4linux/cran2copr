%global __brp_check_rpaths %{nil}
%global packname  ZIBBSeqDiscovery
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Zero-Inflated Beta-Binomial Modeling of Microbiome Count Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mcc 
Requires:         R-CRAN-mcc 

%description
Microbiome count data (Operational Taxonomic Unit, OTUs) is usually
overdispersed and has excessive zero counts. The 'ZIBBSeqDiscovery'
assumes a zero-inflated beta-binomial model for the distribution of the
count data, and employes link functions to adjust interested covariates.
To fit the model, two approaches are proposed (i) a free approach which
treats the overdispersion parameters for OTUs as independent, and (ii) a
constrained approach which proposes a mean-overdispersion relationship to
the count data. This package can be used to test the association between
the composition of the microbiome counts and the interested covariates.

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
