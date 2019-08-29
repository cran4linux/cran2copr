%global packname  gmeta
%global packver   2.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}
Summary:          Meta-Analysis via a Unified Framework of Confidence Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-binom 
Requires:         R-stats 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-binom 

%description
An implementation of an all-in-one function for a wide range of
meta-analysis problems. It contains three functions. The gmeta() function
unifies all standard meta-analysis methods and also several newly
developed ones under a framework of combining confidence distributions
(CDs). Specifically, the package can perform classical p-value combination
methods (such as methods of Fisher, Stouffer, Tippett, etc.), fit
meta-analysis fixed-effect and random-effects models, and synthesizes 2x2
tables. Furthermore, it can perform robust meta-analysis, which provides
protection against model-misspecifications, and limits the impact of any
unknown outlying studies. In addition, the package implements two exact
meta-analysis methods from synthesizing 2x2 tables with rare events (e.g.,
zero total event). The np.gmeta() function summarizes information obtained
from multiple studies and makes inference for study-level parameters with
no distributional assumption. Specifically, it can construct confidence
intervals for unknown, fixed study-level parameters via confidence
distribution. Furthermore, it can perform estimation via asymptotic
confidence distribution whether tie or near tie condition exist or not.
The plot.gmeta() function to visualize individual and combined CDs through
extended forest plots is also available. Compared to version 2.2-6,
version 2.3-0 contains a new function np.gmeta().

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
