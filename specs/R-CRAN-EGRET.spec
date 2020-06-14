%global packname  EGRET
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          2%{?dist}
Summary:          Exploration and Graphics for RivEr Trends

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dataRetrieval >= 2.0.1
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-dataRetrieval >= 2.0.1
Requires:         R-survival 
Requires:         R-CRAN-fields 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-foreach 

%description
Statistics and graphics for streamflow history, water quality trends, and
the statistical modeling algorithm: Weighted Regressions on Time,
Discharge, and Season (WRTDS). The modeling method is introduced and
discussed in Hirsch et al. (2010) <doi:10.1111/j.1752-1688.2010.00482.x>,
and expanded in Hirsch and De Cicco (2015) <doi:10.3133/tm4A10>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
