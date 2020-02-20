%global packname  QTLRel
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Tools for Mapping of Quantitative Traits of Genetically RelatedIndividuals and Calculating Identity Coefficients fromPedigrees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
Requires:         R-CRAN-gdata 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-lattice 
Requires:         R-stats 

%description
This software provides tools for quantitative trait mapping in populations
such as advanced intercross lines where relatedness among individuals
should not be ignored. It can estimate background genetic variance
components, impute missing genotypes, simulate genotypes, perform a genome
scan for putative quantitative trait loci (QTL), and plot mapping results.
It also has functions to calculate identity coefficients from pedigrees,
especially suitable for pedigrees that consist of a large number of
generations, or estimate identity coefficients from genotypic data in
certain circumstances.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
