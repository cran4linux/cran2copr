%global packname  lazytrade
%global packver   0.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
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
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-ReinforcementLearning 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
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
price changes using pattern recognition deep regression learning. Summary
of Methods used: Awesome H2O tutorials:
<https://github.com/h2oai/awesome-h2o>, Market Type research of Van Tharp
Institute: <https://www.vantharp.com/>, Reinforcement Learning R package:
<https://CRAN.R-project.org/package=ReinforcementLearning>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
