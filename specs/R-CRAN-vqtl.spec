%global packname  vqtl
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Genome Scans to Accommodate and Target Genetic and Non-GeneticEffects on Trait Variance in Test Crosses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dglm 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-qtl 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dglm 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-qtl 

%description
In recognition that there are many factors (genetic loci, macro- genetic
factors such as sex, and environmental factors) that influence the extent
of environmental variation, the 'vqtl' package conducts genome scans that
accommodate and target these factors. The main functions of this package,
scanonevar() and scanonevar.perm() take as input a cross object from the
popular 'qtl' package, as described in Corty and Valdar (2019)
<doi:10.1534/g3.118.200642>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
