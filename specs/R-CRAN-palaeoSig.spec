%global packname  palaeoSig
%global packver   2.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Significance Tests for Palaeoenvironmental Reconstructions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-rioja 
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-assertr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-rioja 
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-assertr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 

%description
Several tests of quantitative palaeoenvironmental reconstructions from
microfossil assemblages, including the null model tests of the
statistically significant of reconstructions developed by Telford and
Birks (2011) <doi:10.1016/j.quascirev.2011.03.002>, and tests of the
effect of spatial autocorrelation on transfer function model performance
using methods from Telford and Birks (2009)
<doi:10.1016/j.quascirev.2008.12.020> and Trachsel and Telford (2016)
<doi:10.5194/cp-12-1215-2016>. Age-depth models with generalized
mixed-effect regression from Heegaard et al (2005)
<doi:10.1191/0959683605hl836rr> are also included.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
