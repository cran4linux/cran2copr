%global packname  live
%global packver   1.5.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.13
Release:          3%{?dist}%{?buildtag}
Summary:          Local Interpretable (Model-Agnostic) Visual Explanations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-breakDown 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-forestmodel 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-breakDown 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-forestmodel 
Requires:         R-CRAN-shiny 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gower 
Requires:         R-CRAN-e1071 

%description
Interpretability of complex machine learning models is a growing concern.
This package helps to understand key factors that drive the decision made
by complicated predictive model (so called black box model). This is
achieved through local approximations that are either based on additive
regression like model or CART like model that allows for higher
interactions. The methodology is based on Tulio Ribeiro, Singh, Guestrin
(2016) <doi:10.1145/2939672.2939778>. More details can be found in
Staniak, Biecek (2018) <doi:10.32614/RJ-2018-072>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
