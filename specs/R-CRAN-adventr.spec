%global __brp_check_rpaths %{nil}
%global packname  adventr
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive R Tutorials to Accompany Field (2016), "An Adventurein Statistics"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-learnr 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lm.beta 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-sjstats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-learnr 
Requires:         R-CRAN-BayesFactor 
Requires:         R-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-car 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lm.beta 
Requires:         R-nlme 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-sjstats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WRS2 

%description
Interactive 'R' tutorials written using 'learnr' for Field (2016), "An
Adventure in Statistics", <ISBN:9781446210451>. Topics include general
workflow in 'R' and 'Rstudio', the 'R' environment and 'tidyverse',
summarizing data, model fitting, central tendency, visualising data using
'ggplot2', inferential statistics and robust estimation, hypothesis
testing, the general linear model, comparing means, repeated measures
designs, factorial designs, multilevel models, growth models, and
generalized linear models (logistic regression).

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
%{rlibdir}/%{packname}
