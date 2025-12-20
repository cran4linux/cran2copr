%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Buddle
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Deep Learning for Statistical Classification and Regression Analysis with Random Effects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-graphics 

%description
Statistical classification and regression have been popular among various
fields and stayed in the limelight of scientists of those fields. Examples
of the fields include clinical trials where the statistical classification
of patients is indispensable to predict the clinical courses of diseases.
Considering the negative impact of diseases on performing daily tasks,
correctly classifying patients based on the clinical information is vital
in that we need to identify patients of the high-risk group to develop a
severe state and arrange medical treatment for them at an opportune
moment. Deep learning - a part of artificial intelligence - has gained
much attention, and research on it burgeons during past decades: see, e.g,
Kazemi and Mirroshandel (2018) <DOI:10.1016/j.artmed.2017.12.001>. It is a
veritable technique which was originally designed for the classification,
and hence, the Buddle package can provide sublime solutions to various
challenging classification and regression problems encountered in the
clinical trials. The Buddle package is based on the back-propagation
algorithm - together with various powerful techniques such as batch
normalization and dropout - which performs a multi-layer feed-forward
neural network: see Krizhevsky et. al (2017) <DOI:10.1145/3065386>,
Schmidhuber (2015) <DOI:10.1016/j.neunet.2014.09.003> and LeCun et al.
(1998) <DOI:10.1109/5.726791> for more details. This package contains two
main functions: TrainBuddle() and FetchBuddle(). TrainBuddle() builds a
feed-forward neural network model and trains the model. FetchBuddle()
recalls the trained model which is the output of TrainBuddle(), classifies
or regresses given data, and make a final prediction for the data.

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
