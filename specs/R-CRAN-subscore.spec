%global packname  subscore
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}
Summary:          Computing Subscores in Classical Test Theory and Item ResponseTheory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CTT 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-irtoys 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-cocor 
BuildRequires:    R-boot 
Requires:         R-CRAN-CTT 
Requires:         R-stats 
Requires:         R-CRAN-irtoys 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-cocor 
Requires:         R-boot 

%description
Functions for computing subscores for a test using different methods in
both classical test theory (CTT) and item response theory (IRT). This
package enables three sets of subscoring methods within the framework of
CTT and IRT: Wainer's augmentation method, Haberman's three subscoring
methods, and Yen's objective performance index (OPI). The package also
includes the function to compute Proportional Reduction of Mean Squared
Errors (PRMSEs) in Haberman's methods which are used to examine whether
test subscores are of added value.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
