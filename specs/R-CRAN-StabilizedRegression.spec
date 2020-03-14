%global packname  StabilizedRegression
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Stabilizing Regression and Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-MASS 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
Contains an implementation of 'StabilizedRegression', a regression
framework for heterogeneous data introduced in Pfister et al. (2019)
<arXiv:1911.01850>. The procedure uses averaging to estimate a regression
of a set of predictors X on a response variable Y by enforcing stability
with respect to a given environment variable. The resulting regression
leads to a variable selection procedure which allows to distinguish
between stable and unstable predictors. The package further implements a
visualization technique which illustrates the trade-off between stability
and predictiveness of individual predictors.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
