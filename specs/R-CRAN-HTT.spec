%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing Tree

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 

%description
A novel decision tree algorithm in the hypothesis testing framework. The
algorithm examines the distribution difference between two child nodes
over all possible binary partitions. The test statistic of the hypothesis
testing is equivalent to the generalized energy distance, which enables
the algorithm to be more powerful in detecting the complex structure, not
only the mean difference. It is applicable for numeric, nominal, ordinal
explanatory variables and the response in general metric space of strong
negative type. The algorithm has superior performance compared to other
tree models in type I error, power, prediction accuracy, and complexity.

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
