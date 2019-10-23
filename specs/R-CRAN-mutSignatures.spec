%global packname  mutSignatures
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Decipher Mutational Signatures from Somatic Mutational Catalogs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-cluster 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-proxy 

%description
Cancer cells accumulate DNA mutations as result of DNA damage and DNA
repair processes. This computational framework is aimed at deciphering DNA
mutational signatures operating in cancer. The input is a numeric matrix
of DNA mutation counts detected in a panel of cancer samples. The
framework performs Non-negative Matrix Factorization to extract the most
likely signatures explaining the observed set of DNA mutations. The
framework relies on parallelization and is optimized for use on multi-core
systems. This framework is an R-based implementation of the original
MATLAB WTSI framework by Alexandrov LB et al (2013)
<DOI:10.1016/j.celrep.2012.12.008>.

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
%{rlibdir}/%{packname}/INDEX
