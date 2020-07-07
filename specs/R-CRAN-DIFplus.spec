%global packname  DIFplus
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Multilevel Mantel-Haenszel Statistics for Differential ItemFunctioning Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TestDataImputation 
BuildRequires:    R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-TestDataImputation 
Requires:         R-CRAN-plyr 

%description
Clustered or multilevel data structures are common in the assessment of
differential item functioning (DIF), particularly in the context of
large-scale assessment programs. This package allows users to implement
extensions of the Mantel-Haenszel DIF detection procedures in the presence
of multilevel data based on the work of Begg (1999)
<doi:10.1111/j.0006-341X.1999.00302.x>, Begg & Paykin (2001)
<doi:10.1080/00949650108812115>, and French & Finch (2013)
<doi:10.1177/0013164412472341>.

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
%{rlibdir}/%{packname}/INDEX
