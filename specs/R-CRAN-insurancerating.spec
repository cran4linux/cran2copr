%global packname  insurancerating
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Analytic Insurance Rating Techniques

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ciTools 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-evtree 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ciTools 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-evtree 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-mgcv 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Methods for insurance rating. It helps actuaries to implement GLMs within
all relevant steps needed to construct a risk premium from raw data. It
provides a data driven strategy for the construction of insurance tariff
classes. This strategy is based on the work by Antonio and Valdez (2012)
<doi:10.1007/s10182-011-0152-7>. It also provides recipes on how to easily
perform one-way, or univariate, analyses on an insurance portfolio. In
addition it adds functionality to include reference categories in the
levels of the coefficients in the output of a generalized linear
regression analysis.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
