%global packname  ecoval
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Procedures for Ecological Assessment of Surface Waters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-utility 
BuildRequires:    R-CRAN-rivernet 
BuildRequires:    R-CRAN-jpeg 
Requires:         R-CRAN-utility 
Requires:         R-CRAN-rivernet 
Requires:         R-CRAN-jpeg 

%description
Functions for evaluating and visualizing ecological assessment procedures
for surface waters containing physical, chemical and biological
assessments in the form of value functions.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ecoval_manual_plots.r
%doc %{rlibdir}/%{packname}/ecoval.dictionaries.default.dat
%doc %{rlibdir}/%{packname}/msk.macrophytes.2017_ListTaxa.dat
%doc %{rlibdir}/%{packname}/msk.macrophytes.2017_RiverTypes_DefLimitsUnc.dat
%doc %{rlibdir}/%{packname}/msk.macrophytes.2017_RiverTypes_DefObsUnc.dat
%doc %{rlibdir}/%{packname}/msk.macrophytes.2017_RiverTypes_DefStruct.dat
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
