%global packname  MXM
%global packver   1.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.8
Release:          1%{?dist}
Summary:          Feature Selection (Including Multiple Solutions) and BayesianNetworks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-relations 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-geepack 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-CRAN-ordinal 
Requires:         R-nnet 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-relations 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-geepack 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-Hmisc 

%description
Many feature selection methods for a wide range of response variables,
including minimal, statistically-equivalent and equally-predictive feature
subsets. Bayesian network algorithms and related functions are also
included. The package name 'MXM' stands for "Mens eX Machina", meaning
"Mind from the Machine" in Latin. References: a) Lagani, V. and Athineou,
G. and Farcomeni, A. and Tsagris, M. and Tsamardinos, I. (2017). Feature
Selection with the R Package MXM: Discovering Statistically Equivalent
Feature Subsets. Journal of Statistical Software, 80(7).
<doi:10.18637/jss.v080.i07>. b) Tsagris, M., Lagani, V. and Tsamardinos,
I. (2018). Feature selection for high-dimensional temporal data. BMC
Bioinformatics, 19:17. <doi:10.1186/s12859-018-2023-7>. c) Tsagris, M.,
Borboudakis, G., Lagani, V. and Tsamardinos, I. (2018). Constraint-based
causal discovery with mixed data. International Journal of Data Science
and Analytics, 6(1): 19-30. <doi:10.1007/s41060-018-0097-y>. d) Tsagris,
M., Papadovasilakis, Z., Lakiotaki, K. and Tsamardinos, I. (2018).
Efficient feature selection on gene expression data: Which algorithm to
use? BioRxiv. <doi:10.1101/431734>. e) Tsagris, M. (2019). Bayesian
Network Learning with the PC Algorithm: An Improved and Correct Variation.
Applied Artificial Intelligence, 33(2):101-123.
<doi:10.1080/08839514.2018.1526760>. f) Tsagris, M. and Tsamardinos, I.
(2019). Feature selection with the R package MXM. F1000Research 7: 1505.
<doi:10.12688/f1000research.16216.2>. g) Borboudakis, G. and Tsamardinos,
I. (2019). Forward-Backward Selection with Early Dropping. Journal of
Machine Learning Research 20: 1-39.

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
