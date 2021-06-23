%global __brp_check_rpaths %{nil}
%global packname  feamiR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classification and Feature Selection for microRNA/mRNA Interactions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reticulate 

%description
Comprises a pipeline for predicting microRNA/mRNA interactions, as
detailed in Williams, Calinescu, Mohorianu (2020)
<doi:10.1101/2020.12.23.424130>. Its input consists of [a] a messenger RNA
(mRNA) dataset (either in fasta format, focused on 3' UTRs or in gtf
format; for the latter, the sequences of the 3’ UTRs are generated using
the genomic coordinates), [b] a microRNA dataset (in fasta format,
retrieved from miRBase, <http://www.mirbase.org/>) and [c] an interaction
dataset (in csv format, from miRTarBase
<http://mirtarbase.cuhk.edu.cn/php/index.php>). To characterise and
predict microRNA/mRNA interactions, we use [a] statistical analyses based
on Chi-squared and Fisher exact tests and [b] Machine Learning classifiers
(decision trees, random forests and support vector machines). To enhance
the accuracy of the classifiers we also employ feature selection
approaches used in on conjunction with the classifiers. The feature
selection approaches include a voting scheme for decision trees, a measure
based on Gini index for random forests, forward feature selection and
Genetic Algorithms on SVMs. The pipeline also includes a novel approach
based on embryonic Genetic Algorithms which combines and optimises the
forward feature selection and Genetic Algorithms. All analyses, including
the classification and feature selection, are applicable on the microRNA
seed features (default), on the full microRNA features and/or flanking
features on the mRNA. The sets of features can be combined.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
