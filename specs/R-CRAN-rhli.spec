%global packname  rhli
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}
Summary:          An R Implementation of the FIS MarketMap C-Toolkit

License:          AGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Complete access from 'R' to the FIS 'MarketMap C-Toolkit' ('FAME C-HLI').
'FAME' is a fully integrated software and database management system from
FIS that provides the following capabilities: Time series and
cross-sectional data management; Financial calculation, data analysis,
econometrics, and forecasting; Table generation and detailed multicolor,
presentation-quality report writing; Multicolor, presentation-quality
graphics; "What-if" analysis; Application development and structured
programming; Data transfer to and from other applications; Tools for
building customized graphical user interfaces.

%prep
%setup -q -c -n %{packname}
rm -f %{packname}/src/Makevars*
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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
