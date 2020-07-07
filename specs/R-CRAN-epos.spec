%global packname  epos
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Epilepsy Ontologies Similarities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-TopKLists 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-TopKLists 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xtable 

%description
Analysis and visualization of similarities between epilepsy ontologies
based on text mining results by comparing ranked lists of co-occurring
drug terms in the corpus of LIVIVO. The ranked result lists of
neurological drug terms co-occurring with named entities from the epilepsy
ontologies EpSO, ESSO, and EPILONT are aggregated in order to generate two
different results: an overview table of drugs that are relevant to
epilepsy created with the method createNeuroTable, and a plot of tanimoto
similarity coefficients between the aggregated list of drug terms against
the list of drug terms from each of the ontologies created with the method
createTanimotoBaseline(). The alignment of the Top-K Ranked Lists is
conducted using the R-package TopKLists
<https://cran.r-project.org/package=TopKLists>. The source data to create
the ranked lists of drug names is produced using the text mining workflows
described in Mueller, Bernd and Hagelstein, Alexandra (2016)
<doi:10.4126/FRL01-006408558> and Mueller, Bernd et al. (2017)
<doi:10.1007/978-3-319-58694-6_22>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
