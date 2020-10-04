%global packname  spatstat.Knet
%global packver   1.12-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.2
Release:          3%{?dist}%{?buildtag}
Summary:          Extension to 'spatstat' for Large Datasets on a Linear Network

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat >= 1.62.2
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-spatstat >= 1.62.2
Requires:         R-CRAN-spatstat.utils 
Requires:         R-Matrix 

%description
Extension to the 'spatstat' package, for analysing large datasets of
spatial points on a network. The geometrically-corrected K function is
computed using the memory-efficient tree-based algorithm described by
Rakshit, Baddeley and Nair (2019).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
