%global packname  shazam
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Immunoglobulin Somatic Hypermutation Analysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-stringi >= 1.1.3
BuildRequires:    R-CRAN-alakazam >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-kedd 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-stringi >= 1.1.3
Requires:         R-CRAN-alakazam >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-ape 
Requires:         R-CRAN-diptest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-kedd 
Requires:         R-KernSmooth 
Requires:         R-CRAN-lazyeval 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-seqinr 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Provides a computational framework for analyzing mutations in
immunoglobulin (Ig) sequences. Includes methods for Bayesian estimation of
antigen-driven selection pressure, mutational load quantification,
building of somatic hypermutation (SHM) models, and model-dependent
distance calculations. Also includes empirically derived models of SHM for
both mice and humans. Citations: Gupta and Vander Heiden, et al (2015)
<doi:10.1093/bioinformatics/btv359>, Yaari, et al (2012)
<doi:10.1093/nar/gks457>, Yaari, et al (2013)
<doi:10.3389/fimmu.2013.00358>, Cui, et al (2016)
<doi:10.4049/jimmunol.1502263>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
