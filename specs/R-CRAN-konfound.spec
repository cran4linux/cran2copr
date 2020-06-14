%global packname  konfound
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Quantify the Robustness of Causal Inferences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Statistical methods that quantify the conditions necessary to alter
inferences, also known as sensitivity analysis, are becoming increasingly
important to a variety of quantitative sciences. A series of recent works,
including Frank (2000) <doi:10.1177/0049124100029002001> and Frank et al.
(2013) <doi:10.3102/0162373713493129> extend previous sensitivity analyses
by considering the characteristics of omitted variables or unobserved
cases that would change an inference if such variables or cases were
observed. These analyses generate statements such as "an omitted variable
would have to be correlated at xx with the predictor of interest (e.g.,
treatment) and outcome to invalidate an inference of a treatment effect".
Or "one would have to replace pp percent of the observed data with null
hypothesis cases to invalidate the inference". We implement these recent
developments of sensitivity analysis and provide modules to calculate
these two robustness indices and generate such statements in R. In
particular, the functions konfound(), pkonfound() and mkonfound() allow
users to calculate the robustness of inferences for a user's own model, a
single published study and multiple studies respectively.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
