%global packname  jubilee
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Forecasting Long-Term Growth of the U.S. Stock Market andBusiness Cycles

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-splines 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-stats 
Requires:         R-CRAN-yaml 
Requires:         R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-splines 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 

%description
A long-term forecast model called "Jubilee-Tectonic model" is implemented
to forecast future returns of the U.S. stock market, Treasury yield, and
gold price. The five-factor model forecasts the 10-year and 20-year future
equity returns with high R-squared above 80 percent. It is based on linear
growth and mean reversion characteristics in the U.S. stock market. This
model also enhances the CAPE model by introducing the hypothesis that
there are fault lines in the historical CAPE, which can be calibrated and
corrected through statistical learning. In addition, it contains a module
for business cycles, optimal interest rate, and recession forecasts.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
