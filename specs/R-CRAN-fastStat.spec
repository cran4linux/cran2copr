%global packname  fastStat
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Faster for Statistic Work

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-set 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-set 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-do 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-tseries 
Requires:         R-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
When we do statistic work, we need to see the structure of the data.
list.str() function will help you see the structure of the data quickly.
list.plot() function can help you check every variable in your dataframe.
table_one() function will make it easy to make a baseline table including
difference tests. uv_linear(), uv_logit(), uv_cox(), uv_logrank() will
give you a hand to do univariable regression analysis, while mv_linear(),
mv_logit() and mv_cox() will carry out multivariable regression analysis.

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
%{rlibdir}/%{packname}/INDEX
