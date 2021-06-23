%global __brp_check_rpaths %{nil}
%global packname  mhurdle
%global packver   1.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Hurdle Tobit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-texreg 
Requires:         R-methods 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-truncreg 
Requires:         R-CRAN-maxLik 
Requires:         R-survival 
Requires:         R-CRAN-texreg 

%description
Estimation of models with zero left-censored variables. Null values may be
caused by a selection process (Cragg (1971) <doi:10.2307/1909582>),
insufficient resources (Tobin (1958) <doi:10.2307/1907382>) or infrequency
of purchase (Deaton and Irish (1984) <doi:10.1016/0047-2727(84)90067-7>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
