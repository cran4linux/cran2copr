%global packname  oolong
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Create Validation Tests for Automated Content Analysis

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-text2vec >= 0.6
BuildRequires:    R-CRAN-stm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-text2vec >= 0.6
Requires:         R-CRAN-stm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Intended to create standard human-in-the-loop validity tests for typical
automated content analysis such as topic modeling and dictionary-based
methods. This package offers a standard workflow with functions to
prepare, administer and evaluate a human-in-the-loop validity test. This
package provides functions for validating topic models using word
intrusion and Topic intrusion tests, as described in Chang et al. (2009)
<https://papers.nips.cc/paper/3700-reading-tea-leaves-how-humans-interpret-topic-models>.
This package also provides functions for generating gold-standard data
which are useful for validating dictionary-based methods. The default
settings of all generated tests match those suggested in Chang et al.
(2009) and Song et al. (2020) <doi:10.1080/10584609.2020.1723752>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
