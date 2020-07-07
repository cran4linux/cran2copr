%global packname  OptSig
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}
Summary:          Optimal Level of Significance for Regression and OtherStatistical Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pwr 
Requires:         R-CRAN-pwr 

%description
Calculates the optimal level of significance based on a decision-theoretic
approach. The optimal level is chosen so that the expected loss from
hypothesis testing is minimized. A range of statistical tests are covered,
including the test for the population mean, population proportion, and a
linear restriction in a multiple regression model. The details are covered
in Kim, Jae H. and Choi, In, 2020, Choosing the Level of Significance: A
Decision-Theoretic Approach, Abacus. See also Kim, Jae H., 2020,
Decision-theoretic hypothesis testing: A primer with R package OptSig, The
American Statistician.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
