%global packname  CGManalyzer
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Continuous Glucose Monitoring Data Analyzer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains all of the functions necessary for the complete analysis of a
continuous glucose monitoring study and can be applied to data measured by
various existing 'CGM' devices such as 'FreeStyle Libre', 'Glutalor',
'Dexcom' and 'Medtronic CGM'. It reads a series of data files, is able to
convert various formats of time stamps, can deal with missing values,
calculates both regular statistics and nonlinear statistics, and conducts
group comparison. It also displays results in a concise format. Also
contains two unique features new to 'CGM' analysis: one is the
implementation of strictly standard mean difference and the class of
effect size; the other is the development of a new type of plot called
antenna plot. It corresponds to 'Zhang
XD'(2018)<doi:10.1093/bioinformatics/btx826>'s article 'CGManalyzer: an R
package for analyzing continuous glucose monitoring studies'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/exampleDATA
%doc %{rlibdir}/%{packname}/SPEC
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
