%global packname  adwave
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Wavelet Analysis of Genomic Data from Admixed Populations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-waveslim 

%description
Implements wavelet-based approaches for describing population admixture.
Principal Components Analysis (PCA) is used to define the population
structure and produce a localized admixture signal for each individual.
Wavelet summaries of the PCA output describe variation present in the data
and can be related to population-level demographic processes. For more
details, see J Sanderson, H Sudoyo, TM Karafet, MF Hammer and MP Cox.
2015. Reconstructing past admixture processes from local genomic ancestry
using wavelet transformation. Genetics 200:469-481
<doi:10.1534/genetics.115.176842>.

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
