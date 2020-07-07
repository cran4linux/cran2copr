%global packname  modopt.matlab
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          'MatLab'-Style Modeling of Optimization Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.glpk 
BuildRequires:    R-CRAN-ROI.plugin.quadprog 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.glpk 
Requires:         R-CRAN-ROI.plugin.quadprog 

%description
'MatLab'-Style Modeling of Optimization Problems with 'R'. This package
provides a set of convenience functions to transform a 'MatLab'-style
optimization modeling structure to its 'ROI' equivalent.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/test.intlinprog.R
%doc %{rlibdir}/%{packname}/test.linprog.R
%doc %{rlibdir}/%{packname}/test.quadprog.R
%{rlibdir}/%{packname}/INDEX
