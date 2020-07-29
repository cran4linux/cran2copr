%global packname  DALEXtra
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Extension for 'DALEX' Package

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX >= 1.3
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-DALEX >= 1.3
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-gridExtra 

%description
Provides wrapper of various machine learning models. In applied machine
learning, there is a strong belief that we need to strike a balance
between interpretability and accuracy. However, in field of the
interpretable machine learning, there are more and more new ideas for
explaining black-box models, that are implemented in 'R'. 'DALEXtra'
creates 'DALEX' Biecek (2018) <arXiv:1806.08915> explainer for many type
of models including those created using 'python' 'scikit-learn' and
'keras' libraries, and 'java' 'h2o' library. Important part of the package
is Champion-Challenger analysis and innovative approach to model
performance across subsets of test data presented in Funnel Plot. Third
branch of 'DALEXtra' package is aspect importance analysis that provides
instance-level explanations for the groups of explanatory variables.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
