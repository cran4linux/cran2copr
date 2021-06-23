%global __brp_check_rpaths %{nil}
%global packname  tigger
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Infers Novel Immunoglobulin Alleles from Sequencing Data

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-alakazam >= 1.0.0
BuildRequires:    R-CRAN-shazam >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-tidyr >= 0.1.0
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-alakazam >= 1.0.0
Requires:         R-CRAN-shazam >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-tidyr >= 0.1.0
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-lazyeval 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringi 

%description
Infers the V genotype of an individual from immunoglobulin (Ig) repertoire
sequencing data (AIRR-Seq, Rep-Seq). Includes detection of any novel
alleles. This information is then used to correct existing V allele calls
from among the sample sequences. Citations: Gadala-Maria, et al (2015)
<doi:10.1073/pnas.1417683112>. Gadala-Maria, et al (2019)
<doi:10.3389/fimmu.2019.00129>.

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
