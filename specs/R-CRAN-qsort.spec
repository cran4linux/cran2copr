%global packname  qsort
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Scoring Q-Sort Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-purrr 
Requires:         R-stats 

%description
Computes scores from Q-sort data, using criteria sorts and derived scales
from subsets of items. The 'qsort' package includes descriptions and
scoring procedures for four different Q-sets commonly used in
developmental psychology research: Attachment Q-set (version 3.0) (Waters,
1995, <doi:10.1111/j.1540-5834.1995.tb00214.x>); California Child Q-set
(Block and Block, 1969, <doi:10.1037/0012-1649.21.3.508>); Maternal
Behaviour Q-set (version 3.1) (Pederson et al., 1999,
<https://ir.lib.uwo.ca/cgi/viewcontent.cgi?article=1000&context=psychologypub>);
Preschool Q-set (Baumrind, 1968 revised by Wanda Bronson,
<doi:10.1111/j.1540-5834.1995.tb00214.x>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
