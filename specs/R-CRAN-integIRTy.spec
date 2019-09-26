%global packname  integIRTy
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Integrating Multiple Modalities of High Throughput Assays UsingItem Response Theory

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-mclust 
Requires:         R-MASS 
Requires:         R-CRAN-abind 

%description
Provides a systematic framework for integrating multiple modalities of
assays profiled on the same set of samples. The goal is to identify genes
that are altered in cancer either marginally or consistently across
different assays. The heterogeneity among different platforms and
different samples are automatically adjusted so that the overall
alteration magnitude can be accurately inferred. See Tong and Coombes
(2012) <doi:10.1093/bioinformatics/bts561>.

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
