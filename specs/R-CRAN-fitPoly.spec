%global packname  fitPoly
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          2%{?dist}
Summary:          Genotype Calling for Bi-Allelic Marker Assays

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-foreach 

%description
Genotyping assays for bi-allelic markers (e.g. SNPs) produce signal
intensities for the two alleles. 'fitPoly' assigns genotypes (allele
dosages) to a collection of polyploid samples based on these signal
intensities. 'fitPoly' replaces the older package 'fitTetra' that was
limited (a.o.) to only tetraploid populations whereas 'fitPoly' accepts
any ploidy level. Reference: Voorrips RE, Gort G, Vosman B (2011)
<doi:10.1186/1471-2105-12-172>.

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
