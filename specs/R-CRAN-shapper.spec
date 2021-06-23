%global __brp_check_rpaths %{nil}
%global packname  shapper
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Wrapper of Python Library 'shap'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-ggplot2 

%description
Provides SHAP explanations of machine learning models. In applied machine
learning, there is a strong belief that we need to strike a balance
between interpretability and accuracy. However, in field of the
Interpretable Machine Learning, there are more and more new ideas for
explaining black-box models. One of the best known method for local
explanations is SHapley Additive exPlanations (SHAP) introduced by
Lundberg, S., et al., (2016) <arXiv:1705.07874> The SHAP method is used to
calculate influences of variables on the particular observation. This
method is based on Shapley values, a technique used in game theory. The R
package 'shapper' is a port of the Python library 'shap'.

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
