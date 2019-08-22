%global packname  ACMEeqtl
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Estimation of Interpretable eQTL Effect Sizes Using a Log ofLinear Model

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-filematrix 
BuildRequires:    R-parallel 
Requires:         R-CRAN-filematrix 
Requires:         R-parallel 

%description
We use a non-linear model, termed ACME, that reflects a parsimonious
biological model for allelic contributions of cis-acting eQTLs. With
non-linear least-squares algorithm we estimate maximum likelihood
parameters. The ACME model provides interpretable effect size estimates
and p-values with well controlled Type-I error. Includes both R and (much
faster) C implementations. For more details see Palowitch et al. (2017)
<doi:10.1111/biom.12810>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
