%global packname  predict3d
%global packver   0.1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Draw Three Dimensional Predict Plot Using Package 'rgl'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-rgl >= 0.99.16
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggiraphExtra 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-moonBook 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TH.data 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-rgl >= 0.99.16
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggiraphExtra 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-moonBook 
Requires:         R-stats 
Requires:         R-CRAN-TH.data 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 

%description
Draw 2 dimensional and three dimensional plot for multiple regression
models using package 'ggplot2' and 'rgl'. Supports linear models (lm),
generalized linear models (glm) and local polynomial regression fittings
(loess).

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
%doc %{rlibdir}/%{packname}/figures
%{rlibdir}/%{packname}/INDEX
