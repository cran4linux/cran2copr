%global packname  model4you
%global packver   0.9-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          3%{?dist}
Summary:          Stratified and Personalised Models Based on Model-Based Treesand Forests

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.6
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-survival 
Requires:         R-CRAN-partykit >= 1.2.6
Requires:         R-grid 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gridExtra 
Requires:         R-survival 

%description
Model-based trees for subgroup analyses in clinical trials and model-based
forests for the estimation and prediction of personalised treatment
effects (personalised models). Currently partitioning of linear models,
lm(), generalised linear models, glm(), and Weibull models, survreg(), is
supported.  Advanced plotting functionality is supported for the trees and
a test for parameter heterogeneity is provided for the personalised
models. For details on model-based trees for subgroup analyses see
Seibold, Zeileis and Hothorn (2016) <doi:10.1515/ijb-2015-0032>; for
details on model-based forests for estimation of individual treatment
effects see Seibold, Zeileis and Hothorn (2017)
<doi:10.1177/0962280217693034>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/JORS
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/reproducing_papers
%{rlibdir}/%{packname}/INDEX
