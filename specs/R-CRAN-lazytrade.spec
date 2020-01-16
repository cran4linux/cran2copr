%global packname  lazytrade
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}
Summary:          Learn Computer and Data Science using Algorithmic Trading

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-ReinforcementLearning 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-h2o 
Requires:         R-CRAN-ReinforcementLearning 
Requires:         R-CRAN-openssl 

%description
Provide sets of functions and methods to learn and practice data science
using idea of algorithmic trading. Main goal is to process information
within "Decision Support System" to come up with analysis or predictions.
There are several utilities such as dynamic and adaptive risk management
using reinforcement learning and even functions to generate predictions of
price changes using pattern recognition deep regression learning.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
