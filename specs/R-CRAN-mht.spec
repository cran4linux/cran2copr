%global packname  mht
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          Multiple Hypothesis Testing for Variable Selection inHigh-Dimensional Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 

%description
Multiple Hypothesis Testing For Variable Selection in high dimensional
linear models. This package performs variable selection with multiple
hypothesis testing, either for ordered variable selection or non-ordered
variable selection. In both cases, a sequential procedure is performed. It
starts to test the null hypothesis "no variable is relevant"; if this
hypothesis is rejected, it then tests "only the first variable is
relevant", and so on until the null hypothesis is accepted.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
