%global packname  DALEX
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          moDel Agnostic Language for Exploration and eXplanation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-iBreakDown 
BuildRequires:    R-CRAN-ingredients 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-iBreakDown 
Requires:         R-CRAN-ingredients 

%description
Unverified black box model is the path to the failure. Opaqueness leads to
distrust. Distrust leads to ignoration. Ignoration leads to rejection.
DALEX package xrays any model and helps to explore and explain its
behaviour. Machine Learning (ML) models are widely used and have various
applications in classification or regression. Models created with
boosting, bagging, stacking or similar techniques are often used due to
their high performance. But such black-box models usually lack of direct
interpretability. DALEX package contains various methods that help to
understand the link between input variables and model output. Implemented
methods help to explore model on the level of a single instance as well as
a level of the whole dataset. All model explainers are model agnostic and
can be compared across different models. DALEX package is the cornerstone
for 'DrWhy.AI' universe of packages for visual model exploration. Find
more details in (Biecek 2018) <arXiv:1806.08915>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
