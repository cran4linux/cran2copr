%global debug_package %{nil}
%global packname  dgo
%global packver   0.2.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.15
Release:          1%{?dist}
Summary:          Dynamic Estimation of Group-Level Opinion

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-rstan >= 2.15.1
BuildRequires:    R-CRAN-dgodata 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-rstan >= 2.15.1
Requires:         R-CRAN-dgodata 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-survey 

%description
Fit dynamic group-level item response theory (IRT) and multilevel
regression and poststratification (MRP) models from item response data.
dgo models latent traits at the level of demographic and geographic
groups, rather than individuals, in a Bayesian group-level IRT approach
developed by Caughey and Warshaw (2015) <doi:10.1093/pan/mpu021>. The
package also estimates subpopulations' average responses to single survey
items with a dynamic MRP model proposed by Park, Gelman, and Bafumi (2004)
<doi:10.11126/stanford/9780804753005.003.0011>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dgirt_details.pdf
%doc %{rlibdir}/%{packname}/models
%{rlibdir}/%{packname}/INDEX
