%global packname  HGMND
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Heterogeneous Graphical Model for Non-Negative Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-genscore 
Requires:         R-CRAN-genscore 

%description
Graphical model is an informative and powerful tool to explore the
conditional dependence relationships among variables. The traditional
Gaussian graphical model and its extensions either have a Gaussian
assumption on the data distribution or assume the data are homogeneous.
However, there are data with complex distributions violating these two
assumptions. For example, the air pollutant concentration records are
non-negative and, hence, non-Gaussian. Moreover, due to climate changes,
distributions of these concentration records in different months of a year
can be far different, which means it is uncertain whether datasets from
different months are homogeneous. Methods with a Gaussian or homogeneous
assumption may incorrectly model the conditional dependence relationships
among variables. Therefore, we propose a heterogeneous graphical model for
non-negative data (HGMND) to simultaneously cluster multiple datasets and
estimate the conditional dependence matrix of variables from a
non-Gaussian and non-negative exponential family in each cluster.

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
