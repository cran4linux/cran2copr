%global packname  QuantumClone
%global packver   1.0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Clustering Mutations using High Throughput Sequencing (HTS) Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-fpc 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-fpc 

%description
Using HTS data, clusters mutations in order to recreate putative clones
from the data provided. It requires genotype at the location of the
variant as well as the depth of coverage and number of reads supporting
the mutation. Additional information may be provided, such as the
contamination in the tumor sample. This package also provides a function
QuantumCat() which simulates data obtained from tumor sequencing.

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
