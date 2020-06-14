%global packname  outForest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Multivariate Outlier Detection and Replacement

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-missRanger >= 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-missRanger >= 2.1.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ranger 

%description
Provides a random forest based implementation of the method described in
Chapter 7.1.2 (Regression model based anomaly detection) of Chandola et
al. (2009) <doi.acm.org/10.1145/1541880.1541882>. It works as follows:
Each numeric variable is regressed onto all other variables by a random
forest. If the scaled absolute difference between observed value and
out-of-bag prediction of the corresponding random forest is suspiciously
large, then a value is considered an outlier. The package offers different
options to replace such outliers, e.g. by realistic values found via
predictive mean matching. Once the method is trained on a reference data,
it can be applied to new data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
