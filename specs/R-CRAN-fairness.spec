%global packname  fairness
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Algorithmic Fairness Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pROC 

%description
Offers various metrics of algorithmic fairness. Fairness in machine
learning is an emerging topic with the overarching aim to critically
assess algorithms (predictive and classification models) whether their
results reinforce existing social biases. While unfair algorithms can
propagate such biases and offer prediction or classification results with
a disparate impact on various sensitive subgroups of populations (defined
by sex, gender, ethnicity, religion, income, socioeconomic status,
physical or mental disabilities), fair algorithms possess the underlying
foundation that these groups should be treated similarly / should have
similar outcomes. The fairness R package offers the calculation and
comparisons of commonly and less commonly used fairness metrics in
population subgroups. These methods are described by Calders and Verwer
(2010) <doi:10.1007/s10618-010-0190-x>, Chouldechova (2017)
<doi:10.1089/big.2016.0047>, Feldman et al. (2015)
<doi:10.1145/2783258.2783311> , Friedler et al. (2018)
<doi:10.1145/3287560.3287589> and Zafar et al. (2017)
<doi:10.1145/3038912.3052660>. The package also offers convenient
visualizations to help understand fairness metrics.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
