%global __brp_check_rpaths %{nil}
%global packname  VFP
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Variance Function Program

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm 
BuildRequires:    R-CRAN-VCA 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-gnm 
Requires:         R-CRAN-VCA 
Requires:         R-MASS 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Variance function estimation for models proposed by W. Sadler in his
variance function program ('VFP',
<http://www.aacb.asn.au/resources/useful-tools/variance-function-program-v14>).
Here, the idea is to fit multiple variance functions to a data set and
consequently assess which function reflects the relationship 'Var ~ Mean'
best. For 'in-vitro diagnostic' ('IVD') assays modeling this relationship
is of great importance when individual test-results are used for defining
follow-up treatment of patients.

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
%doc %{rlibdir}/%{packname}/ChangLog.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/UnitTests
%{rlibdir}/%{packname}/INDEX
