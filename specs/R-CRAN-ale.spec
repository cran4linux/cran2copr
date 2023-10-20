%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ale
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Machine Learning and Statistical Inference with Accumulated Local Effects (ALE)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-yaImpute 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ellipsis 
Requires:         R-grDevices 
Requires:         R-CRAN-labeling 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-yaImpute 

%description
Accumulated Local Effects (ALE) were initially developed as a
model-agnostic approach for global explanations of the results of
black-box machine learning algorithms. ALE has a key advantage over other
approaches like partial dependency plots (PDP) and SHapley Additive
exPlanations (SHAP): its values represent a clean functional decomposition
of the model. As such, ALE values are not affected by the presence or
absence of interactions among variables in a mode. Moreover, its
computation is relatively rapid. This package rewrites the original code
from the 'ALEPlot' package for calculating ALE data and it completely
reimplements the plotting of ALE values. It also extends the original ALE
concept to add bootstrap-based confidence intervals and ALE-based
statistics that can be used for statistical inference. For more details,
see Okoli, Chitu. 2023. “Statistical Inference Using Machine Learning and
Classical Techniques Based on Accumulated Local Effects (ALE).” arXiv.
<arXiv:2310.09877>. <doi:10.48550/arXiv.2310.09877>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
