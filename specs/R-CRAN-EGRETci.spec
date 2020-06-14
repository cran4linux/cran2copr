%global packname  EGRETci
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          2%{?dist}
Summary:          Exploration and Graphics for RivEr Trends Confidence Intervals

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EGRET >= 3.0.0
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-EGRET >= 3.0.0
Requires:         R-CRAN-binom 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Collection of functions to evaluate uncertainty of results from water
quality analysis using the Weighted Regressions on Time Discharge and
Season (WRTDS) method. This package is an add-on to the EGRET package that
performs the WRTDS analysis. The WRTDS modeling method was initially
introduced and discussed in Hirsch et al. (2010)
<doi:10.1111/j.1752-1688.2010.00482.x>, and expanded in Hirsch and De
Cicco (2015) <doi:10.3133/tm4A10>. The paper describing the uncertainty
and confidence interval calculations is Hirsch et al. (2015)
<doi:10.1016/j.envsoft.2015.07.017>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
