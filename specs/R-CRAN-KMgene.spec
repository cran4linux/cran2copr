%global packname  KMgene
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Gene-Based Association Analysis for Complex Traits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-seqMeta 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-CRAN-kinship2 
Requires:         R-mgcv 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-seqMeta 

%description
Gene based association test between a group of SNPs and traits including
familial (both continuous and binary) traits, multivariate continuous
(both independent and familial) traits and longitudinal continuous traits.
Part of methods were previously published in Maity et al (2012)
<doi:10.1002/gepi.21663>, Chen et al (2013) <doi:10.1002/gepi.21703>, Yan
et al (2015) <doi:10.1159/000375409>, Yan et al (2015)
<doi:10.1534/genetics.115.178590> and Yan et al (2015)
<doi:10.1159/000445057>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
