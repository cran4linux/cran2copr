%global packname  shatteringdt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Provide SLT Tools for 'rpart' and 'tree' to Study Decision Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-tree 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-testthat 

%description
Learning, in Machine Learning (ML) area, is one of the most important
steps in the construction of algorithms that seek to predict a certain
task, whether this is the classification of objects, the forecast of
demand for a specific product or even the diagnosis of malignant diseases.
In ML, we can study supervised (which have a label, e.g., a class) and
unsupervised algorithms, used for tasks such as pattern detection,
grouping, among others that do not depend directly on a label. Knowing
this, the present work aims to carry out the study of different supervised
learning algorithms, in this case, the classification algorithms, more
specifically Decision Trees, to carry out an analytical study about the
steps that make up the learning process of the algorithm, exploring
concepts of the statistical learning theory (SLT) that provide tools for
studies and allow to prove issues such as the guarantee of learning of a
certain algorithm. Reference: Rodrigo Fernandes de Mello, Chaitanya
Manapragada, Albert Bifet: "Measuring the Shattering coefficient of
Decision Tree models". Expert Syst. Appl. 137: 443-452
(2019)<DOI:10.1016/j.eswa.2019.07.012>.

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
