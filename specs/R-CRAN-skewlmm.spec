%global packname  skewlmm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Scale Mixture of Skew-Normal Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 

%description
It fits scale mixture of skew-normal linear mixed models using an
expectation–maximization (EM) type algorithm, including some possibilities
for modeling the within-subject dependence. Details can be found in
Schumacher, Matos and Lachos (2020) <arXiv:2002.01040>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
