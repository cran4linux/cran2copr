%global packname  HCTR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Higher Criticism Tuned Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncvreg >= 3.11.1
BuildRequires:    R-CRAN-harmonicmeanp >= 3.0
BuildRequires:    R-CRAN-glmnet >= 2.0.18
BuildRequires:    R-CRAN-Rdpack >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-ncvreg >= 3.11.1
Requires:         R-CRAN-harmonicmeanp >= 3.0
Requires:         R-CRAN-glmnet >= 2.0.18
Requires:         R-CRAN-Rdpack >= 0.11.0
Requires:         R-MASS 
Requires:         R-stats 

%description
A novel searching scheme for tuning parameter in high-dimensional
penalized regression. We propose a new estimate of the regularization
parameter based on an estimated lower bound of the proportion of false
null hypotheses (Meinshausen and Rice (2006)
<doi:10.1214/009053605000000741>). The bound is estimated by applying the
empirical null distribution of the higher criticism statistic, a
second-level significance testing, which is constructed by dependent
p-values from a multi-split regression and aggregation method (Jeng, Zhang
and Tzeng (2019) <doi:10.1080/01621459.2018.1518236>). An estimate of
tuning parameter in penalized regression is decided corresponding to the
lower bound of the proportion of false null hypotheses. Different
penalized regression methods are provided in the multi-split algorithm.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
