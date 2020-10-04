%global packname  tbma
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Tree-Based Moving Average Forecasting Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppRoll 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-RcppRoll 

%description
We provide a forecasting model for time series forecasting problems with
predictors. The offered model, which is based on a submitted research and
called tree-based moving average (TBMA), is based on the integration of
the moving average approach to tree-based ensemble approach.  The
tree-based ensemble models can capture the complex correlations between
the predictors and response variable but lack in modelling time series
components. The integration of the moving average approach to the
tree-based ensemble approach helps the TBMA model to handle both
correlations and autocorrelations in time series data. This package
provides a tbma() forecasting function that utilizes the ranger() function
from the 'ranger' package. With the help of the ranger() function, various
types of tree-based ensemble models, such as extremely randomized trees
and random forests, can be used in the TBMA model.

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
