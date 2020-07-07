%global packname  FPV
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}
Summary:          Testing Hypotheses via Fuzzy P-Value in Fuzzy Environment

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FuzzyNumbers 
BuildRequires:    R-CRAN-FuzzyNumbers.Ext.2 
Requires:         R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-FuzzyNumbers.Ext.2 

%description
The main goal of this package is drawing the membership function of the
fuzzy p-value which is defined as a fuzzy set on the unit interval for
three following problems: (1) testing crisp hypotheses based on fuzzy
data, see Filzmoser and Viertl (2004) <doi:10.1007/s001840300269>, (2)
testing fuzzy hypotheses based on crisp data, see Parchami et al. (2010)
<doi:10.1007/s00362-008-0133-4>, and (3) testing fuzzy hypotheses based on
fuzzy data, see Parchami et al. (2012) <doi:10.1007/s00362-010-0353-2>. In
all cases, the fuzziness of data or / and the fuzziness of the boundary of
null fuzzy hypothesis transported via the p-value function and causes to
produce the fuzzy p-value. If the p-value is fuzzy, it is more appropriate
to consider a fuzzy significance level for the problem. Therefore, the
comparison of the fuzzy p-value and the fuzzy significance level is
evaluated by a fuzzy ranking method in this package.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
