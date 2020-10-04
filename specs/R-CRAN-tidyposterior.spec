%global packname  tidyposterior
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Analysis to Compare Models using Resampling Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rstanarm >= 2.15.3
BuildRequires:    R-CRAN-tidyr >= 0.7.1
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-rsample >= 0.0.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-rstanarm >= 2.15.3
Requires:         R-CRAN-tidyr >= 0.7.1
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-rsample >= 0.0.2
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 

%description
Bayesian analysis used here to answer the question: "when looking at
resampling results, are the differences between models 'real'?" To answer
this, a model can be created were the performance statistic is the
resampling statistics (e.g. accuracy or RMSE). These values are explained
by the model types. In doing this, we can get parameter estimates for each
model's affect on performance and make statistical (and practical)
comparisons between models. The methods included here are similar to
Benavoli et al (2017) <http://jmlr.org/papers/v18/16-305.html>.

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
