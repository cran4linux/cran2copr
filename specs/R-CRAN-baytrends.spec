%global packname  baytrends
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Long Term Water Quality Trend Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-dataRetrieval 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-zCompositions 
Requires:         R-CRAN-lubridate 
Requires:         R-mgcv 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-dataRetrieval 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-survival 
Requires:         R-CRAN-zCompositions 

%description
Enable users to evaluate long-term trends using a Generalized Additive
Modeling (GAM) approach. The model development includes selecting a GAM
structure to describe nonlinear seasonally-varying changes over time,
incorporation of hydrologic variability via either a river flow or
salinity, the use of an intervention to deal with method or laboratory
changes suspected to impact data values, and representation of left- and
interval-censored data. The approach has been applied to water quality
data in the Chesapeake Bay, a major estuary on the east coast of the
United States to provide insights to a range of management- and
research-focused questions.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
