%global __brp_check_rpaths %{nil}
%global packname  TrendInTrend
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Odds Ratio Estimation and Power Calculation for the Trend inTrend Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pracma 

%description
Estimation of causal odds ratio and power calculation given trends in
exposure prevalence and outcome frequencies of stratified data.

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
