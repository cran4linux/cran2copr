%global packname  likeLTD
%global packver   6.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.3.0
Release:          3%{?dist}
Summary:          Tools to Evaluate DNA Profile Evidence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-rtf 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-tools 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-rtf 
Requires:         R-CRAN-gdata 
Requires:         R-tools 
Requires:         R-tcltk 

%description
Tools to determine DNA profile Weight of Evidence. For further information
see the 'likeLTD' guide provided, Balding, D.J. (2013)
<DOI:10.1073/pnas.1219739110>, or Steele, C.D. et al. (2016)
<DOI:10.1515/sagmb-2016-0038>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
